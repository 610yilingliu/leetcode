#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        count = 0
        store = []
        def generator(node, count):
            if not node:
                return
            if count >= len(store):
                store.append([])
            store[count].append(node)
            if node.left:
                generator(node.left, count + 1)
            if node.right:
                generator(node.right, count + 1)
        generator(root, count)
        for item in store:
            for i in range(len(item) - 1):
                item[i].next = item[i + 1]
            item[-1].next = None
        return store[0][0]
# @lc code=end

