package debugDemoArrayList;

public class DemoArrayList {

    private Coordinate[] elements;
    private int maxUsed;
    public DemoArrayList() {
        elements = new Coordinate[ 10 ];
        maxUsed = -1;
    }

    public int size() {
        return maxUsed + 1;
    }

    public Coordinate get( int index ) {
        if ( index < 0 || index > maxUsed ) {
            throw new IndexOutOfBoundsException();
        }
        return elements[ index ];
    }

    public void set( int index, Coordinate element ) {
        if ( index < 0 || index > maxUsed ) {
            throw new IndexOutOfBoundsException();
        }
        elements[ index ] = element;
    }

    public void add( Coordinate element ) {
        if ( maxUsed  == elements.length ) {
            extend();
        }
        elements[ maxUsed++ ] = element;
    }

    private void extend() {
        Coordinate[] newArray = new Coordinate[ elements.length * 2 ];
        for ( int i = 0; i < elements.length; i++ ) {
            newArray[ i ] = elements[ i ];
        }
        elements = elements.clone();
    }
}

