package DataStructure.intro;

import java.util.Objects;
import java.util.Set;
import java.util.HashSet;

public class WorkingWithSets {
    public static void main(String[] args) {
        Set<Ball> balls = new HashSet<>();
        balls.add(new Ball("blue"));
        balls.add(new Ball("yellow"));
        balls.add(new Ball("red"));
        balls.remove(new Ball("red"));


        balls.forEach(System.out::println);
    }

    static class Ball{
        private String color;

        public Ball(String color){
            this.color = color;
        }
        @Override
        public int hashCode() {
            return Objects.hash(color);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            } else if (!(obj instanceof Ball)) {
                return false;
            } else {
                Ball other = (Ball) obj;
                return Objects.equals(color, other.color);

            }
        }
        @Override
        public String toString() {
            return "Ball[color = " + color + "]";
        }

    }
}
