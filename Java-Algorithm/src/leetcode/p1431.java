package leetcode;

import java.util.*;
// 1431. kids with greatest number of candies
public class p1431 {
    public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandy = 0;
        for (int candy : candies ){
            maxCandy = Math.max(candy , maxCandy);
        }

        List<Boolean> result = new ArrayList<>();

        for (int candy : candies){
            result.add(candy + extraCandies >= maxCandy);
        }
        return result;

    }

    public static void main(String[] args) {
        int[] candies = {2,3,5,1,5};
        int extracandies = 3;

        System.out.println(kidsWithCandies(candies, extracandies));

    }


}
