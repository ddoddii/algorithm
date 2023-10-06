package problems;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// 단어 뒤집기
public class p0104 {
    public static List<String> solution( String[] words){
        List<String> answer = new ArrayList<>();
        for (String word : words){
            StringBuilder reversed = new StringBuilder(word);
            answer.add(reversed.reverse().toString());
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        String[] words = new String[N];

        for (int i = 0 ; i < N ; i++){
            words[i] = sc.next();
        }

        List<String> answers = solution(words);
        for (String answer : answers){
            System.out.println(answer);
        }


    }
}

