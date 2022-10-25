# 字符语法的常见陷阱

```c++
char c1 = 'yes'; // correct 截断, 有的编译器会只保留第一个字符 有的字符会保留最后一个字符
char c2 = "yes"; // wrong

const char* slash = "/"; // correct
const char* slash2 = '/'; // wrong
```