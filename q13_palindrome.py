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
from typing import List
class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = None
def 
