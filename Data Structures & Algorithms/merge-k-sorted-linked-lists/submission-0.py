# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        if not lists[0]:
            return None

        import heapq

        heap = []

        for head in lists: # --- O(K)
            curr = head
            while curr:
                heapq.heappush(heap,curr.val)
                curr = curr.next
            
        nhead = ListNode()

        ncurr = nhead

        while heap:
            node = ListNode(heapq.heappop(heap))
            ncurr.next = node
            ncurr = ncurr.next
        
        return nhead.next

        

            




        
        
        