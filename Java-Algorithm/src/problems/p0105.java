package problems;

import java.util.List;
import java.util.Scanner;

// 특정 문자 뒤집기
// toCharArray 이용
public class p0105 {
    public static String solution(String input){
        char[] charArray = input.toCharArray();
        int left = 0;
        int right = charArray.length -1 ;
        while (left < right) {
            if (!Character.isAlphabetic(charArray[left])) {
                left++;
            }
            else if (!Character.isAlphabetic(charArray[right])) {
                right ++;
            }
            else {
                char temp = charArray[left];
                charArray[left] = charArray[right];
                charArray[right] = temp;
                left++;
                right--;
            }
        }

        return new String(charArray);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String answer = solution(input);
        System.out.println(answer);

    }
}
