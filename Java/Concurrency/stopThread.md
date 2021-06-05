# 线程的停止和中断
一句话概括: 停止线程的方式其实是一种规范, 不仅要求线程能够停止, 而且需要被停止线程配合我们
- 停止线程的原理:
   1. 使用interrupt()来通知, 而不是强制.

   2. 在Java中最多能做的就是告知该线程该中断了, 但是线程本身具有最终决定权来决定是不是要停止自己, Java这样设计的原因是Java认为线程本身最清楚自己在做什么事情, 所以比较好的实现线程的规范是: 让线程本身可以相应相应的中断, 线程的停止已经资源释放等工作放到线程内部自己完成.

   3. 线程通常什么情况下会停止:
      - 线程的run方法正常执行完毕
      - 线程在被阻塞的时候收到了中断信号:
         线程执行中执行到了类似Thread.sleep()这样阻塞线程的功能
         使用try catch还捕捉并且正确处理
      - 线程中每次迭代后都阻塞:
         记住一点: 中断标志位Thread.currentThread().isInterrupted() 会在被成功中断的时候置位, 被成功响应后复位.
- 实际开发中的两种最佳实践:
   1. 优先选择: 传递中断
      - 背景描述: 一般的run()方法中会调用其他的方法, 形成一个call stack.
      - 错误做法: 如果在run()方法调用的其他方法中进行InterruptedException的try catch, 那么这种做法就相当没有将这个异常上报给run()方法, 而是自己做了处理, 实际编码中如果发生了问题, 那么很难从日志中发现这种错误, run方法本身也无能为力
      - 正确做法 1: 因为实现线程的执行代码是通过重写run()来做到的, 但是run() 在Runnable中的原始定义就是 public abstract run(), 并没有任何和异常处理有关的定义, 所以run(方法是不能抛出异常的.
      ```
      package threadcoreknowledge.stopthreads;

      import threadcoreknowledge.createthreads.ThreadStyle;

      /**
      * 描述：     最佳实践：catch了InterruptedExcetion之后的优先选择：在方法签名中抛出异常 那么在run()就会强制try/catch
      */
      public class RightWayStopThreadInProd implements Runnable {

         @Override
         public void run() {
            while (true && !Thread.currentThread().isInterrupted()) {
                  System.out.println("go");
                  try {
                     throwInMethod();
                  } catch (InterruptedException e) {
                     Thread.currentThread().interrupt();
                     //保存日志、停止程序
                     System.out.println("保存日志");
                     e.printStackTrace();
                  }
            }
         }

         private void throwInMethod() throws InterruptedException {
                  Thread.sleep(2000);
         }

         public static void main(String[] args) throws InterruptedException {
            Thread thread = new Thread(new RightWayStopThreadInProd());
            thread.start();
            Thread.sleep(1000);
            thread.interrupt();
         }
      }
      ```

   2. 不想或无法传递: 在中断产生的方法内处理好中断后, 重新中断一下.
   
      如果由于各种原因, 就希望在中断抛出的地方处理好中断, 而不选择往上传递给run()方法, 那么该方法内处理完中断后, 本线程的中断标记位需要再次通过interrupt()来置位, 这样run()方法可以通过Thread.currentThread.isInterrupted()来周期性的轮询, 看看是否自己调用的方法让自己处于中断待响应状态. 
      ```
      package threadcoreknowledge.stopthreads;

      /**
      * 描述：最佳实践2：在catch子语句中调用Thread.currentThread().interrupt()来恢复设置中断状态，以便于在后续的执行中，依然能够检查到刚才发生了中断
      * 回到刚才RightWayStopThreadInProd补上中断，让它跳出
      */
      public class RightWayStopThreadInProd2 implements Runnable {

         @Override
         public void run() {
            while (true) {
                  if (Thread.currentThread().isInterrupted()) {
                     System.out.println("Interrupted，程序运行结束");
                     break;
                  }
                  reInterrupt();
            }
         }

         private void reInterrupt() {
            try {
                  Thread.sleep(2000);
            } catch (InterruptedException e) {
                  Thread.currentThread().interrupt();
                  e.printStackTrace();
            }
         }

         public static void main(String[] args) throws InterruptedException {
            Thread thread = new Thread(new RightWayStopThreadInProd2());
            thread.start();
            Thread.sleep(1000);
            thread.interrupt();
         }
      }

      ```

   3. 不应该屏蔽中断

- 响应中断的方法总结列表:
   - Object.wait()
   - Thread.sleep()
   - Thread.join()
   - java.util.concurrent.BlockingQueue.take()\
   - java.util.concurrent.locks.lockInterruptibly()
   - java.util.concurrent.CountDownLatch.await()
   - java.util.concurrent.InterruptibleChannel
   - java.nio.channels.Selector


- 错误停止线程的方法:
   1. 使用已经弃用的stop, suspend, resume方法
      
   2. 使用volatile设置boolean标记位
      虽然volatile canceled标记位可以被置位, 而且线程可以轮询去查看这个标记位并且做出相应的反应, 比如在while的循环条件里面进行这个检查, 但是, 如果线程在while循环体内被阻塞是无法被发现的, 导致线程就停在了某轮while循环内的某行代码出, 其他线程发现不了, 自己也跳不出来.
      ```
      package threadcoreknowledge.stopthreads.volatiledemo;

      import java.util.concurrent.ArrayBlockingQueue;
      import java.util.concurrent.BlockingQueue;
      import java.util.concurrent.ConcurrentLinkedQueue;

      /**
      * 描述：     演示用volatile的局限part2 陷入阻塞时，volatile是无法线程的 此例中，生产者的生产速度很快，消费者消费速度慢，所以阻塞队列满了以后，生产者会阻塞，等待消费者进一步消费
      */
      public class WrongWayVolatileCantStop {

         public static void main(String[] args) throws InterruptedException {
            ArrayBlockingQueue storage = new ArrayBlockingQueue(10);

            Producer producer = new Producer(storage);
            Thread producerThread = new Thread(producer);
            producerThread.start();
            Thread.sleep(1000);

            Consumer consumer = new Consumer(storage);
            while (consumer.needMoreNums()) {
                  System.out.println(consumer.storage.take()+"被消费了");
                  Thread.sleep(100);
            }
            System.out.println("消费者不需要更多数据了。");

            //一旦消费不需要更多数据了，我们应该让生产者也停下来，但是实际情况
            producer.canceled=true;
            System.out.println(producer.canceled);
         }
      }

      class Producer implements Runnable {

         public volatile boolean canceled = false;

         BlockingQueue storage;

         public Producer(BlockingQueue storage) {
            this.storage = storage;
         }
      ```


         @Override
         public void run() {
            int num = 0;
            try {
                  while (num <= 100000 && !canceled) {
                     if (num % 100 == 0) {
                        storage.put(num);
                        System.out.println(num + "是100的倍数,被放到仓库中了。");
                     }
                     num++;
                  }
            } catch (InterruptedException e) {
                  e.printStackTrace();
            } finally {
                  System.out.println("生产者结束运行");
            }
         }
      }
    
      class Consumer {
    
         BlockingQueue storage;
    
         public Consumer(BlockingQueue storage) {
            this.storage = storage;
         }
    
         public boolean needMoreNums() {
            if (Math.random() > 0.95) {
                  return false;
            }
            return true;
         }
      }
      ```

- 相关重要函数
   1. static boolean interrupted()
   
      返回当前线程是否被中断, 但是无论返回true还是false, 都会清除该线程的中断标记位, 表示该线程不再被中断.
   
   2. boolean isInterrupted()
   
      功能同上, 但是不清除标记位

   3. Thread.interrupted()
   
      该方法的目标对象是"当前线程", 而不管本方法是来自于哪个对象 

- 常见面试问题:
   1. 如何停止线程
      - 原理: 用interrupt来请求, 说说好处
      - 想停止线程, 要求请求方, 被停止方, 子方法被调用方相互配合
      - 最后再说错误的方法: stop/suspend已经被废弃, volatile的boolean无法处理长时间阻塞的情况
   2. 如何处理不可中断的阻塞
      - 没有通用的解决方案
      - 尽量使用可以响应中断的方法
