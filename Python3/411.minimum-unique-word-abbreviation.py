#
# @lc app=leetcode id=411 lang=python3
#
# [411] Minimum Unique Word Abbreviation
#
import heapq
import collections
# @lc code=start
class Solution:
    def minAbbreviation(self, target, dictionary):
        if not target:
            return ''
        if not dictionary:
            return str(len(target))
        targets = self.finder(target)
        heap = []
        for item in targets:
            heapq.heappush(heap, (len(item), item))
        while heap:
            abbr = heapq.heappop(heap)[1]
            found = False
            for word in dictionary:
                if self.abbr_valid(abbr, word):
                    found = True
                    break
            if found == False:
                return abbr
        return ''

    def abbr_valid(self, abbr, word):
        word = collections.deque(word)
        i = 0
        while word and i < len(abbr):
            if abbr[i].isdigit():
                temp = abbr[i]
                while i + 1 < len(abbr) and abbr[i + 1].isdigit():
                    temp += abbr[i + 1]
                    i += 1
                time = int(temp)
                for _ in range(time):
                    if not word:
                        return False
                    word.popleft()
            else:
                if abbr[i] != word[0]:
                    return False
                word.popleft()
            i += 1
        if word or i < len(abbr):
            return False
        return True

    def finder(self, word):
        ans = ['']
        for i in range(len(word)):
            temp = []
            for item in ans:
                if item == '' or item[-1].isalpha():
                    temp.append(item + word[i])
                    temp.append(item + '1')
                else:
                    temp.append(item + word[i])
                    temp.append(item[: -1] + str(int(item[-1]) + 1))
            ans = temp
        return ans 

# @lc code=end

