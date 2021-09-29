# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def addTwoNumbers(l1, l2):
    out = ret = ListNode()
    carry = 0
    while l1 or l2 or carry:
        if not l1 and not l2:
            sum = carry
        elif l1 and l2:
            sum = l1.val + l2.val + carry
            l1, l2 = l1.next, l2.next
        elif l1:
            sum = l1.val + carry
            l1 = l1.next
        elif l2:
            sum = l1.val + carry
            l2 = l2.next

        if sum >= 10:
            carry = 1
            sum = sum % 10
        else:
            carry = 0

        ret.val = sum
        ret.next = ListNode()
        ret = ret.next

    return out

# TEST 1 STANDARD 3 DIGIT INPUT
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)

l3.next = l2
l2.next = l1

l9.next = l8
l8.next = l7

n1 = addTwoNumbers(l3, l9)
print(n1)

# TEST 2 ASYMMETRICAL INPUT LENGTH
l2 = ListNode(1)
l3 = ListNode(2)

l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)

l3.next = l2

l9.next = l8
l8.next = l7

print(addTwoNumbers(l3, l9))

# TEST 3 EMPTY NODES
l1 = ListNode()
l2 = ListNode()
print(addTwoNumbers(l1, l2))

# TEST 4 CARRY VALUE
l1 = ListNode(9)
l2 = ListNode(9)
print(addTwoNumbers(l1, l2))

# while n1:
    # print(n1.val)
    # n1 = n1.next

# while there is still either a node or a carry
#     # addition
#     add the nodes and the carry
#     if the sum > 10
#         do mod 10 and carry = 1
#     append sum to sums
#     move on to the next set of nodes
# # return
# iterate through sums
# build linked list in reverse order

# 9 + 9
# sum = 18
# carry = 1
# sum = 8
# ret.val = 8
# ret.next = ListNode()
# !next

# 12 + 789
# 9 + 2 + 0 = 11
# sum = 1, carry = 1
# 1 + 8 + 1 = 10
# sum = 0, carry = 1
# none + 7 + 1
#
# 123 + 789