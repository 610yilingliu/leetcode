#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    leng = len(values)
    nums = 1
    while nums < leng:
             node = queue.popleft()
             if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    return root

class Solution:
    def distanceK(self, root, target, K):
        if root is None:
            return []
        allnodes = collections.defaultdict(list)
        def router(root):
            if root.left:
                allnodes[root.val].append(root.left.val)
                allnodes[root.left.val].append(root.val)
                router(root.left)
            if root.right:
                allnodes[root.val].append(root.right.val)
                allnodes[root.right.val].append(root.val)
                router(root.right)
        router(root)
        ans = []
        seem = set()
        def neighbours(val, time):
            if time == 0 and val not in seem:
                ans.append(val)
            else:
                if val not in seem:
                    seem.add(val)
                    for item in allnodes[val]:
                        neighbours(item, time - 1)
        neighbours(target, K)
        return ans

if __name__ == '__main__':
    a = construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    b = Solution()
    c = b.distanceK(a, 5, 2)
    print(c)
            
# @lc code=end

