package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

// 605. Can place flowers
public class p605 {
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int[] newFlowerbed = new int[flowerbed.length + 2];

        newFlowerbed[0] = 0;
        System.arraycopy(flowerbed, 0, newFlowerbed, 1, flowerbed.length);
        newFlowerbed[newFlowerbed.length - 1] = 0;

        List<Integer> splits = new ArrayList<>();
        if (newFlowerbed[1] != 1) {
            splits.add(-1);
        }
        for (int i = 0 ; i < newFlowerbed.length ; i++){
            if (newFlowerbed[i]  == 1 ){
                splits.add(i);
            }
        }
        if (newFlowerbed[newFlowerbed.length -2] != 1){
            splits.add(newFlowerbed.length);
        }
        List<Integer> countZeros = new ArrayList<>();
        for (int i = 0 ; i< splits.size() -1 ; i++){
            countZeros.add(splits.get(i+1) - splits.get(i) -1);
        }

        int count = 0;
        for (int zeros : countZeros){
            count += (zeros-1)/2;
        }

        return count >= n;

    }

    public static boolean canPlaceFlowers2(int[] flowerbed, int n){
        int count = 0;
        for (int i = 0 ; i < flowerbed.length ; i++){
            if (flowerbed[i] == 0){
                boolean emptyLeft = ( i == 0 || flowerbed[i-1] == 0);
                boolean emptyRight = ( i == flowerbed.length -1 || flowerbed[i+1] == 0);

                if (emptyLeft && emptyRight){
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        return count >= n;

    }

    public static void main(String[] args) {
        int[] flowerbed = {1,0,0,0,1};
        int n = 1;
        System.out.println(canPlaceFlowers2(flowerbed,n));

    }

}
