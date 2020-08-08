#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (74.02%)
# Likes:    983
# Dislikes: 70
# Total Accepted:    80.1K
# Total Submissions: 102.9K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph):
        if not graph[0]:
            return []
        self.ans = []
        self.search_path(graph, 0, [0], {0})
        return self.ans
    
    def search_path(self, graph, curidx, curpath, walked):
        if curidx == len(graph) - 1:
            self.ans.append(curpath)
            return
        for node in graph[curidx]:
            if node not in walked:
                self.search_path(graph, node, curpath + [node], walked|{node})
# a = Solution()
# b = a.allPathsSourceTarget([[1,2], [3], [3], []])
# print(b)
# @lc code=end

