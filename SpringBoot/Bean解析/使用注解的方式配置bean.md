# 使用注解的方式配置bean

## `@Component`声明
```java
@Component
public class Animal {
    private String name;
    private String type;

    //...
}
```

## 配置类中使用`@Bean`
```java
public class Animal {
    private String name;
    private String type;

    //...
}

@Configuration
public class AnimalConfiguration {

    @Bean
    public Animal getAnimal() {
        return new Animal();
    }
}

@Service
class HelloService{

    @Autowired
    private Animal animal;

    //...
}

```

## 实现`FactoryBean`
```java
@Component
public class MyAnimal implements FactoryBean<Animal> {

    @Override
    pubic Animal getObject() throws Exceptino {
        return new Animal();
    }

    @Override
    public Class<?> getObjectType() {
        return Animal.class;
    }
}

@Service
class HelloService{

    @Autowired
    private Animal animal;

    //...
}
```

## 实现`BeanDefinitionRegistryPostProcessor`
```java
@Component
public class MyUserRegister implements BeanDefinitionRegistryPostProcessor {

    @Override
    public void postProcessBeanDefinitionRegistry(BeanDefinitionRegistry beanDefinitionRegistry) throws BeansException {
        RootBeanDefinition rootBeanDefinition = new RootBeanDefinition();
        rootBeanDefinition.setBeanClass(User.class);
        beanDefinitionRegistry.registerBeanDefinition("User", rootBeanDefinition);
    }

    @Override
    public void postProcessBeanFactory(ConfigurableListableBeanFactory configurableListableBeanFactory) throws BeansException {

    }
}

@Service
public class HelloService {

    @Autowired
    private User user;

    void sayHello() {
        System.out.println(user);
    }
}

```

## 实现`ImportBeanDefinitionRegistrar`
```java
public class MyBeanImport implements ImportBeanDefinitionRegistrar {
    
    @Override
    public void registerBeanDefinitions(AnnotationMetaData importingClassMetaData, BeanDefinitionRegistory registry) {
        RootBeanDefinition rootBeanDefinition = new RootBeanDefinition();
        rootBeanDefinition.setBeanClass(User.class);
        registry.registerBeanDefinition("User", rootBeanDefinition);
    }
}
```