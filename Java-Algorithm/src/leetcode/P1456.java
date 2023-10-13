package leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

// 1456. Maximum number of vowels in a substring of a given length
public class P1456 {
    public static int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a','e','i','o','u'));
        char[] strArr = s.toCharArray();
        int count = 0;

        for (int i = 0 ; i < k ; i++){
            if (vowels.contains(strArr[i])){
                count++;
            }
        }

        int maxCount = count;

        for (int i = k ; i < strArr.length ; i++){
            if (vowels.contains(strArr[i-k])){
                count--;
            }
            if (vowels.contains(strArr[i])){
                count++;
            }
            if (count > maxCount) {
                maxCount = count;
            }
        }

        return maxCount;


    }

    public static void main(String[] args) {
        String s = "abciiidef";
        int k = 3;
        System.out.println(maxVowels(s,k));
    }
}
