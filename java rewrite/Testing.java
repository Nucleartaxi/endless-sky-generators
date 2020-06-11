import java.util.Random;
public class Testing {
    public static void main(String args[]) {
        Random r = new Random();
        DoublePoint q = new DoublePoint(5, r);
        System.out.println(q);
        System.out.println(q);
        DoublePoint p = new DoublePoint();
        if (q.distanceTo(p) > 5) {
            System.out.println(q.distanceTo(p));
            System.out.println(">5");
        } else if (q.distanceTo(p) < 5) {
            System.out.println(q.distanceTo(p));
            System.out.println("<5");
        } else {
            System.out.println(q.distanceTo(p));
            System.out.println("!");
        }
    }
}