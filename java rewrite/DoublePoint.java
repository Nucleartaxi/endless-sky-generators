import java.awt.Point;
import java.util.Random;
public class DoublePoint {
    double x;
    double y;
    public DoublePoint() { //create a new point at (0, 0)
        setPosition(0, 0);
    }
    public DoublePoint(double x, double y) { //create a new point at the specified position
        setPosition(x, y);
    }
    public DoublePoint(int radius, Random rand) { //create a randomized point within the specified radius, using the distribution in the randomize method
        randomize(radius, rand);
    }
    public double getX() { //returns x
        return x;
    }
    public double getY() { //returns y
        return y;
    }
    public void setPosition(double x, double y) { //sets the position to the specified values
        this.x = x;
        this.y = y;
    }
    public void randomize(int radius, Random rand) { //randomizes the point with the even circular distribution outlined here: https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly/50746409#50746409
        double r = radius * Math.sqrt(rand.nextDouble());
        double theta = rand.nextDouble() * 2 * Math.PI; 
        setPosition(r * Math.cos(theta), r * Math.sin(theta)); //sets the position to the coordinates converted from polar coordinates to cartesian coordinates
    }
    public double distanceTo(DoublePoint p) { //returns the distance between this point and point p
        return Math.sqrt(Math.abs(Math.pow(x - p.getX(), 2) + Math.pow(y - p.getY(), 2)));
    }
    public String toString() { //returns this point as a string in the format (x, y)
        return "(" + x + ", " + y + ")";
    }
}