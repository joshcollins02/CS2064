"""Practice with writing test cases and performing test-driven development using a
Guess-My-Number game as a problem statement.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Josh Collins
"""

import random

def computerNumber():
    ''' This function should generate a computer number in the 1-100 range, returning that value
    from the function. '''
    return random.randint(1,100)

def userGuess():
    ''' This function should obtain a guess from the user, validate that it is in the 1-100 range,
    and return that value from the function. '''
    while True:
        # Calls user to input a valid number (must be int 1-100)
        uGuess = input('Enter a guess for # 1-100: \n')
        if uGuess.isdigit() and 1 <= int(uGuess) <= 100:
            return int(uGuess)
        # Handles if incorrect inputs (x<1,x>100,x!=int)
        elif type(uGuess) != int:
            print('Invalid input. Please enter a whole number between 1 and 100')
        else:
            print('Invalid input. Please enter a whole number between 1 and 100')


def provideFeedback(user, computer):
    ''' This function should take as inputs the guess from the user and the number from the computer,
    and will provide feedback as to whether the user's guess is too low, too high, or correct. '''
    # Returns clues to user to get the number right
    if user < computer:
        return 'Too low'
    elif user > computer:
        return 'Too high'
    else:
        return 'Correct'

def gameLoop():
    ''' This function handles the main game loop, continually calling the userGuess() and
    provideFeedback() functions until the user guesses correctly.  After the user has guessed
    correctly, this function will return 0. '''
    # Calls computer number before loop to prevent change of generated number
    computer_num = computerNumber()
    while True:
        # Returns 0 if guess is correct, if not prompts provideFeedback
        uGuess = userGuess()
        print(provideFeedback(uGuess, computer_num))
        if uGuess == computer_num:
            return 0
            

###############################################################

# Here is where you will write your basic test case functions
# Do NOT test provideFeedback here. That must go in the structured test further below

def testGeneratedNumber():
    for i in range(1000):
        aNum = computerNumber() ## generates a number
        assert 1 <= aNum and aNum <= 100, "The computer generated a number of valid range"
### ADD MORE HERE
        assert isinstance(aNum, int), 'The computer generated a number that is an integer'
###############################################################

import unittest

class TestGuessMyNumber(unittest.TestCase):

    # Here is where you will write your structured tests for the provideFeedback function

    # Added false assertions to test if it would return a failed test, worked.
    # Calls back to provideFeedback func
    def testProvideFeedbackLow(self):
        self.assertEqual(provideFeedback(1, 100), 'Too low')
        # self.assertEqual(provideFeedback(100, 1), 'Too low')

    def testProvideFeedbackHigh(self):
        self.assertEqual(provideFeedback(100, 1), 'Too high')
        # self.assertEqual(provideFeedback(1, 100), 'Too high')
        
    def testProvideFeedbackCorrect(self):
        self.assertEqual(provideFeedback(50,50), 'Correct')
        # self.assertEqual(provideFeedback(1,100), 'Correct')

    ### ADD MORE HERE
    # Test for user input, checks both if user inputs an int and if it's in valid range 1-100
    def testMyGuess(self):
        aNum = userGuess()
        assert 1 <= aNum and aNum <= 100, "The user chose a number of valid range"
        self.assertIsInstance(aNum, int), 'The user chose a number that is an integer'

    def aUtilityFunction(self, param):
        # This is a utility function which unittest.main() will NOT run automatically.
        # Your test functions could still use it though:  self.aUtilityFunction("hello")
        print("Utility function runs! Has parameter:", param)
        
###############################################################    

# Calls the game loop, as well as runs the basic and structured tests
def main():
    # Call each one of your basic test functions first:
    game = gameLoop()
    # ADD MORE HERE
    print(game)
    print("Started testing...") 
    testGeneratedNumber()
    print("Basic tests done and passed")
    unittest.main()
    print("Structured tests done and passed")

if __name__ == "__main__":
    main()