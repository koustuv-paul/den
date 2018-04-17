
public class ArrayRotate {

	public boolean rotate( int[] array, int order ) {
		if ( array == null )
			return false;
		if ( order < 0 || order > array.length ) {
			return false;
		}
		if ( order == 0 ) {
			return false;
		}
		int[] temp = new int[order];
		for ( int i = 0; i < array.length; i++ ) {
			if ( i < order ) {
				temp[i] = array[i];
				continue;
			}
			array[( i - ( order ) )] = array[i];
		}
		int j = 0;
		for ( int i = ( array.length - order ); i < array.length; i++ ) {
			array[i] = temp[j++];
		}
		return true;
	}
}
