package DataStructure.intro;

import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;

public class WorkingWithQueues {
    public static void main(String[] args) {
        LinkedList<Person> linkedlist = new LinkedList<>();
        linkedlist.add(new Person("Soeun", 26));
        linkedlist.add(new Person("Alex", 21));
        linkedlist.addFirst(new Person("ali", 18));
        ListIterator<Person> personListIterator= linkedlist.listIterator();

        while(personListIterator.hasNext()) {
            System.out.println(personListIterator.next());
        }

        while(personListIterator.hasPrevious()) {
            System.out.println(personListIterator.previous());
        }

    }

    public static void queues() {
        Queue<Person> supermarket = new LinkedList<>();

        supermarket.add(new Person("Soeun", 26));
        supermarket.add(new Person( "Alex", 20));

        System.out.println(supermarket.peek().name);
        System.out.println(supermarket.poll().name);
        System.out.println(supermarket.size());
        System.out.println(supermarket.peek().name);
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
     }
}
