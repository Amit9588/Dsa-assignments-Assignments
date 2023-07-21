#Reversal of Linked List
#Given a singly linked list, give me the reversal of the linked list.
#For example 
#Input - 1 -> 2 -> 3 -> 4 -> 5
#Output - 5 -> 4 -> 3 -> 2 -> 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

#Convert a singly linked list into a circular linked list
def convert_to_circular(head):
    if head is None:
        return None

    current = head
    while current.next is not None:
        current = current.next

    current.next = head
    return head

#Palindrome Linked List
def is_palindrome(head):
    slow = fast = head

    # Find the middle of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Compare elements of the first and reversed second half
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next

    return True



#Sort 0s, 1s, and 2s in ascending order in Linked List
def sort_list(head):
    count = [0, 0, 0]
    current = head

    while current:
        count[current.val] += 1
        current = current.next

    current = head

    for i in range(3):
        while count[i] > 0:
            current.val = i
            current = current.next
            count[i] -= 1

    return head

#Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s. 
#Linked List Cycle
#Given a linked list, detect the loop inside the linked list.
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

#Remove Nth Node from End of List
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy

    # Move second pointer n steps ahead
    for i in range(n + 1):
        second = second.next

    # Move both pointers until the second pointer reaches the end
    while second:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    first.next = first.next.next

    return dummy.next
