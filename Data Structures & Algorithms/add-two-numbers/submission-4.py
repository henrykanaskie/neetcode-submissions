# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = ListNode()
        result = dummy

        carry = 0
        nodesum = 0
        while cur1 or cur2:
            if cur1 is None:
                nodesum = cur2.val + carry
                cur2 = cur2.next
            elif cur2 is None:
                nodesum = cur1.val + carry
                cur1 = cur1.next
            else:
                nodesum = cur1.val + cur2.val + carry
                cur1 = cur1.next
                cur2 = cur2.next

            if nodesum > 9:
                carry = 1
                nodesum = nodesum % 10 
            else:
                carry = 0    

            result.next = ListNode(nodesum)  
            result = result.next
            

        if carry > 0:
            result.next = ListNode(carry)
        
        return dummy.next
