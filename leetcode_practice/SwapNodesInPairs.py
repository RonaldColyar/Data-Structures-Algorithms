


'''

Given a linked list, swap every two adjacent nodes and return its head.

Runtime: 24 ms, faster than 95.95% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.3 MB, less than 52.88% of Python3 online submissions for Swap Nodes in Pairs.


'''


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        #check to see if there are at least two in the list
        
        if head == None:
            return head
        elif head.next == None:
                
                
            return head
        else:
            prev_node = head
            current_node = head.next
            
            while  True:
                #storing the node values before changing
                prev_val = prev_node.val 
                current_val = current_node.val
                #swap them
                prev_node.val = current_val
                current_node.val = prev_val

                #validate that there are two more nodes
                #for example if the list is [1,2,3] current_node will be 1 and prev_node will be 2
                #so then we check to see if there are two values after 2 
                #if there aren't two values after 2 our work is finished.
                #if there is two values then we need to swap them on the next iteration.

                if current_node.next != None:
                    if current_node.next.next != None:
                        prev_node = current_node.next
                        current_node = current_node.next.next
                    else:
                        break
                else:
                    break
                        
            return head
            
        