
import java.util.HashSet;

public class MaxSubstringWithoutRepeat {

	public static void main( String[] args ) {
		MaxSubstringWithoutRepeat obj = new MaxSubstringWithoutRepeat();
		System.out.println( obj.maxSubstringWithoutRepeat( "abcabcdeabcabcdef" ) );//abcdef
	}

	public int maxSubstringWithoutRepeat( String data ) {
		if ( data == null || data.isEmpty() )
			return 0;
		int max = 0;
		int currentMax = 0;

		int size = data.length();
		int index = 0;
		HashSet<Character> uniques = new HashSet<Character>();
		while ( size > 0 ) {
			char charAt = data.charAt( index );
			if ( uniques.contains( charAt ) ) {
				if ( currentMax > max ) {
					max = currentMax;
				}
				uniques.clear();
				currentMax = 0;
				currentMax++;
				uniques.add( charAt );
				index++;
				size--;
				continue;
			}
			uniques.add( charAt );
			currentMax++;
			index++;
			size--;
		}
		return currentMax > max ? currentMax : max;
	}

}
