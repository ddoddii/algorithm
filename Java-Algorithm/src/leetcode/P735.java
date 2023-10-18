package leetcode;

import java.util.Stack;

//735. Asteroid Collision
public class P735 {
    public static int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int ast : asteroids){
            if (ast > 0){
                stack.push(ast);
            }
            else{
                while(!stack.isEmpty() && stack.peek() > 0 && stack.peek() < Math.abs(ast) ){
                    stack.pop();
                }
                if (stack.isEmpty() || stack.peek() < 0){
                    stack.push(ast);
                }
                else if (stack.peek() == Math.abs(ast)){
                    stack.pop();
                }

            }
        }
        int[] result = new int[stack.size()];
        for (int i = result.length - 1 ; i >= 0 ; i--){
            result[i] = stack.pop();
        }

        return result;


    }

    public static void main(String[] args) {
        int[] asteroids = {-2,-1,2,1};
        int[] result = asteroidCollision(asteroids);
        for (int num : result){
            System.out.println(num);
        }


    }

}
