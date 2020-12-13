"""
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

csCheckPalindrome("racecar") -> true
csCheckPalindrome("anna") -> true
csCheckPalindrome("12345") -> false
csCheckPalindrome("12321") -> true
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] boolean

"""

def csCheckPalindrome(input_str):

    return input_str == input_str[::-1]
 

print(csCheckPalindrome("racecar")) 
print(csCheckPalindrome("12345"))   