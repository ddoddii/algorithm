package onboarding;

public class problem3 {
    public static void main(String[] args) {
        int number = 103;
        int result = solution(number);
        System.out.println(result);

    }

    static int solution(int number) {
        int count = 0;
        for (int num = 0 ; num < number + 1 ; num++) {
            String num_str = Integer.toString(num);
            count += countClap(num_str);
        }
        return count;
    }

    static int countClap (String num_str) {
        int clap_count = 0;
        for (char digit : num_str.toCharArray()) {
            if (digit == '3' || digit =='6' || digit == '9'){
                clap_count++;
            }
        }
        return clap_count;

    }
}
