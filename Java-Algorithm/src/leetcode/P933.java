package leetcode;

import java.util.ArrayList;
import java.util.List;

// 933. Number of Recent Calls
public class P933 {

  public static void main(String[] args) {
    RecentCounter obj = new RecentCounter();
    int param_1 = obj.ping(1);
    int param_2 = obj.ping(100);
    int param_3 = obj.ping(3001);
    int param_4 = obj.ping(3002);
    System.out.println(param_1);
    System.out.println(param_2);
    System.out.println(param_3);
    System.out.println(param_4);

  }
}

class RecentCounter {

  private List<Integer> requestTime;

  public RecentCounter() {
    requestTime = new ArrayList<>();
  }

  public int ping(int t) {
    requestTime.add(t);
    while (!requestTime.isEmpty() && requestTime.get(0) < t - 3000) {
      requestTime.remove(0);
    }
    return requestTime.size();
  }
}
