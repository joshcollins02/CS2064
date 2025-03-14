import static org.junit.Assert.*;
import org.junit.Assert;
import org.junit.Test;

/** The RationalTest unit test class.  
Refer to the instructions on Canvas for more information.
"I have neither given nor received help on this assignment."
author: Josh Collins
 */

// Note: If you see problems, red underlines, or have trouble running this file: 
// You need to add the 'JUnit 4' library to your project.  Look at the 
// 'Package Explorer' view on the left.  Right click your project there. 
// Find 'Build Path' -> 'Add Libraries'.  Then select JUnit 4.  Now you are good!

// Once you have JUnit 4, running this file should show a 'JUnit' view on the left. 
// That view should say "Runs: 3/3  Errors:0  Failures:0" and have a green bar.  
// You can also expand out the 'RationalTest' folder there to see each test result

public class RationalTest {
//	Given test for rational number
	@Test
	public void testRational() {
		Rational r = null;
		assertNull(r);
		r = new Rational(3, 5);
		assertNotNull(r);
		// ^^^ Shows you how JUnit does null assertions
	}

//	Given test for conversion to string
	@Test
	public void testToString() {
		Rational r = new Rational(4, 7);
		String s = r.toString();
		assertEquals("4/7", s);
		int variFive = 2+3;
		assertEquals(5, variFive);
		// ^^^ To show you how JUnit does equals assertions.  
		// You should be doing something similar on your tests below!
	}

//	Tests getter method returns numerator
	@Test
	public void testGetNumerator() {
//		Creates rational and calls getNumerator method
		assertEquals(1, new Rational(1,2).getNumerator());
		assertEquals(0, new Rational(0,2).getNumerator());
		assertEquals(5, new Rational(10,2).getNumerator());
	}

//	Tests getter method returns denominator
	@Test
	public void testGetDenominator() {
//		Creates rational and calls getDenominator method
		assertEquals(2, new Rational(1,2).getDenominator());
		assertEquals(20, new Rational(1,20).getDenominator());
		assertEquals(3, new Rational(5,3).getDenominator());
	}

//	Tests reciprocal method returns flipped frac
	@Test
	public void testReciprocal() {
//		Creates rational and calls reciprocal method
		Rational r1 = new Rational(3, 4);
		r1.reciprocal();
		assertEquals(4, r1.getNumerator());
		assertEquals(3, r1.getDenominator());

		Rational r2 = new Rational(1, 2);
		r2.reciprocal();
		assertEquals(2, r2.getNumerator());
		assertEquals(1, r2.getDenominator());

		Rational r3 = new Rational(1,5);
		r3.reciprocal();
		assertEquals(5, r3.getNumerator());
		assertEquals(1, r3.getDenominator());
	}

//	Tests add method returns sum of two values
	@Test
	public void testAdd() {
//		Creates rational and calls add method
		Rational r1 = new Rational(1,5);
		Rational r2 = new Rational(1,3);
		r1.add(r2);
		assertEquals(8, r1.getNumerator());
		assertEquals(15, r1.getDenominator());

		Rational r3 = new Rational(-1, 4);
		r1 = new Rational(1, 5);
		r1.add(r3);
		assertEquals(-1, r1.getNumerator());
		assertEquals(20, r1.getDenominator());

		Rational r4 = new Rational(-1, 3);
		Rational r5 = new Rational(-1, 6);
		r4.add(r5);
		assertEquals(-1, r4.getNumerator());
		assertEquals(2, r4.getDenominator());
	}

//	Tests sub method returns difference of two values
	@Test
	public void testSub() {
//		Creates rational and calls sub method
		Rational r1 = new Rational(1,5);
		Rational r2 = new Rational(1,3);
		r1.sub(r2);
		assertEquals(-2, r1.getNumerator());
		assertEquals(15, r1.getDenominator());

		Rational r3 = new Rational(-1, 4);
		r1 = new Rational(1, 5);
		r1.sub(r3);
		assertEquals(9, r1.getNumerator());
		assertEquals(20, r1.getDenominator());

		Rational r4 = new Rational(-1, 3);
		Rational r5 = new Rational(-1, 6);
		r4.sub(r5);
		assertEquals(-1, r4.getNumerator());
		assertEquals(6, r4.getDenominator());
	}

//	Tests mult method returns product of two values
	@Test
	public void testMult() {
//		Creates rational and calls mult method
		Rational r1 = new Rational(1,5);
		Rational r2 = new Rational(1,3);
		r1.mult(r2);
		assertEquals(1, r1.getNumerator());
		assertEquals(15, r1.getDenominator());

		Rational r3 = new Rational(-1, 4);
		r1 = new Rational(1, 5);
		r1.sub(r3);
		assertEquals(9, r1.getNumerator());
		assertEquals(20, r1.getDenominator());

		Rational r4 = new Rational(-1, 3);
		Rational r5 = new Rational(-1, 6);
		r4.sub(r5);
		assertEquals(-1, r4.getNumerator());
		assertEquals(6, r4.getDenominator());
	}

//	Tests div method returns quotient of two values
	@Test
	public void testDiv() {
//		Creates rational and calls div method
		Rational r1 = new Rational(1,5);
		Rational r2 = new Rational(1,3);
		r1.div(r2);
		assertEquals(3, r1.getNumerator());
		assertEquals(5, r1.getDenominator());

		Rational r3 = new Rational(-1, 4);
		r1 = new Rational(1, 5);
		r1.sub(r3);
		assertEquals(9, r1.getNumerator());
		assertEquals(20, r1.getDenominator());

		Rational r4 = new Rational(-1, 3);
		Rational r5 = new Rational(-1, 6);
		r4.sub(r5);
		assertEquals(-1, r4.getNumerator());
		assertEquals(6, r4.getDenominator());
	}
}