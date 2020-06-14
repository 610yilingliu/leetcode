#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start

# it is also easy to use raw dict, but collection saves time
import collections

class Solution:
    def topKFrequent(self, words, k):
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # special condition
        if k == 0 or not words:
            return 0
        # start
        word_dic = collections.Counter(words)
        ans = []
        for key, val in word_dic.items():
            ans.append([val, key])
        ans.sort(key = lambda x: (-x[0], x[1]))
        res = [item[1] for item in ans[:k]]
        return res
# way to save time: write an extra function to get only top k values

if __name__ == '__main__':
    a = Solution()
    b = a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
    print(b)

# @lc code=end

