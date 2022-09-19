'''
정렬되어 있는 두 연결 리스트를 합쳐라.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self,data):
        self.head = Node(data)
    def append(self,data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    def get_node(self,index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
    def add_node(self, index,value):
        new_node = Node(value)
        if index ==0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

class ListNode(object):
    def __init__(self,val = 0 , next =  None):
        self.val = val
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = ListNode(data)
node1 = ListNode(1)
head = node1
add(3)
print(next)
'''
class Solution(object):
    def mergetwo(self,l1:ListNode,l2:ListNode):
        node = ListNode(0)
        cur = node
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2

        return node.next
if __name__ == "__main__":
    l1 = ListNode()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l2 = ListNode()
    l2.append(1)
    l2.append(3)
    l2.append(4)
    sol = Solution()
    ans = sol.mergetwo(l1,l2)
    print(ans)'''