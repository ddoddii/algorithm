package DataStructure.LinkedList;


public class Main {
    public static void main(String[] args) {
        LinkedList myLinkedList = new LinkedList(1);

        myLinkedList.append(2);
        myLinkedList.append(3);
        myLinkedList.append(4);

        //myLinkedList.removeLast();

        myLinkedList.prepend(0);
        myLinkedList.printList();


        //myLinkedList.removeFirst();

        System.out.println("Index :" + myLinkedList.get(2).value);


        myLinkedList.insert(5,8);


        myLinkedList.remove(5);

        myLinkedList.printList();

        myLinkedList.reverse();
        myLinkedList.printList();



//        myLinkedList.getHead();
//        myLinkedList.getTail();
//        myLinkedList.getLength();
    }
}
