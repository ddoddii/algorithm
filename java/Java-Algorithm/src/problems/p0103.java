package problems;

import java.util.Scanner;

// 3. 문장 속 단어
// 문장 속에서 가장 긴 단어 출력
public class p0103 {
    public static String solution(String input) {
        String[] words = input.split(" ");
        String longestWord = "";

        for(String word : words){
            if (word.length() > longestWord.length() ){
                longestWord = word;
            }
        }
        return longestWord;
    }

    public static String solution2(String input){
        String answer = "";
        int m = Integer.MIN_VALUE, pos;
        while ((pos = input.indexOf(" ")) != -1 ){
            String temp = input.substring(0, pos);
            int len = temp.length();
            if (len > m) {
                m = len;
                answer = temp;
            }
            input = input.substring(pos+1);
        }
        if (input.length() > m) answer = input;
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        System.out.println(solution2(input));
    }

}
