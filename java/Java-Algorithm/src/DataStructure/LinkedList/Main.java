package DataStructure.LinkedList;


public class Main {
    public static void main(String[] args) {
        LinkedList myLinkedList = new LinkedList(4);

        myLinkedList.append(3);
        myLinkedList.append(2);

        myLinkedList.removeLast();

        myLinkedList.prepend(1);

        myLinkedList.removeFirst();

        myLinkedList.printList();
        myLinkedList.getHead();
        myLinkedList.getTail();
        myLinkedList.getLength();
    }
}
