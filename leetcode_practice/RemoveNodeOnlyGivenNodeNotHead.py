# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#remove node (only given the node itself not the head)
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next.next == None:
            node.val = node.next.val
            node.next = None
        else:
            node.val = node.next.val
            node.next = node.next.next
  
            
        