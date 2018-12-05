public class HeapDemo2 {
    public static void main(String[] args){
        Coordinate a = new Coordinate(1,2);
        a.move(20,30);
        System.out.println("a.y is: " + a.y);
    }
}

class Coordinate {
    Coordinate(int newX, int newY){
        x = newX;
        y = newY;
    }
    public int x;
    public int y;

    void move(int x, int y){
        this.x += x;
        this.y += y;
    }
}