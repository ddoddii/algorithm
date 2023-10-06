package leetcode;

// 1071. Greatest Common Divisor of Strings
public class p1071 {
    public static String gcdOfStrings(String str1, String str2) {
        int len1 = str1.length();
        int len2 = str2.length();

        int gcd = gcd(len1, len2);

        String substr1 = str1.substring(0,gcd);
        String substr2 = str2.substring(0,gcd);

        int repeat1 = len1 / gcd;
        int repeat2 = len2 / gcd;

        if (str1.equals(repeatString(substr1, repeat1)) && str2.equals(repeatString(substr2, repeat2))){
            if (substr1.equals(substr2)) {
                return substr1;
            }
        }
        return "";

    }

    public static String repeatString(String str , int N){
        StringBuilder result = new StringBuilder();
        for (int i = 0 ; i < N ; i++){
            result.append(str);
        }
        return result.toString();
    }

    public static int gcd(int a, int b){
        while (b!=0){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a ;
    }

    // Solution2

    public static String gcdOfStrings2(String str1, String str2) {
        int len1 = str1.length();
        int len2 = str2.length();
        for (int i = Math.min(len1, len2); i >= 1 ; --i){
            if (isvalid(str1, str2, i)){
                return str1.substring(0,i);
            }
        }
        return "";
    }

    public static boolean isvalid(String str1, String str2, int k){
        int len1 = str1.length();
        int len2 = str2.length();
        if (len1 % k != 0 || len2 % k != 0){
            return false;
        }
        else {
            String base = str1.substring(0,k);
            return str1.replace(base,"").isEmpty() && str2.replace(base, "").isEmpty();
        }

    }
    public static void main(String[] args) {
        String str1 = "ABCDEF";
        String str2 = "ABC";

        System.out.println(gcdOfStrings(str1, str2));
        System.out.println(gcdOfStrings2(str1, str2));



    }
}
