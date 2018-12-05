package debugDemoArrayList;

public class Main {

    public static void main( String[] args ) {
        DemoArrayList al = new DemoArrayList();
        for ( int i = 10; i < 100; i++ ) {
            al.add( new Coordinate( i, i * 2 ) );
        }
        System.out.println( "Size: " + al.size() );
        System.out.println( "Last 10: " );
        for (int i = al.size() - 10; i< al.size(); i++){
            System.out.print( al.get( i ).toString() );
        }
    }
}