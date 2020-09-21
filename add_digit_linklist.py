# Problem Statement:
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None

    def print_ll(self,head):
        current = head
        while(current):
            print(current.data,end =" ")
            current = current.next

    def add(self,ll1,ll2):
        carry = 0
        Last = None
        while(ll1 or ll2):
            if(ll1 and ll2):
                addition = ll1.data+ll2.data+carry
            elif(ll1):
                addition = ll1.data + carry
            elif(ll2):
                addition = ll2.data + carry
            sum = addition%10
            carry = int(addition/10)
            if(Last):
                Last.next=Node(sum)
                Last = Last.next
            else:
                self.head = Node(sum)
                Last = self.head
            if(ll1):
                ll1=ll1.next
            if(ll2):
                ll2=ll2.next

        if(carry != 0):
            Last.next = Node(carry)

        return(self.head)

#139
ll = Linklist()
print("First num")
l1 = Node(1,Node(3,Node(9)))
ll.print_ll(l1)
print("\n")
print("Second num")
#923
l2= Node(9,Node(2,Node(3)))
ll.print_ll(l2)
print("\n")
print("Sum:")
ll.print_ll(ll.add(l1,l2))


