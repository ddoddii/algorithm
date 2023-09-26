


public class Main {
    public static void main(String[] args) {
        String str = "ABC  abc";
        char[] CharList = str.toCharArray();
        for (int i = 0 ; i < CharList.length ; i++){
            int asciiValue = CharList[i];
            System.out.println(asciiValue);
        }

    }
}