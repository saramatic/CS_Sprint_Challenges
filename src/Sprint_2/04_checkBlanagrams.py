"""

Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string word1

A string consisting of lowercase letters.

Guaranteed constraints:
1 ≤ word1.length ≤ 100.

[input] string word2

A string consisting of lowercase letters.

Guaranteed constraints:
word2.length = word1.length.

[output] boolean

Return true if word1 and word2 are blanagrams of each other, otherwise return false.
"""
def checkBlanagrams(word1, word2):
    
