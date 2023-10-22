package leetcode;


import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

//2130. Maximum Twin Sum of a Linked List
public class P2130 {

  private static int getLength(ListNode head) {
    int length = 0;
    ListNode curr = head;
    while (curr != null) {
      length++;
      curr = curr.next;
    }
    return length;
  }

  //timeout error
  public static int pairSum(ListNode head) {
    int length = getLength(head);

    int maxSum = Integer.MIN_VALUE;

    int middle = length / 2;
    for (int i = 0; i < middle; i++) {
      ListNode curr = head;
      ListNode pairNode = head;

      int pair = length - 1 - i;
      int now = i;
      while (now > 0) {
        curr = curr.next;
        now--;
      }
      while (pair > 0) {
        pairNode = pairNode.next;
        pair--;
      }
      int sum = curr.val + pairNode.val;
      if (sum > maxSum) {
        maxSum = sum;
      }

    }
    return maxSum;
  }

  //sol2. converting singly list into array
  public static int pairSum2(ListNode head){
    List<Integer> listValues = new ArrayList<>();
    while (head != null){
      listValues.add(head.val);
      head = head.next;
    }
    int left = 0 , right = listValues.size() - 1;
    int maxSum = Integer.MIN_VALUE;

    while (left < right){
      int sum = listValues.get(left) + listValues.get(right);
      maxSum = Math.max(sum,maxSum);
      left++;
      right--;
    }
    return maxSum;
  }

  //sol3. using stack (since stack is LIFO -> to access the end of list)
  public static int pairSum3(ListNode head){
    Stack<Integer> stack = new Stack<>();
    ListNode curr = head;
    while (curr != null){
      stack.push(curr.val);
      curr = curr.next;
    }
    int maxSum = Integer.MIN_VALUE;
    int length = stack.size();
    curr = head;
    for (int i = 0 ; i < length/2 ;i++){
      int sum = curr.val + stack.pop();
      maxSum = Math.max(sum,maxSum);

      curr = curr.next;
    }
    return maxSum;
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(6);
    head.next.next.next = new ListNode(4);

    long start = System.currentTimeMillis();
    System.out.println(pairSum(head));
    long end = System.currentTimeMillis();
    System.out.println("pairSum1:"+(end-start));

    long start2 = System.currentTimeMillis();
    System.out.println(pairSum(head));
    long end2 = System.currentTimeMillis();
    System.out.println("pairSum2:"+(end2-start2));

    long start3 = System.currentTimeMillis();
    System.out.println(pairSum(head));
    long end3 = System.currentTimeMillis();
    System.out.println("pairSum3:"+(end3-start3));

    //ArrayList 를 이용한 것이 가장 빨랐다.

  }


}
