public class PointTest {
    public static void main(String[] args) {
        Point3D p3 = new Point3D (1,2,3);
        String str = p3.getLocation();
        System.out.println(str);
    }
}

class Point{
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    String getLocation(){
        return ("x: "+ x + " y: " +y);
    }

}

class Point3D extends Point{
    int z;

    public Point3D(int x, int y, int z) {
        super(x,y);
        this.z = z;
    }

    @Override
    String getLocation(){
        return ("x: "+ x + " y: " + y + " z: "+ z);
    }
}