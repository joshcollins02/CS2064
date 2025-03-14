# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Josh Collins
"""
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []
        
        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList

def reduceOne(firstString, secondString, wordList):
    # Here is where you will write your function to determine
    # if the second string can be reduced from the first string

    # Check for non empty strings
    if firstString and secondString and firstString in wordList and secondString in wordList:
        # If current word is 1 longer and to iterate over each char in string
        if len(firstString) == len(secondString) + 1:
            for i in range(len(firstString)):
                ansstring = firstString[:i] + firstString[i + 1:]
                # See if equal
                if ansstring == secondString:
                    return True
        # If current word is 1 shorter and to iterate over each char in string
        elif len(firstString) == len(secondString) - 1:
            for i in range(len(secondString)):
                # Remove current
                ansstring = secondString[:i] + secondString[i + 1:]
                # See if equal
                if ansstring == firstString:
                    return True
        # If same length
        elif len(firstString) == len(secondString):
            # Look for differences
            diffCount = 0
            for i in range(len(firstString)):
                if firstString[i] != secondString[i]:
                    diffCount += 1
            # If equal to 1 return True
            if diffCount == 1:
                return True
        return False
    return False
    
def reduceAll(word, wordList):
    # Here is where you will write your function to determine
    # all word reductions that can be obtained from the input word
    # after removing one letter

    # Storeable list
    reduce = []
    # Iterate over chars
    for i in range(len(word)):
        newWord = word[:i] + word[i + 1:]
        # Check if in list
        if newWord in wordList:
            # add it to list
            reduce.append(newWord)
    return reduce
        
def reduceTwoAll(word, wordList):
    # Here is where you will write your function to determine
    # all word reductions that can be obtained from the input word
    # after removing two letters

    # Storeable list
    reduce2 = []
    # Iterate over chars
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            newWord = word[:i] + word[i + 1:j] + word[j + 1:]
            # If the resulting word is in word list and is greater than 1
            if newWord in wordList and len(newWord) > 1:
                reduce2.append(newWord)
    return reduce2

def validateReduction(reduction, wordList):
    # Here is where you will write your function to determine
    # whether or not the provided sequence is a valid one-letter
    # reduction, checking for both the character removal and the
    # validity of each word

    # If the first word in the reduction sequence can be reduced to the second word
    if len(reduction) > 1 and not reduceOne(reduction[0], reduction[1], wordList):
        return False
    # Iterate over adjacent words
    for i in range(len(reduction) - 1):
        # If current word is 1 longer and if it can be reduced to the next word
        if not reduceOne(reduction[i], reduction[i + 1], wordList):
                return False
    # Check for words in list
    for word in reduction:
        if word not in wordList:
            return False
    return True
    
    
def main():
    # Here is where you will call your test cases
    wordList = loadWords()
    
    firstString = wordList[0]
    secondString = wordList[1]
    if reduceOne(firstString, secondString, wordList):
        print(f"{secondString} can be reduced to {firstString} by removing one letter.")
    else:
        print(f"{secondString} cannot be reduced to {firstString} by removing one letter.")

    word = wordList[3030]
    reduce = reduceAll(word, wordList)
    print(f"One-letter reductions of {word}: {reduce}")

    word = wordList[3005]
    reduce = reduceTwoAll(word, wordList)
    print(f"Two-letter reductions of {word}: {reduce}")

    reduce = wordList[100]
    if validateReduction(reduce, wordList):
        print('Valid:', reduce)
    else:
        print('Invalid:', reduce)

    reduce = ['boats', 'oats', 'oat', 'at']
    if validateReduction(reduce, wordList):
        print('Valid:', reduce)
    else:
        print('Invalid:', reduce)

    reduce = ['leave', 'eave']
    if validateReduction(reduce, wordList):
        print('Valid:', reduce)
    else:
        print('Invalid:', reduce)

###############################################################

# Here is where you will write your test case functions
import unittest

class TestTime(unittest.TestCase):
# Below are the tests for reduce()
    def test1(self):
    # This comment explains what test1() is testing for, and is followed by code
    # Test that reduceOne() returns True when the first string can be reduced to the second string
        wordList = loadWords()
        self.assertTrue(reduceOne('a', 'aa', wordList))
        self.assertTrue(reduceOne('b', 'bb', wordList))
        self.assertTrue(reduceOne('c', 'cc', wordList))
        self.assertTrue(reduceOne('arg', 'argh', wordList))
        self.assertTrue(reduceOne('res', 'rest', wordList))
        self.assertTrue(reduceOne('far', 'fart', wordList))

    def test2(self):
    # This comment explains what test2() is testing for, and is followed by code
    # Test that reduceAll() returns True when the word can be reduced correctly
        wordList = loadWords()
        self.assertTrue(reduceAll('hello', wordList), ['ello', 'hllo', 'helo', 'hell'])
        self.assertTrue(reduceAll('fart', wordList), ['far', 'arf', 'raf'])
        self.assertTrue(reduceAll('abc', wordList), ['ac', 'bc', 'ab'])
        self.assertTrue(reduceAll('take', wordList), ['tak', 'ake', 'tae'])

    # Below are the tests for reduce2()
    def testN(self):
    # This comment explains what testN() is testing for, and is followed by code
    # Test that reduce2() returns True when the word can be reduced correctly
        wordList = loadWords()
        self.assertTrue(reduceTwoAll('hello', wordList), ['hll', 'ell', 'hel', 'llo'])
        self.assertTrue(reduceTwoAll('world', wordList), ['wor', 'rld', 'orl', 'wld'])
        self.assertTrue(reduceTwoAll('times', wordList), ['tim', 'ime', 'mes', 'tie'])
        self.assertTrue(reduceTwoAll('happy', wordList), ['hap', 'ppy', 'hay', 'app'])

    def testValid(self):
        # This comment explains what testValid() is testing for, and is followed by code
        # Test that validateReduction() returns True when the word can be reduced correctly
        wordlist = loadWords()
        self.assertTrue(validateReduction(['hello'], wordlist))
        self.assertFalse(validateReduction(['hello', 'helo'], wordlist))
        self.assertTrue(validateReduction(['hello', 'hell'], wordlist))
        self.assertFalse(validateReduction(['hello', 'helo', 'hi'], wordlist))
    
###############################################################    
    
if __name__ == "__main__":
    main()  
    unittest.main()  