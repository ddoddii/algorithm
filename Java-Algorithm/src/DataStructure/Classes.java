package DataStructure;


public class Classes {
    public static void main(String[] args) {
        Cookie cookieOne = new Cookie("green");
        Cookie cookieTwo = new Cookie("blue");

        cookieOne.setColor("yellow");

        System.out.println(cookieOne.getColor());

    }

    public static class Cookie {
        private String color;

        public Cookie(String color) {
            this.color = color;
        }

        public String getColor() {
            return color;
        }

        public void setColor(String color) {
            this.color = color;
        }
    }
}


