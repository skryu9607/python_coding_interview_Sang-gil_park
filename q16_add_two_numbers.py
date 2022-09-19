'''
역순으로 저장된 연결 리스트의 숫자를 더하라. 
입력 : 2->4->3 + 5->6->4 
출럭 : 7->0->8

'''

class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = next
# 연결리스트 뒤집기
def reverseList(head: ListNode)-> ListNode:
    node,prev = head,None
    while node:
        next,node.next = node.next,prev
        prev,node = node, next
    return prev
# 연결리스트를 파이썬리스트로 변환
def toList(node:ListNode) -> list:
    LIST = []
    while node:
        LIST.append(node.val)
        node = node.next
    return LIST
# 파이썬 리스트를 연결 리스트로 변환
def toLinked(result:str) -> ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
    return node
def addTwoNumbers(l1:ListNode,l2:ListNode) -> ListNode:
    
    a = toList(reverseList(l1))
    b = toList(reverseList(l2))

    result = int(''.join(str(e) for e in a))+int(''.join(str(e) for e in b))
    
    return  toLinked(str(result))

