package leetcode;

//1768. Merge Strings Alternately
public class p1768 {
    public static String mergeAlternately(String word1, String word2) {
        char[] word1Arr = word1.toCharArray();
        char[] word2Arr = word2.toCharArray();
        StringBuilder answer = new StringBuilder();
        int number = Math.min(word1Arr.length, word2Arr.length);
        for (int i = 0 ; i < number ; i++){
            answer.append(word1Arr[i]);
            answer.append(word2Arr[i]);
        }
        if (word1Arr.length > word2Arr.length){
            String extraPart = word1.substring(word2Arr.length);
            answer.append(extraPart);
        } else{
            String extraPart = word2.substring(word1Arr.length);
            answer.append(extraPart);
        }

        return answer.toString();
    }

    public static String mergeAlternately2(String word1, String word2){
        int m = word1.length();
        int n = word2.length();
        StringBuilder result = new StringBuilder();
        int i = 0, j = 0;

        while (i < m || j < n){
            if (i < m) {
                // i 번째 char 추가하고, i 를 1 증가 (i++)
                result.append(word1.charAt(i++));
            }
            if (j < n){
                result.append(word2.charAt(j++));
            }
        }
        return result.toString();
    }


    public static void main(String[] args) {
        String word1 = "abcd";
        String word2 = "pq";
        System.out.println(mergeAlternately2(word1, word2));
    }

}
