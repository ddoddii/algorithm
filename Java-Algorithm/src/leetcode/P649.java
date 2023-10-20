package leetcode;

import java.util.LinkedList;
import java.util.Queue;

//649. Dota2 Senate
public class P649 {

  public static String predictPartyVictory(String senate) {
    Queue<Integer> dire = new LinkedList<>();
    Queue<Integer> radiant = new LinkedList<>();

    int n = senate.length();

    for (int i = 0; i < n; i++) {
      if (senate.charAt(i) == 'D') {
        dire.add(i);
      } else {
        radiant.add(i);
      }
    }

    while (!radiant.isEmpty() && !dire.isEmpty()) {
      int rIndex = radiant.poll();
      int dIndex = dire.poll();

      if (rIndex > dIndex) {
        dire.add(dIndex + n);
      } else {
        radiant.add(rIndex + n);
      }
    }
    return radiant.isEmpty() ? "Dire" : "Radiant";
  }

  public static void main(String[] args) {
    String senate = "DDRRR";
    System.out.println(predictPartyVictory(senate));
  }
}