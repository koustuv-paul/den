
import java.util.LinkedList;

public class SumOfReverseLinkedList {

	public static void main( String[] args ) {
		SumOfReverseLinkedList obj = new SumOfReverseLinkedList();
		LinkedList<Integer> one = new LinkedList<Integer>();
		one.add( 2 );
		one.add( 4 );
		one.add( 5 );

		LinkedList<Integer> two = new LinkedList<Integer>();
		two.add( 5 );
		two.add( 6 );
		two.add( 4 );

		LinkedList<Integer> sum = obj.sum( one, two );
		System.out.println( sum );
	}

	public LinkedList<Integer> sum( LinkedList<Integer> one, LinkedList<Integer> two ) {
		if ( one == null || two == null ) {
			return null;
		}

		if ( one.size() != two.size() ) {
			return null;
		}

		int count = one.size();
		int index = 0;
		LinkedList<Integer> sum = new LinkedList<Integer>();
		int carry = 0;
		while ( count > 0 ) {
			Integer integer = one.get( index );
			Integer integer2 = two.get( index );
			int add = integer + integer2 + carry;
			index++;
			count--;
			carry = 0;
			if ( add >= 10 ) {
				carry = add / 10;
				add = add % 10;
				sum.add( add );
				continue;
			}
			sum.add( add );
		}
		if ( carry > 0 )
			sum.add( carry );
		return sum;
	}

}
