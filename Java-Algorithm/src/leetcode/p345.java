package leetcode;

import java.util.*;

// 345. Reverse Vowels of a String
public class p345 {
    public static String reverseVowels(String s) {
        String[] strArr = s.split("");
        ArrayList<String> strlist = new ArrayList<>(Arrays.asList(strArr));
        List<String> vowels = Arrays.asList("A","E","I","O","U","a","e","i","o","u");

        List<String> reversedVowels = new ArrayList<>();
        List<Integer> vowelIdx = new ArrayList<>();

        for (int i = 0 ; i < strlist.size(); i++){
            if (vowels.contains(strlist.get(i))) {
                reversedVowels.add(strlist.get(i));
                vowelIdx.add(i);
            }
        }

        Collections.reverse(reversedVowels);

        for (int i = 0; i < reversedVowels.size() ; i++){
            int position = vowelIdx.get(i);
            strlist.set(position, reversedVowels.get(i));
        }

        StringBuilder result = new StringBuilder();
        for (String str : strlist){
            result.append(str);
        }

        return (result.toString());

    }

    //solution2 . Two Pointers
    public String reverseVowels2(String s){
        int left = 0;
        int right = s.length() - 1;
        List<String> vowels = Arrays.asList("A","E","I","O","U","a","e","i","o","u");
        char[] sChar = s.toCharArray();

        while (left < right){
            while (left < s.length() && !isVowel(sChar[left])){
                left++;
            }
            while (right >= 0 && !isVowel(sChar[right])){
                right--;
            }
            if (left < right){
                swap(sChar, left, right);
            }
        }

        return new String(sChar);

    }

    void swap(char[] chars , int x , int y){
        char temp = chars[x];
        chars[x] = chars[y];
        chars[y] = temp;
    }

    boolean isVowel(char c ){
        return c == 'a' || c == 'i' || c == 'e' || c == 'o' || c == 'u'
                || c == 'A' || c == 'I' || c == 'E' || c == 'O' || c == 'U';
    }


    public static void main(String[] args) {
        String s = "Aa";
        System.out.println(reverseVowels(s));


    }
}
