class Node:
    def __init__(self,val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.cargo)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3


def helper(ln, ls):
    ls.append(ln.val)
    if ln.next:
        return helper(ln.next, ls)
    return ls

node1
print(helper(node1, []))