package leetcode;

// 443. String Compression
public class p443 {
    public static int compress(char[] chars) {
        if (chars.length == 0) return 0;
        int i = 0;
        int index = 0;

        while( i < chars.length){
            char currentChar = chars[i];
            int count = 0;

            while(i < chars.length && chars[i] == currentChar){
                i++;
                count++;
            }

            chars[index++] = currentChar;

            if (count != 1){
                for (char c : String.valueOf(count).toCharArray()){
                    chars[index++] = c;
                }
            }
        }
        return index;

    }

    public static void main(String[] args) {
        char[] chars = {'a','b','b','b','b','b','b','b','b','b','b','b','b'};
        System.out.println(compress(chars));

    }
}
