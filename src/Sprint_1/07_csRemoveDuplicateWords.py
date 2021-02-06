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


"""
Provide a summary of your solution to this challenge. Describe the process that you went through during your attempts to solve it.

What specific obstacles or difficulties did you encounter in the process of solving it?


Taking the problem description and transforming it into a complete, actionable plan to solve that problem (oftentimes using pseudocode to do so)

"""


"""
Explain the time and space complexity of your solution. Is that the most efficient approach?
If not, how could you improve the time and/or space complexity of your solution?

Quadratic Time Complexity represents an algorithm whose performance is directly proportional to the squared size of the input data set (think of Linear, but squared).

"""