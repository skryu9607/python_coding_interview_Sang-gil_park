'''
연결리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성해라. 공간복잡도 O(1), 시간복잡도 O(N)
입력 : 1->2->3->4->5->NULL
출력 : 1->3->5->2->4->NULL

'''
class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = next
class Solution:
    def odd_Even_list(self,head:ListNode)->ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next
        while even and even.next:
            odd.next,even.next = odd.next.next,even.next.next
            odd,even = odd.next,even.next
            
        odd.next = even_head
        return head
