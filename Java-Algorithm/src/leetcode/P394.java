package leetcode;

import java.util.Stack;


//394. Decode String
public class P394 {
    // sol. Stack
    public static String decodeString(String s) {
        Stack<Integer> numStack = new Stack<>();
        Stack<String> strStack = new Stack<>();

        StringBuilder currentStr = new StringBuilder();
        int idx = 0;

        while (idx < s.length()){
            char c = s.charAt(idx);
            if (Character.isDigit(c)){
                int numStart = idx;
                while(Character.isDigit(s.charAt(idx))) idx++;
                numStack.push(Integer.parseInt(s.substring(numStart,idx)));
            }
            else if (c == '[') {
                strStack.push(currentStr.toString());
                currentStr.setLength(0);
                idx++;
            }
            else if (c == ']') {
                StringBuilder tmp = new StringBuilder(strStack.pop());
                int repeatCount = numStack.pop();
                for (int i = 0 ; i < repeatCount; i++){
                    tmp.append(currentStr);
                }
                currentStr = tmp;
                idx++;
            }
            else{
                currentStr.append(c);
                idx++;
            }

        }
        return(currentStr.toString());
    }



    public static void main(String[] args) {
        String s = "3[a2[c]]";
        System.out.println(decodeString(s));

    }
}
