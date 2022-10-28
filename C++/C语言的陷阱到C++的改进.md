# 字符语法的常见陷阱

```c++
char c1 = 'yes'; // correct 截断, 有的编译器会只保留第一个字符 有的字符会保留最后一个字符
char c2 = "yes"; // wrong

const char* slash = "/"; // correct  => '/', '\0' 
const char* slash2 = '/'; // wrong 把一个字符类型赋值给一个指针了
```

# C语言指针和数组的问题
