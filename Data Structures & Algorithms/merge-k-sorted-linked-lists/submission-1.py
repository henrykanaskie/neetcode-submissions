# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        merged_list = []
        for i in range(len(lists)):
            merged_list = self.merge2Lists(merged_list, lists[i])
        
        return merged_list

    def merge2Lists(self, l1, l2):
        print((l1, l2))
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
               node.next = l2
               l2 = l2.next
            node = node.next
        node.next = l1 or l2

        return dummy.next
                
            


