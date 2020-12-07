#
# @lc app=leetcode id=536 lang=python3
#
# [536] Construct Binary Tree from String
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
            if not s:
                return None
            stack,number=[],''
            for c in s:
                if c in '()':
                    if c=='(' and number:
                        stack.append(TreeNode(number))
                        number=''
                    elif c==')':
                        if number:
                            node,parent=TreeNode(number),stack[-1]
                            number=''
                        else:
                            node,parent=stack.pop(),stack[-1]
                        if parent.left:
                            parent.right=node
                        else:
                            parent.left=node
                else:
                    number+=c
            if number:
                stack=[TreeNode(number)]
            return stack[0]
                


# @lc code=end

