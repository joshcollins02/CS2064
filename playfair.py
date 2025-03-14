""" Refer to the instructions on Canvas for more information.

"I have neither given nor received unauthorized help on this assignment."
author: Josh Collins """

from string import ascii_lowercase
import unittest

def createTable(phrase):
    ''' Given an input string, create a lowercase playfair table.  The
    table should include no spaces, no punctuation, no numbers, and 
    no Qs -- just the letters [a-p]+[r-z] in some order.  Note that 
    the input phrase may contain uppercase characters which should 
    be converted to lowercase.
    
    Input:   string:         a passphrase
    Output:  list of lists:  a ciphertable '''

    # Reference table
    # [['i', 'a', 'm', 'e', 'n'], 
    #  ['t', 'r', 'g', 'p', 's'], 
    #  ['h', 'b', 'c', 'd', 'f'], 
    #  ['j', 'k', 'l', 'o', 'u'], 
    #  ['v', 'w', 'x', 'y', 'z']]
    
    # Converting a list to all lowercase letters
    phrase = phrase.lower()
    # Removes special characters
    phrase = ''.join(c for c in phrase if c.isalpha() and c != 'q')
    see = set()
    unique_chars = [c for c in phrase if c not in see and not see.add(c)]
    # Sorts the unique chars in alphabetical order
    chars = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in unique_chars and c != 'q']
    chars2 = unique_chars + chars
    # Creates a 5x5 table with the characters in the correct order
    table = [chars2[i:i+5] for i in range(0,25,5)]
    return table

def splitString(plaintext):
    ''' Splits a string into a list of two-character pairs.  If the string
    has an odd length, append an 'x' as the last character.  As with
    the previous function, the bigrams should contain no spaces, no
    punctuation, no numbers, and no Qs.  Return the list of bigrams,
    each of which should be lowercase.
    
    Input:   string:  plaintext to be encrypted
    Output:  list:    collection of plaintext bigrams '''
    
    # Converts to lowercase and removes q
    plaintext = ''.join([char for char in plaintext.lower() if char.isalpha()])
    plaintext = plaintext.replace('q', '')
    # If odd append x to create pairs
    if len(plaintext) % 2 != 0:
        plaintext += 'x'
    # Split into pairs of 2
    two_pair = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    return two_pair
        
def playfairRuleOne(pair):
    ''' If both letters in the pair are the same, replace the second
    letter with 'x' and return; unless the first letter is also
    'x', in which case replace the second letter with 'z'.
    
    You can assume that any input received by this function will 
    be two characters long and already converted to lowercase.
    
    After this function finishes running, no pair should contain two
    of the same character   
    
    Input:   string:  plaintext bigram
    Output:  string:  potentially modified bigram '''

    # If two letters are the same turns second into x
    if pair[0] == pair[1]:
    # If both are x turns second into z
        if pair[0] == 'x':
            pair = pair[0] + 'z'
        else:
            pair = pair[0] + 'x'
    return pair

def playfairRuleTwo(pair, table):
    ''' If the letters in the pair appear in the same row of the table, 
    replace them with the letters to their immediate right respectively
    (wrapping around to the left of a row if a letter in the original
    pair was on the right side of the row).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''

    # Checks for both in same row
    for row in table:
        if pair[0] in row and pair[1] in row:
            index0 = row.index(pair[0])
            index1 = row.index(pair[1]) 
    # Shifts right by 1
            new_index0 = (index0 + 1) % 5
            new_index1 = (index1 + 1) % 5
    # Replaces with shifted pair
            pair = row[new_index0] + row[new_index1]
            return pair
    # If not in same row returns original
    return pair

def playfairRuleThree(pair, table):
    ''' If the letters in the pair appear in the same column of the table, 
    replace them with the letters immediately below respectively
    (wrapping around to the top of a column if a letter in the original
    pair was at the bottom of the column).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    
    # Does same as rule 2 excepts transposes the table to handle vertical "columns"
    transposed_table = list(map(list, zip(*table)))

    for col in transposed_table:
        if pair[0] in col and pair[1] in col:
            index0 = col.index(pair[0])
            index1 = col.index(pair[1]) 
            
            new_index0 = (index0 + 1) % 5
            new_index1 = (index1 + 1) % 5

            pair = col[new_index0] + col[new_index1]
            return pair
    return pair
    
def playfairRuleFour(pair, table):
    ''' If the letters are not on the same row and not in the same column, 
    replace them with the letters on the same row respectively but in 
    the other pair of corners of the rectangle defined by the original 
    pair.  The order is important -- the first letter of the ciphertext
    pair is the one that lies on the same row as the first letter of 
    the plaintext pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.  
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    
    # Intialize
    index0 = index1 = None
    # Checks if first and second char in current rows and stores them
    for r, row in enumerate(table):
        if pair[0] in row:
            index0 = (r, row.index(pair[0]))
        if pair[1] in row:
            index1 = (r, row.index(pair[1]))  
    # If not found in rows, checks columns and does the same thing              
    if index0 is None or index1 is None:
        for c in range(5):
            column = [table[r][c] for r in range(5)]
            if pair[0] in column:
                index0 = (column.index(pair[0]), c)
            if pair[1] in column:
                index1 = (column.index(pair[1]), c)
    # If in different, executes rectangle swap and returns new pair
    if index0[0] != index1[0] and index0[1] != index1[1]:
        n_char0 = table[index0[0]][index1[1]]
        n_char1 = table[index1[0]][index0[1]]
        return n_char0 + n_char1
    # If in same returns original pair
    else:
        return pair
                
def encrypt(pair, table):
    ''' Given a character pair, run it through all four rules to yield
    the encrypted version!
    
    Input:   string:         plaintext bigram
    Input:   list of lists:  ciphertable
    Output:  string:         ciphertext bigram '''

    # Runs the pair through all rules to return true pair
    pair = playfairRuleOne(pair)
    pair = playfairRuleTwo(pair, table)
    pair = playfairRuleThree(pair, table)
    pair = playfairRuleFour(pair, table)
    return pair

def joinPairs(pairsList):
    ''' Given a list of many encrypted pairs, join them all into the 
    final ciphertext string (and return that string)
    
    Input:   list:    collection of ciphertext bigrams
    Output:  string:  ciphertext '''
    
    # Intialize
    ciphertext = ''
    # Checks for pair and stores it in empty string
    for pair in pairsList:
        if len(pair) == 2:
            ciphertext += pair
    # If only one then adds solo to string
        else:
            ciphertext += pair[0]
    return ciphertext

def main(): 
    ''' Example main() function '''

    # Pre-test for test cases based on each func

    table = createTable("i am entering a pass phrase")
    print(table)
    
    splitMessage = splitString("this is a test message")
    print(splitMessage)
    
    modified_pairs = [playfairRuleTwo(pair, table) for pair in splitMessage]
    print(modified_pairs)
    
    modified_pairs2 = [playfairRuleThree(pair, table) for pair in splitMessage]
    print(modified_pairs2)
    
    modified_pairs3 = [playfairRuleFour(pair, table) for pair in splitMessage]
    print(modified_pairs3)

    pair = 'th'
    print(encrypt(pair, table))

    print(joinPairs(modified_pairs))

    pairsList = []

    # print(table) # printed for debugging purposes
    
    for pair in splitMessage:
        # Note: encrypt() should call the four rules
        pairsList.append(encrypt(pair, table))
    cipherText = joinPairs(pairsList)
    
    print(cipherText) #printed as the encrypted output
    #output should be be hjntntirnpginprnpm
    print("Done with main!")


###############################################################

class TestPlayfair(unittest.TestCase):
    # Below are your tests.  Remember structured tests need to named with 'test' in the
    # beginning so that unittest recognizes them and runs them. 

    def testTable(self):
        # Creates a table and checks correct placing of letters, as well as the size and no letters are missing
        
        phrase = "i am entering a pass phrase"
        table = createTable(phrase)

        assert table[0][0] == 'i'
        assert table[1][1] == 'r'
        
        assert len(table) == 5
        for row in table:
            assert len(row) == 5


    def testSplit(self):
        # Tests that a message is correctly split into pairs, removes special characters, and appends x to odd phrases
        self.assertEqual(splitString("this is a test message"), ['th', 'is', 'is', 'at', 'es', 'tm', 'es', 'sa', 'ge'])
        self.assertEqual(splitString("hello"), ['he', 'll', 'ox'])
        self.assertEqual(splitString("abcdefg"), ['ab', 'cd', 'ef', 'gx'])
        self.assertEqual(splitString("Hello!"), ['he', 'll', 'ox'])

    def testOne(self):
        # Tets rule 1, 2 same changes x to the end 2 xs changes z to the end
        self.assertTrue(playfairRuleOne('aa'), ('ax'))
        assert playfairRuleOne('aa') == 'ax'
        assert playfairRuleOne('xx') == 'xz'
        assert playfairRuleOne('ab') == 'ab'

    def testTwo(self):
        # Tests rule 2, if letters are in the same row, and wrapping rows

        phrase = "i am entering a pass phrase"
        table = createTable(phrase)

        self.assertTrue(playfairRuleTwo('am', table), 'me')
        self.assertTrue(playfairRuleTwo('ux', table), 'vz')
        self.assertTrue(playfairRuleTwo('ry', table), 'ka')
        self.assertTrue(playfairRuleTwo('st', table), 'to')

    def testThree(self):
        # Tests rule 3, transposed version of rule 2

        phrase = "i am entering a pass phrase"
        table = createTable(phrase)

        self.assertTrue(playfairRuleThree('am', table), 'me') 
        self.assertTrue(playfairRuleThree('th', table), 'tg')
        self.assertTrue(playfairRuleThree('ok', table), 'kd')
        self.assertTrue(playfairRuleThree('gx', table), 'ag')

    def testFour(self):
        # Tests rule 4, if pairs will rotate in a rectangle

        phrase = "i am entering a pass phrase"
        table = createTable(phrase)

        self.assertEqual(playfairRuleFour('th', table), 'th')
        self.assertEqual(playfairRuleFour('is', table), 'nt')
        self.assertEqual(playfairRuleFour('at', table), 'ir')
        self.assertEqual(playfairRuleFour('es', table), 'np')

    def testEncrypt(self):
        # Tests encrypt, based on each rule
        
        phrase = "i am entering a pass phrase"
        table = createTable(phrase)
        
        self.assertTrue(encrypt('th', table), 'tr')
        self.assertTrue(encrypt('me', table), 'me')
        self.assertTrue(encrypt('ok', table), 'ld')
        self.assertTrue(encrypt('am', table), 'ie')

    def testJoin(self):
        # Tests join to make sure pairs come back together

        self.assertTrue(joinPairs(['hi', 'hi']), 'hihi')
        self.assertTrue(joinPairs(['ab', 'cd', 'ef']), 'abcdef')
        self.assertTrue(joinPairs(['ab', 'cd', 'ef', 'gh']), 'abcdefgh')
        self.assertTrue(joinPairs(['ab']), 'ab')
    
    print('Done with unit tests!')

###############################################################    

if __name__ == "__main__":
    main()
    unittest.main()       