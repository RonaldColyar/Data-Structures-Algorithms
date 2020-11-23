


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node = l1
        current_node2 = l2
        number1 = ""
        number2 = ""
        
        while current_node != None :
            number1 = number1 + str(current_node.val)
            current_node = current_node.next
        while current_node2 != None:
            number2 = number2 +str(current_node2.val)
            current_node2 = current_node2.next
        #reverse the numbers
        number1 = number1[::-1]
        number2 = number2[::-1]
        #get the result and reverse it
        result = int(number1) + int(number2)
        formatted_result = str(result)[::-1]
        #create the linked list
        head = ListNode(formatted_result[0])
        current = head
        for i in range(1,len(formatted_result)):
            new_node = ListNode(formatted_result[i])
            current.next = new_node
            current = new_node
        return head
