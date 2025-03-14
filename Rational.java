/** Defining a Rational number class
Refer to the instructions on Canvas for more information.
"I have neither given nor received help on this assignment."
author: Josh Collins
*/

public class Rational {
	// These are the instances variables defined for your class.  Don't change these lines!
	private int numerator;
	private int denominator;
	
	/** 
	 * Initialize a new Rational object with value iNum/iDen stored in the numerator and
	 * denominator variables.  Calls the reduce() method to put the fraction in lowest terms.
	 */

//	Constructor that initializes the numerator and denominator
	public Rational(int iNum, int iDen) {
		this.numerator = iNum;
		this.denominator = iDen;		
		this.reduce();
	}

//	Getter for numerator
	public int getNumerator() {
		return this.numerator;
	}

//	Setter for numerator
	public void setNumerator(int n) {
		this.numerator = n;
		this.reduce();
	}

//	Getter for denominator
	public int getDenominator() {
		return this.denominator;
	}

//	Setter for denominator
	public void setDenominator(int d) {
		this.denominator = d;
		this.reduce();
	}

//	Reciprocal method, returns the flip of a rational fraction
	public void reciprocal() {
//		Double-checking the denominator can't be 0
		if (this.numerator == 0) {
			throw new Error("Error, can't have denominator as 0");
		}
//		Creates new var for opposite values, returns reduced form
		int newDen = this.denominator;
		int newNum = this.numerator;
		this.numerator = newDen;
		this.denominator = newNum;
		this.reduce();
	}

//	Checks validity of a fraction
	public boolean isValid() {
		// Instead of always returning true, this method should return false under the right conditions
		if (this.getDenominator() != 0) {
			return true;
		} else {
			return false;
		}
	}

//	Add method, returns rational fraction plus new num
	public void add(Rational num2) {
//		Creates new val for numerator and denominator using basic fraction math
		int newDen = this.getDenominator() * num2.getDenominator();
		int newNum = this.getNumerator() * num2.getDenominator() + this.getDenominator() * num2.getNumerator();
		this.denominator = newDen;
		this.numerator = newNum;
//		Reduces to gcf
		this.reduce();
	}

//	Subtract method, returns rational fraction minus new num
	public void sub(Rational num2) {
//		Creates new val for numerator and denominator using basic fraction math
		int newDen = this.getDenominator() * num2.getDenominator();
		int newNum = this.getNumerator() * num2.getDenominator() - this.getDenominator() * num2.getNumerator();
		this.denominator = newDen;
		this.numerator = newNum;
//		Reduces to gcf
		this.reduce();
	}

//	Multiply method, returns rational fraction times new num
	public void mult(Rational num2) {
//		Creates new val for numerator and denominator using basic fraction math
		int newDen = this.getDenominator() * num2.getDenominator();
		int newNum = this.getNumerator() * num2.getNumerator();
		this.denominator = newDen;
		this.numerator = newNum;
//		Reduces to gcf
		this.reduce();
	}

//	Divide method, returns rational fraction over new num
	public void div(Rational num2) {
//		Checks that numerator can't be 0, or else number DNE
		if (num2.getNumerator() == 0) {
			throw new Error("Can't divide by 0");
		}
//		Creates new val for numerator and denominator using basic fraction math
		int newDen = this.getDenominator() * num2.getNumerator();
		int newNum = this.getNumerator() * num2.getDenominator();
		this.denominator = newDen;
		this.numerator = newNum;
//		Reduces to gcf
		this.reduce();
	}
	
	/*******************************
	*    HELPER FUNCTIONS BELOW    *
	*******************************/
	
	/**
	  Reduces the Rational to lowest terms
        - Checks if both the numerator and denominator are negative; if so, makes both positive
        - Calls gcf() to find the greatest common factor between the numerator and denominator, and
          continues to divide by that gcf until the greatest common factor is 1
	*/
	private void reduce() {
		if ((this.numerator < 0) && (this.denominator < 0)) {
			this.numerator = -this.numerator;
			this.denominator = -this.denominator;
		} //if
		
		int common = 0;
		while (common != 1) {
			common = this.gcf();
			this.numerator /= common;
			this.denominator /= common;
		} //while
		
	} //reduce
	
	/**
      Determines the greatest common factor between the numerator and denominator
        - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
        - When it finds a number divisble by both, it breaks the loop and returns that number
        - The smallest number that can be returned is 1
	*/	
	private int gcf() {
		int commonFactor = 1;
		for (int i = Math.min(Math.abs(this.numerator), Math.abs(this.denominator)); i > 1; i--) {
			if ((this.numerator % i == 0) && (this.denominator % i == 0)) {
				commonFactor = i;
				break;
			} //if
		} //for
		return commonFactor;
	} //gcf
	
	/**
	  Returns a string representation of the Rational, e.g. "1/8"
	*/
	public String toString() {
		return Integer.toString(this.numerator) + "/" + Integer.toString(this.denominator);
	} //toString
	
	/**
	  Determines if two Rationals are exactly equal to each other (same numerator and same 
	  denominator, no consideration of reducing the numbers)
	*/
	public boolean equals(Object other) {
		Rational fraction = (Rational) other;
		if ((this.numerator == fraction.getNumerator()) && this.denominator == fraction.getDenominator()) {
			return true;
		} //if
		return false;
	} //equals
	
	/*******************************
	*     END HELPER FUNCTIONS     *
	*******************************/	
	
	/**
	 * This is the main function.  Running the Rational.java file will run this method. 
	 * No need for changes. It is better to put your testing in RationalTest and running that!
	 */
	public static void main(String[] args) {
		System.out.println("You're running the Rational.java file.");
		System.out.println("If you want to test your program,");
		System.out.println("you should run the RationalTest.java file instead!");
	}
} //Rational (class)