package problems;

import java.util.Scanner;

// 1. 문자 찾기
public class p0101 {
    public static int solution(String input, char ch) {
        int count = 0;
        for (int i = 0 ; i < input.length() ; i++) {
            char currentChar = input.charAt(i);
            if (currentChar == ch) {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input = in.next().toLowerCase();
        char ch = in.next().toLowerCase().charAt(0);

        int answer = solution(input, ch);
        System.out.println(answer);

    }
}
