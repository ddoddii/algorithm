package leetcode;

import java.util.Stack;

//2390. Removing stars from a string
public class P2390 {
    public static String removeStars(String s) {
        Stack<Character> charStack = new Stack<>();
        for (char c : s.toCharArray()){
            if (c == '*'){
                charStack.pop();
            }
            else{
                charStack.push(c);
            }

        }
        StringBuilder sb = new StringBuilder();
        for (char c : charStack){
            sb.append(c);
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "leet**cod*e";
        System.out.println(removeStars(s));

    }
}
