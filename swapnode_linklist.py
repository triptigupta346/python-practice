# Problem Statement:
# You are given one non-empty linked lists representing some integers and one k value. you need to swap the first kth value of linked list with the last kth value in the one iteration only

# Example:
# Input: (1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7) with kth value 3
# Output: 1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7
# Explanation: swap third value 3 from starting with third value 5 from the last

class Node:
    def __init__(self,data, next =None):
        self.data = data
        self.next = next

def print_ll(head):
    current = head
    while(current != None):
        print(current.data)
        current = current.next

def swap_node(head,k):
    current = head;
    current_last = head;
    first_node = current;
    p=0;
    while(current):
        p = p+1;
        if(p==k):
            next_node = current_last;
        elif(p>k):
            next_node = next_node.next
        else:
            first_node = first_node.next
        current = current.next;

    first_val = first_node.data
    first_node.data = next_node.data
    next_node.data = first_val

ls = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
print_ll(ls)
swap_node(ls,3)
print("swap list:")
print_ll(ls)
