# Maven常用
## 下载、安装与配置
### 下载
Maven 下载地址 http://maven.apache.org/download.cgi
注意下载二进制文件, 解压就可以直接使用

### 安装
1. 解压到不含中文和空格的目录中
2. 配置环境变量
`M2_HOME=解压目录/apache-maven-X
export PATH=PATH:PATH:M2_HOME/bin`
安装完成之后，在命令行执行命令：mvn -v，如果打印类似如下版本信息，则说明安装成功。
    ```shell
    ➜  mvn -v
    Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00)
    Maven home: /apache-maven-3.5.0
    Java version: 1.8.0_131, vendor: Oracle Corporation
    Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre
    Default locale: zh_CN, platform encoding: UTF-8
    ```
### 配置
Maven 的配置文件位于 conf 目录中, 配置文件名称是：settings.xml.
通常, 不需要做任何的修改, 使用默认配置即可正常工作.
这里只需要关注本地仓库（Maven 下载下来的 jar 包的存储路径）的路径即可
```xml
<!-- localRepository
 | The path to the local repository maven will use to store artifacts.
 | 默认的本地仓库路径是 home 下的 .m2/repository
 | Default: ${user.home}/.m2/repository
<localRepository>/path/to/local/repo</localRepository>
-->
```
Maven 项目工程目录约定
通常, 我们会看到如下所示的 Maven 工程结构
```
$ MavenProject
|-- pom.xml
|-- src
|   |-- main
|   |   `-- java
|   |   `-- resources
|   `-- test
|   |   `-- java
|   |   `-- resources
`-- README.md
```

它们的含义如下
- src/main/java：项目的源代码所在的目录
- src/main/resources：项目的资源文件所在的目录
- src/test/java：测试代码所在的目录
- src/test/resources：测试相关的资源文件所在的目录
- 项目的说明文件


常用的 Maven 命令
|   格式  |   含义    |   备注    |
|:-------|-------|----------|
|mvn compile    |   编译源代码  |   这个过程会伴随着下载工程的所有依赖 jar 包   |
|mvn clean  |   清理环境    |   清理 target 目录    |
|mvn test   |   执行测试用例    |	
|mvn install    |   安装项目到本地仓库  |
|mvn dependency:tree    |   显示maven依赖树 |   通常用户排查依赖问题    |
|mvn dependency:list    |   显示maven依赖列表   |   通常用户排查依赖问题    |
