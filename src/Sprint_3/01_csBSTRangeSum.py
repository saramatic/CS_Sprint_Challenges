"""
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32
Example 2:

Input:
root = [10,5,15,3,7,13,18,1,null,6]
lower = 6
upper = 10

           10
          /  \
       5       15
     / \     /   \ 
    3   7  13   18
   /   /
  1   6

Output:
23
[execution time limit] 4 seconds (py3)

[input] tree.integer root

[input] integer lower

[input] integer upper

[output] integer
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    
    # BST recursive solution to traverse the BST
    # with 4 different cases
    def helper(node, lower, upper, total):
        # base case node is Node 
        if node is None:
            # return total
            return total
        
        # case that the node value is in the range    
        if lower <= node.value <= upper:
            # add the value
            total += node.value
            # traverse left
            total = helper(node.left, lower, upper, total)
            # traverse right
            total = helper(node.right, lower, upper, total)
            
        
        # we hit the lower bound bounce back and traverse right
        if node.value < lower:
            total = helper(node.right, lower, upper, total)
            
        # we hit the upper bound bounce back and traverse left    
        if node.value > upper:
            total = helper(node.left, lower, upper, total)
        
        # return total
        return total


    return helper(root, lower, upper, 0)


"""
If you use a recursive approach, 
then at each stage, you have to make a recursive call. 
That means leaving the current invocation on the stack, 
and calling a new one. ... 
With your iterative code, you're allocating one variable (O(1) space) 
plus a single stack frame for the call (O(1) space).
"""

