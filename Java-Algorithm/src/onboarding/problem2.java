package onboarding;

import java.util.*;

public class problem2 {
    public static void main(String[] args) {
        String str = "zyelleyzi";
        String result = solution(str);

        System.out.println(result);

    }

    static String solution(String str) {
        List<Character> result = new ArrayList<>();
        for (int i = 0 ; i < str.length() ; i++) {
            if (i == str.length() -1 || str.charAt(i) != str.charAt(i+1)) {
                result.add(str.charAt(i));
            }
            else {
                i += 1;
            }
        }
        StringBuilder resultStr = new StringBuilder(result.size());
        for (Character c : result) {
            resultStr.append(c);
        }

        if (resultStr.toString().equals(str)){
            return resultStr.toString();
        }
        else{
            return solution(resultStr.toString());
        }
    }


}
