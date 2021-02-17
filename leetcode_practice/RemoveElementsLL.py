# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #our reference to the true head
        truehead = ListNode()
        #linking new listnode with values
        truehead.next = head
        #our 'reference' to the current node
        current = truehead
        #while there is a current node and  next  of the linked list
        while current and current.next:
            #if the next value in the list matches the element to delete
            if current.next.val == val:
                #remove the element from the list
                current.next = current.next.next
            else:
                current = current.next
            #only would like to recieve nodes that have vals
        return truehead.next
