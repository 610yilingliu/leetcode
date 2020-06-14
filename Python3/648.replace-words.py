#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
# time: O(nm)
class Solution:
    def replaceWords(self, dict, sentence):
    # def replaceWords(self, dict: List[str], sentence: str) -> str:
        # special conditions
        if not dict:
            return sentence
        if not sentence:
            return ""
        # start
        sentence = sentence.split(' ')
        d = set(dict)
        for i in range(len(sentence)):
            for j in range(len(sentence[i])):
                if sentence[i][:j] in d:
                    sentence[i] = sentence[i][:j]
        return " ".join(sentence)

if __name__ == '__main__':
    a = Solution()
    b = a.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
    print(b)

# @lc code=end

