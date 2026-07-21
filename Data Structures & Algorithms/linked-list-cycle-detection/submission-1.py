# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr = head

        while itr:
            if itr.val == 9999:
                return True
            
            itr.val = 9999
            itr = itr.next
        
        return False