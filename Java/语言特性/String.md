# String

## 字符串常量池 & intern()

```java
String a = "hello";                 // 如果字符串常量池中没有 “hello”, 则创建该字符串在池中, 然后返回池中引用
String b = new String("hello");     // 先在堆上创建对象, 然后将堆上对象指向字符串常量池中的 “hello” (如果池中没有则创建)

System.out.println(a == b.intern());    // true 说明 intern() 只返回池中引用
System.out.println(a == b);             // false 说明 堆中对象的引用和池中的引用不是一回事
```
1. 在编译期 new 方式创建的字符串就会被放入到编译期的字符串常量池中, 也就是说 new String() 的方式会首先去判断字符串常量池，如果没有就会新建字符串那么就会创建 2 个对象，如果已经存在就只会在堆中创建一个对象指向字符串常量池中的字符串