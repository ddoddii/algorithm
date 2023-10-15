package leetcode;

import java.util.*;

// 1723. Find the Highest Altitude
public class P1723 {
    public static int largestAltitude(int[] gain) {
        int[] alt = new int[gain.length+1];

        alt[0] = 0;
        for (int i = 1 ; i < alt.length ; i++){
            alt[i] = gain[i-1] + alt[i-1];
        }

        int max = Integer.MIN_VALUE;
        for (int i = 0 ; i< alt.length ; i++){
            if (alt[i] > max){
                max = alt[i];
            }
        }

        return max;
    }

    public static void main(String[] args) {
        int[] gain = {-5,1,5,0,-7};

        System.out.println(largestAltitude(gain));

    }
}
