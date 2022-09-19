'''
연결 리스트틀 입력받아 pair 단위로 스왑하라.
입력 : 1->2->3->4
출력 : 2->1->4->3
'''
class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self,head:ListNode)-> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
