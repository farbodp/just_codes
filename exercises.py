'''-MixUp
 Given strings a and b, return a single string with a and b separated
 by a space '<a> <b>', except swap the first 2 chars of each string.
 e.g.
   'mix', pod' -> 'pox mid'
   'dog', 'dinner' -> 'dig donner'
 Assume a and b are length 2 or more.'''
def mix_up(a, b):
  # +++your code here+++
  return


'''-donuts
 Given an int count of a number of donuts, return a string
 of the form 'Number of donuts: <count>', where <count> is the number
 passed in. However, if the count is 10 or more, then use the word 'many'
 instead of the actual count.
 So donuts(5) returns 'Number of donuts: 5'
 and donuts(23) returns 'Number of donuts: many'''
def donuts(count):
  # +++your code here+++
  return



'''-both_ends
 Given a string s, return a string made of the first 2
 and the last 2 chars of the original string,
 so 'spring' yields 'spng'. However, if the string length
 is less than 2, return instead the empty string.'''
def both_ends(s):
  # +++your code here+++
  return


'''-fix_start
 Given a string s, return a string
 where all occurences of its first char have
 been changed to '*', except do not change
 the first char itself.
 e.g. 'babble' yields 'ba**le'
 Assume that the string is length 1 or more.
 Hint: s.replace(stra, strb) returns a version of string s
 where all instances of stra have been replaced by strb.'''
def fix_start(s):
  # +++your code here+++
  return


''' The goal of this exercise is to convert a string to a new string
 where each character in the new string is '(' if that character
 appears only once in the original string, or ')' if that character
 appears more than once in the original string. Ignore capitalization
 when determining if a character is a duplicate.
 Examples:
 "din" => "((("
 "recede" => "()()()"
 "Success" => ")())())"
 "(( @" => "))(("
'''
def duplicate_encode(word):
  # +++your code here+++
  return


''' This time no story, no theory. The examples below show you how to write function accum:
 Examples:
 accum("abcd") -> "A-Bb-Ccc-Dddd"
 accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
 accum("cwAt") -> "C-Ww-Aaa-Tttt"
 The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(word):
  # +++your code here+++
  return


''' The parameter weekday is True if it is a weekday,
 and the parameter vacation is True if we are on vacation.
 We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
 sleep_in(False, False) → True
 sleep_in(True, False) → False
 sleep_in(False, True) → True '''
def sleep_in(weekday, vacation):
  # +++your code here+++
  return


''' Write a function called accept_login(users, username, password)
 with three parameters: users a dictionary of username
 keys and password values, username a string for a login name and
 password a string for a password. The function should return
 True if the user exists and the password is correct and False otherwise'''
def accept_login(users, username, password):
  # +++your code here+++
  return


'''Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
(Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''
def spin_words(sentence):
    # Your code goes here
    return


# just for test
