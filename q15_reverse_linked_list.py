'''
연결 리스트를 뒤집어라.
입력 : 1->2->3->4->5->NULL
출력 : 5->4->3->2->1->NULL

'''
class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = next
class Solution(object):
    def revereList(self,head:ListNode)->ListNode:
        node,prev = head,None
        while node:
            next,node.next = node.next, prev
            prev, node = node, next
        return prev
