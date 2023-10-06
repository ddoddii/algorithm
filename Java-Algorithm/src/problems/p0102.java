package problems;

import java.util.Scanner;

// 대소문자 변환
public class p0102 {
    public static StringBuilder solution(String input) {
        StringBuilder result = new StringBuilder();

        for (int i = 0 ; i < input.length() ; i++){
            char currentChar = input.charAt(i);
            if (Character.isUpperCase(currentChar)){
                result.append(Character.toLowerCase(currentChar));
            }
            else if (Character.isLowerCase(currentChar)){
                result.append(Character.toUpperCase(currentChar));
            }

        }
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        System.out.println(solution(input));
    }
}
