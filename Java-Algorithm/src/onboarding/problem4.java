package onboarding;

import java.util.*;

public class problem4 {
    public static void main(String[] args) {
        String word = "I love you";

        System.out.println(solution(word));

    }
    static String solution(String word){
        StringBuilder result = new StringBuilder();
        for (char ch : word.toCharArray()) {
            if (ch >= 'A' && ch <= 'Z'){
                char flippedLarge = flipLarge(ch);
                result.append(flippedLarge);
            } else if (ch >= 'a' && ch <= 'z'){
                char flippedSmall = flipSmall(ch);
                result.append(flippedSmall);
            } else {
                result.append(' ');
            }
        }
        return result.toString();

    }

    static char flipLarge(char ch){
        char flippedLarge = (char) (155 - (int)ch);
        return flippedLarge;
    }

    static char flipSmall(char ch){
        char flippedSmall = (char) (219 - (int)ch);
        return flippedSmall;
    }

}
