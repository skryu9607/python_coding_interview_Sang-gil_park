'''
연결 리스트가 팰린드롬 구조인지 판별해라.
입력 : 1 -> 2
출력 : False
입력 : 1->2->2->1
출력 : True

'''
'''
import collections
def isPalindrome(head:list) -> bool:
    # 데크 자료형 선언
    q = collections.deque()
    if len(q) == 1:
        return True
    for node in head:
        q.append(node)
    while len(q) > 1:
        if q.popleft()!=q.pop():
            return False
    return True
input = [2,3,3,2,2]
print(isPalindrome(input))
'''

# Node definition
class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = None
'''head = ListNode(0)
# Add new_node
curr_node = head
new_node = ListNode(1)
curr_node.next = new_node
curr_node = curr_node.next

curr_node.next = ListNode(2)
curr_node = curr_node.next
# Print all node
node = head
while node:
    print(node.val)
    node=node.next
# Delete node by value
node = head
while node.next:
    if node.next.val == 2:
        next_node = node.next.next
        node.next = next_node'''
