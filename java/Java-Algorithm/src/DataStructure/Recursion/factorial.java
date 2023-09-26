package DataStructure.Recursion;

public class factorial {
    public static void main(String[] args) {
        int num = 5;
        int result = calculateFactorial(num);


    }
    public static int calculateFactorial(int n){
        if (n==1) return 1;
        return n * calculateFactorial(n-1);
    }
}
