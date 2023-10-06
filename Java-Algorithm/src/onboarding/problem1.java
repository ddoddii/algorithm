package onboarding;

import java.util.*;
import java.util.ArrayList;
import java.util.List;

public class problem1 {
    public static void main(String[] args) {
        List<Integer> pobi = new ArrayList<>(Arrays.asList(131,132));
        List<Integer> crong = new ArrayList<>(Arrays.asList(211,212));

        System.out.println(pobi);
        System.out.println(crong);
        int result = solution (pobi, crong);
        System.out.println(result);


    }

    public static int solution(List<Integer> pobi, List<Integer> crong){
        if (!isValid(pobi) || !isValid(crong)){
            return -1;
        }

        int pobi_score = calculate_score(pobi);
        int crong_score = calculate_score(crong);
        if (pobi_score > crong_score) return 1;
        if (crong_score > pobi_score) return 2;
        else {
            return 0;
        }
    }
    static int calculate_score(List<Integer> pages){
        int MaxScore = Integer.MIN_VALUE;

        for (int page : pages) {
            List<Integer> N = new ArrayList<>();
            int temp = page;
            while (temp > 0) {
                N.add(temp % 10);
                temp /= 10;
            }

            int sum = 0;
            int product = 1;
            for (int digit : N) {
                sum += digit;
                product *= digit;
            }
            int pageScore = Math.max(sum, product);
            MaxScore = Math.max(pageScore, MaxScore);

        }

        return MaxScore;

    }

    static boolean isValid(List<Integer> arr){
        if (arr.get(0) % 2 != 1 || (arr.get(1) - arr.get(0)) != 1 || arr.get(1) % 2 != 0){
            return false;
        }
        return true;
    }
}



