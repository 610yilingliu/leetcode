#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
import collections

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        def levorder(root):
            if root is None:
                return []
            re = [str(root.val)]
            q = [root]
            while True:
                temp = []
                for node in q:
                    if node.left:
                        temp.append(node.left)
                        re.append(str(node.left.val))
                    if not node.left:
                        re.append('None')
                    if node.right:
                        temp.append(node.right)
                        re.append(str(node.right.val))
                    if not node.right:
                        re.append('None')
                if not temp:
                    return re
                q = temp
        ls = levorder(root)
        return '~'.join(ls)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split('~')
        tree = []
        for item in ls:
            if item == 'None':
                tree.append(None)
            else:
                tree.append(int(item))

        def generator(ls):
            if not ls:
                return
            r = TreeNode(ls[0])
            q = collections.deque([r])
            tree_len = len(ls)
            cnt = 1
            while cnt < tree_len:
                if not q:
                    break
                node = q.popleft()
                if node:
                    node.left = TreeNode(ls[cnt]) if ls[cnt] is not None else None
                    q.append(node.left)
                    if cnt + 1 < tree_len:
                        node.right = TreeNode(ls[cnt + 1]) if ls[cnt + 1] is not None else None
                        q.append(node.right)
                        cnt += 1
                    cnt += 1
            return r
        ans = generator(tree)
        return ans

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# re = codec.deserialize("1-2-3-None-None-4-5-None-None-None-None")
# print(re)
# @lc code=end

