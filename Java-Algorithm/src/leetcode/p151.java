package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

// 151. Reverse word in string
public class p151 {
    public static String reverseWords(String s) {
        s = s.trim();
        String[] words = s.split("\\s+");
        List<String> wordList = new ArrayList<>(Arrays.asList(words));
        Collections.reverse(wordList);
        return String.join(" ", wordList);


    }

    public static void main(String[] args) {
        String s = "   the sky    is blue";
        System.out.println(reverseWords(s));
    }
}
