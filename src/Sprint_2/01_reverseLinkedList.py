"""
Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ l.length ≤ 105,
-109 ≤ l.value ≤ 109.

[output] linkedlist.integer

Reversed l.

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseLinkedList(l):
        prev = None
    while l:
        temp = l
        l = l.next
        temp.next = prev
        prev = temp
    return prev


"""
Given a Singly Linked List
reverse the Singly Linked List
1. we set a prev to be temp head to attach to
2. we are going to transverse the linked list
3. while transversing the list we will be switch in the pointer to point to the prev
"""


"""
The space complexity is O(1) because the operation is in-place memory.
The time complexity is O(1) because the linked list is of fixed length.
 and we are iterating once with a fixed length. which is constant
"""    
