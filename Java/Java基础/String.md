# String

## 知识
1. `String`被`final`修饰, 被初始化后不可更改.
2. 内部为 `private final byte[] value;`
3. `String`因为不可修改, 所以线程安全.
4. `StringBuilder`线程不安全 `StringByffer`线程安全, 原因在于它使用`synchronized`进行同步.
5. `String a = new String("aaa");` 这种初始化方式不会将其加入字符串常量池, 但是使用`a.intern()`方法会将其加入字符串常量池中. 而`String a = "aaa";`则直接将该字符串放到字符串常量池中.
6. 字符串常量池在 Java 7 以前是放在永久代中的, 但是在 Java 7 以后就放在堆中了. 



## 问题
1. JVM对于没有放在字符串常量池中的字符串, 会将其当做一个普通对象管理吗.
2. 为什么`String a = "aaa";`会直接将字符串放到堆中.
3. String被final修饰有什么好处.
4. `StringBuffer`和`StringBuilder`的区别是什么, 他们各自使用的使用场景有什么不同.

## 文章
1. https://stackoverflow.com/questions/10578984/what-is-java-string-interning
2. https://tech.meituan.com/2014/03/06/in-depth-understanding-string-intern.html
3. https://stackoverflow.com/questions/2971315/string-stringbuffer-and-stringbuilder
