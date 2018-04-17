
import org.junit.Assert;
import org.junit.Test;

import com.self.quotes.ArrayRotate;

public class ArrayRotateTest {

	private ArrayRotate testObj = new ArrayRotate();

	@Test
	public void testNull() {
		int[] sample = null;
		Assert.assertFalse( testObj.rotate( sample, 2 ) );
	}

	@Test
	public void testNegativeRotateOrder() {
		int[] sample = new int[] { 1, 2, 3, 4, 5, 6 };
		Assert.assertFalse( testObj.rotate( sample, -2 ) );
	}

	@Test
	public void testLargerThanArrayRotateOrder() {
		int[] sample = new int[] { 1, 2, 3, 4, 5, 6 };
		Assert.assertFalse( testObj.rotate( sample, 7 ) );
	}

	@Test
	public void testRotateByN() {
		int[] sample = new int[] { 1, 2, 3, 4, 5, 6 };
		int[] result = new int[] { 3, 4, 5, 6, 1, 2 };
		Assert.assertTrue( testObj.rotate( sample, 2 ) );
		Assert.assertArrayEquals( result, sample );
	}

	@Test
	public void testRotateByArraySize() {
		int[] sample = new int[] { 1, 2, 3, 4, 5, 6 };
		int[] result = new int[] { 1, 2, 3, 4, 5, 6 };
		Assert.assertTrue( testObj.rotate( sample, sample.length ) );
		Assert.assertArrayEquals( result, sample );
	}

	@Test
	public void testRotateByArraySizeMinus1() {
		int[] sample = new int[] { 1, 2, 3, 4, 5, 6 };
		int[] result = new int[] { 6, 1, 2, 3, 4, 5 };
		Assert.assertTrue( testObj.rotate( sample, sample.length - 1 ) );
		Assert.assertArrayEquals( result, sample );
	}
}
