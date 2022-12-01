# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        i = 0
        while l1:
            n1 += int(l1.val*10**i)
            i+=1
            l1 = l1.next
        i =0 
        while l2:
            n2 += int(l2.val*10**i)
            i+=1
            l2 = l2.next
        if n1+n2 ==0:
            return ListNode()
        n3 = n1+n2
        head = ListNode(n3%10)
        n3 = n3//10
        temp = head
        while n3>0:
            new = ListNode(n3%10)
            n3 = n3//10
            temp.next = new
            temp = new
        return head
