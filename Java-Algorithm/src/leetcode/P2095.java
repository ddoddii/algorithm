package leetcode;

// 2095. Delete the Middle Node of a Linked List
public class P2095 {
  class solution {

    public ListNode deleteMiddle(ListNode head) {
      if (head == null || head.next == null) {
        return null;
      }
      int length = 0;
      ListNode current = head;
      while (current != null) {
        length++;
        current = current.next;
      }

      int middle = length / 2;

      current = head;
      for (int i = 0 ; i < middle -1 ; i++){
        current = current.next;
      }

      current.next = current.next.next;

      return head;

    }
  }

  public static void main(String[] args) {
    ListNode node3 = new ListNode(4);
    ListNode node2 = new ListNode(3, node3);
    ListNode node1 = new ListNode(2, node2);
    ListNode node0 = new ListNode(1, node1);

    ListNode current = node0;
    while (current != null) {
      System.out.println(current.val);
      current = current.next;
    }

  }
}
