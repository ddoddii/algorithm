package leetcode;

//11. Container with most water
public class P11 {

  //sol1. O(n^2)
  public static int maxArea(int[] height) {
    int maxAmount = Integer.MIN_VALUE;
    for (int i = 0; i < height.length - 1; i++) {
      for (int j = 1; j < height.length; j++) {
        int amount = (j - i) * Math.min(height[i], height[j]);
        if (amount > maxAmount) {
          maxAmount = amount;
        }
      }
    }
    return maxAmount;

  }

  //sol2. O(n)
  public static int maxArea2(int[] height) {
    int maxAmount = Integer.MIN_VALUE;
    int i = 0;
    int j = height.length - 1;
    while (i < j) {
      int amount = (j - i) * Math.min(height[i], height[j]);
      if (amount > maxAmount) {
        maxAmount = amount;
      }
      if (height[i] < height[j]) {
        i++;
      } else {
        j--;
      }

    }
    return maxAmount;
  }

  public static void main(String[] args) {
    int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    System.out.println(maxArea2(height));
  }
}
