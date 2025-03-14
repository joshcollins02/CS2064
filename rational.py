""" Defining a Rational number class
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Josh Collins """

class Rational:
    """ The Rational class allows us to implement rational numbers with exact precision, 
    without the approximations/errors used in binary representations """
     
    def __init__(self, iNum, iDen):
        """ Constructs a new Rational object with value iNum/iDen stored in hidden __numerator 
        and __denominator variables. Calls reduce() to put the fraction in lowest terms. """
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()
    
    def getNumerator(self):
        """Gets numerator from constructor"""
        return self.__numerator
    
    def getDenominator(self):
        """Gets denominator from constructor"""
        return self.__denominator
    
    def setNumerator(self, n):
        """Sets numerator as object n"""
        self.__numerator = n
        self.reduce()
            
    def setDenominator(self, d):
        """Sets denominator as object d, checks if denominator is non-zero"""
        self.__denominator = d
        self.reduce()

    def isValid(self):
        """Checks if the fraction is valid for operator functions"""
        if self.getDenominator() != 0:
            return True
        else:
            return False
    
    def reciprocal(self):
        """Returns reciprocal of fraction as long as numerator is non-zero"""
        if self.__numerator == 0:
            raise ValueError('Reciprocal of 0 is undefined')
        # Calls back to numerator and denominator and flips them
        newDen = self.__denominator
        newNum = self.__numerator
        # Assigns back to numerator and denominator
        self.__numerator = newDen
        self.__denominator = newNum
        # Returns gcf
        self.reduce()
        return self
    
    def add(self, num2):
        """Adds a number to the fraction to create a new value"""
        # Calls back to numerator and denominator and adds them with a new num
        newDen = self.getDenominator() * num2.getDenominator()
        newNum = self.getNumerator() * num2.getDenominator() + self.getDenominator() * num2.getNumerator()
        # Assigns back to numerator and denominator
        self.__denominator = newDen
        self.__numerator = newNum
        # Returns gcf
        self.reduce()
  	
    def sub(self, num2):
        """Subtracts a number from the fraction to create a new value"""
        # Calls back to numerator and denominator and subtracts from them with a new num
        newDen = self.getDenominator() * num2.getDenominator()
        newNum = self.getNumerator() * num2.getDenominator() - self.getDenominator() * num2.getNumerator()
        # Assigns back to numerator and denominator
        self.__denominator = newDen
        self.__numerator = newNum
        # Returns gcf
        self.reduce()
             
    def mult(self, num2):
        """Multiplies a number to the fraction to create a new value"""
        # Calls back to numerator and denominator and multiplies them with a new num
        newDen = self.getDenominator() * num2.getDenominator()
        newNum = self.getNumerator() * num2.getNumerator()
        # Assigns back to numerator and denominator
        self.__denominator = newDen
        self.__numerator = newNum
        # Returns gcf
        self.reduce()

    def div(self, num2):
        """Divides a number from the fraction to create a new value"""
        # Checks if the num can be divisible first
        if num2.getNumerator() == 0:
            raise ValueError('Cant divide by 0')
        # Calls back to numerator and denominator and divides them with a new num
        newDen = self.getDenominator() * num2.getNumerator()
        newNum = self.getNumerator() * num2.getDenominator()
        # Assigns back to numerator and denominator
        self.__denominator = newDen
        self.__numerator = newNum
        # Returns gcf
        self.reduce()
    
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################

    def reduce(self):
        """ Reduces the Rational to lowest terms
        - Checks if both the numerator and denominator are negative; if so, makes both positive
        - Calls gcf() to find the greatest common factor between the numerator and denominator, and
            continues to divide by that gcf until the greatest common factor is 1 """
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while common != 1:
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    def gcf(self):
        """ Determines the greatest common factor between the numerator and denominator
        - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
        - When it finds a number divisble by both, it breaks the loop and returns that number
        - The smallest number that can be returned is 1 """
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    def __str__(self):
        """ Returns a string representation of the Rational, e.g. "1/8" """
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    def __eq__(self, r2):
        """ Determines if two Rationals are exactly equal to each other 
        (same numerator and same denominator, no consideration of reducing the numbers) """
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    
    
def main():
    """ This main should only start rationalTest's unit tests.  
    Do NOT implement your tests here.  WebCAT wants them in rationalTest.py """
    import unittest
    unittest.main("rationalTest")

if __name__ == "__main__":
    main()