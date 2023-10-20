package leetcode;

//392. Is Subsequence
public class p392 {

  public static boolean isSubsequence(String s, String t) {
      if (s.isEmpty()) {
          return true;
      }
    char[] charsT = t.toCharArray();
    char[] charsS = s.toCharArray();
    int i = 0;
    int j = 0;
    while (j < charsS.length) {
      while (i < charsT.length) {
        if (charsS[j] == charsT[i]) {
          i++;
          j++;
          if (j == charsS.length) {
            return true;
          }
        } else {
          i++;
        }
      }

      j++;

    }
    return false;

  }

  public static void main(String[] args) {
    String s = "b";
    String t = "abc";
    System.out.println(isSubsequence(s, t));

  }
}
