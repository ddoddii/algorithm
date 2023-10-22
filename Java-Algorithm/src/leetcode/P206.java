package leetcode;

// 206. Reverse Linked List
public class P206 {

  public static ListNode reverseList(ListNode head) {
    if (head == null) {
      return head;
    }
    ListNode curr = head;
    ListNode after = head.next;
    ListNode before = null;

    while (curr != null) {
      after = curr.next;
      curr.next = before;
      before = curr;
      curr = after;
    }

    return before;

  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    head.next.next.next = new ListNode(4);
    head.next.next.next.next = new ListNode(5);

    ListNode result = reverseList(head);
    ListNode curr = result;
    while (curr != null) {
      System.out.println(curr.val);
      curr = curr.next;
    }
  }

}
