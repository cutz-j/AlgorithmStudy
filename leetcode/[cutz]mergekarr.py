import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        root = res = ListNode(None)
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        print(heap)
        while heap:
            m = heapq.heappop(heap)
            idx = m[1]
            res.next = m[2]
            res = res.next
            if res.next:
                heapq.heappush(heap, (res.next.val, idx, res.next))

        return root.next
