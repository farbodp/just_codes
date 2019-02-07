'''-MixUp
 Given strings a and b, return a single string with a and b separated
 by a space '<a> <b>', except swap the first 2 chars of each string.
 e.g.
   'mix', 'pod' -> 'pox mid'
   'dog', 'dinner' -> 'dig donner'
 Assume a and b are length 2 or more.'''
def mix_up(a, b):
  return b[:2]+a[2:]+' '+a[:2]+b[2:]



''' -verbing
Given a string, if its length is at least 3,
add 'ing' to its end.
Unless it already ends in 'ing', in which case
add 'ly' instead.
If the string length is less than 3, leave it unchanged.
Return the resulting string.'''
def verbing(s):
  # +++your code here+++
  return



'''Write a Python function to remove the nth index character from a nonempty string.'''
def remove_char(s, n):
  return s[:n] + s[n+1:]



'''Write a Python program to change a given string to a new string
where the first and last chars have been exchanged.'''
def change_string(str1):
  # +++your code here+++
  return



'''Write a Python function to insert a string in the middle of a string'''
def insert_string_middle(s, word):
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




''' -front_back
 Consider dividing a string into two halves.
 If the length is even, the front and back halves are the same length.
 If the length is odd, we'll say that the extra char goes in the front half.
 e.g. 'abcde', the front half is 'abc', the back half 'de'.
 Given 2 strings, a and b, return a string of the form
  a-front + b-front + a-back + b-back'''
def front_back(a, b):
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
  return s[0] + s[1:].replace(s[0], '*')




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
  if weekday==True and vacation==False:
      return False
  else:
      return True



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




# when you run this file, the program starts from here:
if __name__=='__main__':
    print(fix_start('babble'))

  