"""
Functions about calendars
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Josh Collins
"""

def gregorian(year):
    # Here is where you will write your function to determine
    # if a year is a Gregorian leap year
    '''Returns True or False depending on if the year is divisible by conditions returning a leap year based on Gregorian's year'''
    # The year is divisible by 4, then it's a leap year
    if year % 4 != 0:
        return False
    # The year is divisible by 100, then it's not a leap year
    elif year % 100 != 0:
        return True
    # The year is divisible by 400, then it's a leap year
    elif year % 400 != 0:
        return False
    else:
        return True

def milankovic(year):
    # Here is where you will write your function to determine
    # if a year is a Milankovic leap year
    '''Returns True or False depending on if the year is divisible by conditions returning a leap year based on Milankovic's year'''
    # The year is divisible by 4, then it's a leap year
    if year % 4 != 0:
        return False
    # The year is divisible by 100, then it's not a leap year
    elif year % 100 != 0:
        return True
    # The year is divisible by 900 with a remainder of 200 or 600, then it's a leap year
    elif year % 900 == 200 or year % 900 == 600:
        return True
    else:
        return False

def gregorian_count(year1, year2):
    # Here is where you will write your function to determine
    # the number of leap years that lie between two dates on
    # the Gregorian calendar
    '''Returns the number of leap years between year1 and year2 calling from gregorian func'''
    count = 0
    for year in range(year1, year2):
        if gregorian(year):
            count += 1
    return count
        
def milankovic_count(year1, year2):
    # Here is where you will write your function to determine
    # the number of leap years that lie between two dates on
    # the Milankovic calendar
    '''Returns the number of leap years between year1 and year2 calling from milankovic func'''
    count = 0
    for year in range(year1, year2):
        if milankovic(year):
            count += 1
    return count

def fromMiddle(age, year):
    '''Here is where you calculate from a Middle Earth age and year into a 
    modern year'''
    # This might be helpful...
    # Length of each age
    ageLengths = [0, 590, 3441, 3021, 2000, 2000, 2000]
    # Calculate the years in Middle Earth
    t_year = sum(ageLengths[:age]) + year - 1
    # Convert to modern year
    m_year = t_year - 11080
    return m_year

def toMiddle(year):
    '''Here is where you calculate from a modern year into a Middle Earth age 
    and year; Note that it should return a tuple of two integers'''
    # This might be helpful...
    # Length of each age
    ageLengths = [0, 590, 3441, 3021, 2000, 2000, 2000]
    # Convert to Middle Earth year
    t_year = year + 11081
    # Initializing
    age = 1
    # Looping through the ages
    while age < len(ageLengths) and t_year > ageLengths[age]:
        t_year -= ageLengths[age]
        age += 1
    # Handles change in age if == 2000
    if t_year == 2000:
        t_year = 0
        age = age + 1
    return age, t_year

def main():
    # Here is where you can prototype and run some code...
    # Webcat will ignore what's here
    print(gregorian(1696))
    print(gregorian(1697))
    print(gregorian(2100))
    print(gregorian(2800))

    print(milankovic(1696))
    print(milankovic(1697))
    print(milankovic(2100))
    print(milankovic(2800))

    print(gregorian_count(1696,1697))
    print(gregorian_count(1900,1901))
    print(gregorian_count(2000,3000))
    print(gregorian_count(2000,2850))

    print(milankovic_count(1696,1697))
    print(milankovic_count(1900,1901))
    print(milankovic_count(2000,3000))
    print(milankovic_count(2000,2850))
    
    print(fromMiddle(7,0))
    print(fromMiddle(6,1999))
    print(fromMiddle(3,2941))
    print(fromMiddle(5,1999))

    print(toMiddle(1971))
    print(toMiddle(1970))
    print(toMiddle(0))
    print(toMiddle(-11000))
    print(toMiddle(-2029))

###############################################################

# Here is where you will write your testing code
import unittest

class TestCalendars(unittest.TestCase):    
    # Tests should FAIL when there is a bug in your code! 
    # Verify this yourself, by adding a bug up above and re-running.  
    # If nothing fails, your tests are doing a bad job...
    # Also double check that the number of tests matches what is printed/run
    # Right now, running the file should output 'Ran 3 tests in 0.0s'  
        
    def testGregorian1(self):
        # This comment should explain what is being tested, and how
        '''Tests the gregorian func to return the correct values based on rules of func'''
        self.assertTrue(gregorian(2020))
        self.assertTrue(gregorian(1600))
        self.assertTrue(gregorian(4))
        self.assertFalse(gregorian(2011))
        self.assertFalse(gregorian(1))
        self.assertFalse(gregorian(1111))
    
    def testMilankovic(self):
        # This comment should explain what is being tested, and how
        '''Tests the milankovic func to return the correct values based on rules of func'''
        self.assertTrue(milankovic(1696))
        self.assertTrue(milankovic(1880))
        self.assertTrue(milankovic(2000))
        self.assertFalse(milankovic(1697))
        self.assertFalse(milankovic(1701))
        self.assertFalse(milankovic(2800))

    def testfromMiddle(self):
        # This comment should explain what is being tested, and how
        '''Tests the fromMiddle func to return the correct values based on rules of func'''
        assert fromMiddle(7,0) == 1971
        assert fromMiddle(6,1999) == 1970
        assert fromMiddle(3,2941) == -4109

    def testtoMiddle(self):
        '''Tests the fromMiddle func to return the correct values based on rules of func'''
        assert toMiddle(1971) == (7,0)
        assert toMiddle(1970) == (6,1999)
        assert toMiddle(0) == (6,29)

# ... repeat for all functions, testing throughly for several different 
# inputs producing expected outputs ...
    
    
###############################################################    
    
if __name__ == "__main__":
    main() # needed to actually run the main method
    unittest.main() # finds and runs any test methods in our TestCase classes