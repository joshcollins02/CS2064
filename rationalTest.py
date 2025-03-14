""" Tests for the Rational class in rational.py
@author: Josh Collins """

import unittest
from rational import Rational

class TestRational(unittest.TestCase):
    
    def testNumerator1(self):
        """Test to return correct numerator"""
        self.assertEqual(Rational(1, 2).getNumerator(), 1)
        self.assertEqual(Rational(0, 2).getNumerator(), 0)
        self.assertEqual(Rational(5, 2).getNumerator(), 5)
        
    def testDenominator1(self):
        """Test to return correct denominator"""
        self.assertEqual(Rational(1, 2).getDenominator(), 2)
        self.assertEqual(Rational(5, 11).getDenominator(), 11)
        self.assertEqual(Rational(12, 12).getDenominator(), 1)
        
    def testNumerator2(self):
        """Test to return correct numerator using helper funcs to get gcf"""
        self.assertEqual(Rational(10, 5).getNumerator(), 2)
        self.assertEqual(Rational(1, 5).getNumerator(), 1)
        self.assertEqual(Rational(0, 5).getNumerator(), 0)

    def testDenominator2(self):
        """Test to return correct denominator using helper funcs to get gcf"""
        self.assertEqual(Rational(10, 5).getDenominator(), 1)
        self.assertEqual(Rational(1, 5).getDenominator(), 5)
        self.assertEqual(Rational(12, 2).getDenominator(), 1)

    def testReciprocal(self):
        """Test to return correct reciprocal"""
        self.assertEqual(Rational(1, 2).reciprocal().getNumerator(), 2)
        self.assertEqual(Rational(1, 2).reciprocal().getDenominator(), 1)
        self.assertEqual(Rational(5, 2).reciprocal().getDenominator(), 5)

    def testAdd(self):
        """Test to return a sum of fraction and num2"""
        r1 = Rational(1, 4)
        r2 = Rational(1, -8)
        r1.add(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 8)

        r1 = Rational(2, 5)
        r2 = Rational(1, 5)
        r1.add(r2)
        self.assertEqual(r1.getNumerator(), 3)
        self.assertEqual(r1.getDenominator(), 5)

        r1 = Rational(1, 4)
        r2 = Rational(1, 4)
        r1.add(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 2)

        r1 = Rational(1, 4)
        r2 = Rational(1, 8)
        r1.add(r2)
        self.assertEqual(r1.getNumerator(), 3)
        self.assertEqual(r1.getDenominator(), 8)

    def testSub(self):
        """Test to return a difference of fraction and num2"""
        r1 = Rational(3, 2)
        r2 = Rational(1, 2)
        r1.sub(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 1)

        r1 = Rational(2, 5)
        r2 = Rational(1, 5)
        r1.sub(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 5)

        r1 = Rational(1, 4)
        r2 = Rational(1, 8)
        r1.sub(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 8)

        r1 = Rational(1, 10)
        r2 = Rational(2, 10)
        r1.sub(r2)
        self.assertEqual(r1.getNumerator(), -1)
        self.assertEqual(r1.getDenominator(), 10)

    def testMult(self):
        """Test to return a product of fraction and num2"""
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r1.mult(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 4)

        r1 = Rational(2, 5)
        r2 = Rational(1, 5)
        r1.mult(r2)
        self.assertEqual(r1.getNumerator(), 2)
        self.assertEqual(r1.getDenominator(), 25)

        r1 = Rational(1, 4)
        r2 = Rational(1, 4)
        r1.mult(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 16)

        r1 = Rational(1, 4)
        r2 = Rational(1, 8)
        r1.mult(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 32)
    
    def testDiv(self):
        """Test to return a quotient of fraction and num2"""
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r1.div(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 1)

        r1 = Rational(2, 5)
        r2 = Rational(1, 5)
        r1.div(r2)
        self.assertEqual(r1.getNumerator(), 2)
        self.assertEqual(r1.getDenominator(), 1)

        r1 = Rational(1, 4)
        r2 = Rational(1, 4)
        r1.div(r2)
        self.assertEqual(r1.getNumerator(), 1)
        self.assertEqual(r1.getDenominator(), 1)

        r1 = Rational(1, 4)
        r2 = Rational(1, 8)
        r1.div(r2)
        self.assertEqual(r1.getNumerator(), 2)
        self.assertEqual(r1.getDenominator(), 1)

        # Checks for divisibility based on function
        with self.assertRaises(ValueError):
            r1 = Rational(1, 2)
            r2 = Rational(0, 1)
            r1.div(r2)

if __name__ == '__main__':
    unittest.main() 