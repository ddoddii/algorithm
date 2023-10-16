package leetcode;

import java.util.*;

// 1657. Determine if Two Strings Are Close
public class P1657 {
    public static boolean closeStrings(String word1, String word2){
        if (word1.length() != word2.length()) return false;
        Map<Character, Integer> numChars1 = countChars(word1);
        Map<Character, Integer> numChars2 = countChars(word2);

        if(!numChars1.keySet().equals(numChars2.keySet())) return false;

        List<Integer> freq1 = new ArrayList<>(numChars1.values());
        List<Integer> freq2 = new ArrayList<>(numChars2.values());

        Collections.sort(freq1);
        Collections.sort(freq2);

        return freq1.equals(freq2);

    }

    public static Map<Character, Integer> countChars(String word){
        char[] charArr = word.toCharArray();
        Map<Character, Integer> numChars = new HashMap<>();
        for (Character c : charArr) {
            int count = numChars.getOrDefault(c,0);
            numChars.put(c, count+1);
        }
        return numChars;
    }

    public static void main(String[] args) {
        String word1 = "cabbba";
        String word2 = "abbccc";

        System.out.println(closeStrings(word1,word2));

    }
}
