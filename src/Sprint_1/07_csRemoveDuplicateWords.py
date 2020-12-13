"""
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string

"""

def csRemoveDuplicateWords(input_str):

   oList = input_str.split()
   nList = []
   listToSTring = ""

   for x in oList:
       if x not in nList:
           nList.append(x)
           listToSTring += " " + x

   return listToSTring.strip()

print(csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta"))