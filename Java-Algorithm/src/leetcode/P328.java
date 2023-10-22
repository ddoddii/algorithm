package leetcode;


import static leetcode.P328.Solution.oddEvenList;

//328. Odd Even Linked List
public class P328 {

  static class Solution {

    public static ListNode oddEvenList(ListNode head) {
      if (head == null || head.next == null) {
        return head;
      }
      ListNode odd = head;
      ListNode even = head.next;
      ListNode evenHead = even;

      while (even != null && even.next != null) {
        odd.next = even.next;
        odd = odd.next;
        even.next = odd.next;
        even = even.next;
      }
      odd.next = evenHead;

      return head;

    }

  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    head.next.next.next = new ListNode(4);
    head.next.next.next.next = new ListNode(5);

    ListNode result = oddEvenList(head);
    ListNode current = result;
    while (current != null) {
      System.out.println(current.val);
      current = current.next;
    }
  }

}
