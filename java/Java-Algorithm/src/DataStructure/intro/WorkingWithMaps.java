package DataStructure.intro;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class WorkingWithMaps {
    public static void main(String[] args) {
        Map<Person, Dog>  map = new HashMap<>();
        map.put(new Person("Soeun",26), new Dog("Surl"));
        System.out.println(map.get(new Person("Soeun", 26).hashCode()));
        System.out.println(map);
        System.out.println(new Person("Soeun",26).hashCode());
        System.out.println(new Person("Soeun",26).hashCode());
    }

    private static void maps() {
        Map<Integer, Person>  map = new HashMap<>();
        map.put(1, new Person("Alex", 20));
        map.put(2, new Person("Soeun", 26));
        map.put(3, new Person("Mary", 24));
        map.put(4, new Person("Marium", 25));

        System.out.println(map.entrySet());
        System.out.println(map.keySet());
        System.out.println(map);

        map.entrySet().forEach(x -> System.out.println(x.getKey() + " " + x.getValue()));

        map.forEach((key,person) -> {
            System.out.println(key + "-" + person);
        });

        System.out.println(map.getOrDefault(5, new Person("newPerson", 100)));

        System.out.println(map.values());


    }


    static class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        @Override
        public String toString() {
            return "Person[name = " + name + ", age = " + age + "]";
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Person person = (Person) o;
            return age == person.age && Objects.equals(name, person.name);
        }
        @Override
        public int hashCode(){
            return Objects.hash(name, age);
        }

    }

    static class Dog {
        private String name;

        public Dog(String name) {
            this.name = name;
        }
        @Override
        public String toString() {
            return "Dog[name = " + name +  "]";
        }

    }

    static class Cat {
        private String name;
        private int age;

        public Cat(String name, int age){
            this.name = name;
            this.age = age;
        }

        @Override
        public String toString() {
            return "Cat{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    '}';
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Cat cat = (Cat) o;
            return age == cat.age && Objects.equals(name, cat.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, age);
        }
    }


}
