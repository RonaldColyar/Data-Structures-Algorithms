


"""

Runtime: 44 ms, faster than 51.33% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.2 MB, less than 74.14% of Python3 online submissions for Remove Duplicates from Sorted List.`

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current_node = head
        if head == None:
            return head
        while current_node.next != None:
             if current_node.val == None: #if the first node is empty
                    current_node = current_node.next
             else:
                 if current_node.val == current_node.next.val:
                        if current_node.next.next!= None:
                            current_node.next = current_node.next.next
                        else:
                            current_node.next =   None
                 else:
                    current_node = current_node.next
                        
        return head