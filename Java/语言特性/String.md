# String

## String Pool (字符串常量池)

```java
String a = "hello";                     // 如果字符串常量池中没有 “hello”, 则创建该字符串在池中, 然后返回池中引用
String b = new String("hello"); // 先在堆上创建对象, 然后将堆上对象指向字符串常量池中的 “hello” (如果池中没有则创建)

System.out.println(a == b.intern());    // 说明 intern() 返回池中引用
System.out.println(a == b);             // 说明 堆中对象的引用和池中的引用不是一回事
```