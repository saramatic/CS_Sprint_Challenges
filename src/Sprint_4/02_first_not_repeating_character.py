"""

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

[output] char

The first non-repeating character in s of '_' if there are no characters that do not repeat.
"""
def first_not_repeating_character(s):
    """
    :type s: str
    :rtype: int
    """
    count = {}

    # use dict count to Count frequency of letters
    for char in range(len(s)):
        if s[char] not in count:
            count[s[char]] = 1
        else :
            count[s[char]] += 1

    # search for 1st

    for index, char in enumerate(s):
        if count[char] == 1:
            return char
    return '_'
    
