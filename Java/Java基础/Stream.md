# Stream

Stream 就如同一个迭代器（Iterator），单向，不可往复，数据只能遍历一次，遍历过一次后即用尽了，就好比流水从面前流过，一去不复返

```java
class Dish {
    private String name;
    private boolean vegetarian;
    private int calories;
    private Type type;

    public enum Type {MEAT, FISH, OTHER}

    public Dish(String name, boolean vegetarian, int calories, Type type) {
        this.name = name;
        this.vegetarian = vegetarian;
        this.calories = calories;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isVegetarian() {
        return vegetarian;
    }

    public void setVegetarian(boolean vegetarian) {
        this.vegetarian = vegetarian;
    }

    public int getCalories() {
        return calories;
    }

    public void setCalories(int calories) {
        this.calories = calories;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
}

List<Dish> menu = Arrays.asList(
                new Dish("pork", false, 800, Dish.Type.MEAT),
                new Dish("beef", false, 700, Dish.Type.MEAT),
                new Dish("chicken", false, 400, Dish.Type.MEAT),
                new Dish("french fries", true, 530, Dish.Type.OTHER),
                new Dish("rice", true, 350, Dish.Type.OTHER),
                new Dish("season fruit", true, 120, Dish.Type.OTHER),
                new Dish("pizza", true, 550, Dish.Type.OTHER),
                new Dish("prawns", false, 300, Dish.Type.FISH),
                new Dish("salmon", false, 450, Dish.Type.FISH)
        );
```

## 过滤

```java
List<Dish> healthyMenu = menu.stream().filter(Dish::isVegetarian).collect(Collectors.toList());

        // limit 流支持limit(n)方法，该方法会返回一个不超过给定长度的流。所需的长度作为参数传递 给limit
        List<Dish> vegatarianMenu = menu.stream().filter(Dish::isVegetarian).limit(3).collect(Collectors.toList());

        // distinct 流还支持一个叫作distinct的方法，它会返回一个元素各异（根据流所生成元素的 hashCode和equals方法实现）的流
        List<Integer> numbers = Arrays.asList(1, 2, 1, 3, 3, 2, 4);
        numbers.stream().filter(integer -> integer % 2 == 0).distinct().forEach(System.out::println);

        // skip 流还支持skip(n)方法，返回一个扔掉了前n个元素的流。如果流中元素不足n个，则返回一个空流
        List<Dish> vegatarianMenu = menu.stream().filter(Dish::isVegetarian).skip(2).collect(Collectors.toList());
```

## 映射
```java
List<String> dishNames = menu.stream().map(Dish::getName).collect(Collectors.toList());
```

## 匹配查找
```java
// anyMatch
if (vegatarianMenu.stream().anyMatch(Dish::isVegetarian)){
    System.out.printf("The menu is (somewhat) vegetarian friendly!!");
}

// allMatch
boolean flag = vegatarianMenu.stream().allMatch(dish -> dish.getCalories() <1000);
System.out.println(flag);

//findAny方法将返回当前流中的任意元素。它可以与其他流操作结合使用。方法返回结果为 Optional<T>。
vegatarianMenu.stream().filter(Dish::isVegetarian).findAny().ifPresent(d -> System.out.println(d.getName()));
```

## 划归 Reduce
```java
//Type 1
int result = list.stream().reduce(0, Integer::sum);
System.out.println(result);

//Type 2
list.stream().reduce(Integer::sum).ifPresent(System.out::println);
```