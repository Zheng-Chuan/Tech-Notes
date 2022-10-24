# XMC

## 该项目的微服务架构是什么样的 通过怎样的配置来配置出来的

## 项目是如何构建一个定时任务服务的

## common service 提供了方法

## 该项目的错误异常是怎么定义的, 如何扩展

## Bean的生命周期

## 项目中是如何进行复杂的权限控制的

## 项目中的是如何定义通用的SQL, 从而支持复杂查询的

## 项目中用切面编程做了什么事情

## 项目中有没有一个地方可以使用到设计模式 用什么模式 为什么

## 持久化一个多叉树 有什么好的实践

## @PsotConstruct

## @BeforeDestory

## Notification 核心代码

    ```java
        protected void executeInternal(JobExecutionContext jobExecutionContext) {
            int threadCount = 10;

            ExecutorService executor = Executors.newThreadPool(threadCount);
            int total = 0;
            int count = 0;
            try {
                List<Notification> notifications = notificationService.getLastNotReadyNotification(threadCount);
                count = notifications.size();
                if (count > 0) {
                    List<CompletableFuture<Integer>> resultList = notifications.stream().map(notification -> CompleteFuture.supplyAsync(
                        () -> notificationService.sendNotification(notification), executor
                    )).collect(Collectors.toList());

                    total = resultList.stream().map(CompletableFuture::join).reduce(0, Integer::sum);
                }
                jobExecutionContext.getMergedJobDataMap().put(SchedulerConstants.JOB_RESULT_MESSAGE, count + " vs " + total);
            } catch (Exception e) {
                jobExecutionContext.getMergedJobDataMap().put(SchedulerConstants.JOB_RESULT_MESSAGE, count + " vs " + total + ": " + e.getMessage());
                scheduleExceptionHandler.processException(e, EngineExceptionType.EXCEPTION);
            }
        }
        
        
        
    ```
