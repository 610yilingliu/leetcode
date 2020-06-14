#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1, list2):
        if not list1 or not list2:
            return []
        both_like = set()
        d = dict()
        for i in range(len(list1)):
            d[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in d:
                both_like.add(list2[j])
                d[list2[j]] += j
        if not both_like:
            return []
        indexes = [val for key, val in d.items() if key in both_like]
        mi_index = min(indexes)
        answer = []
        for key, val in d.items():
            if val == mi_index and key in both_like:
                answer.append(key)
        return answer

if __name__ == '__main__':
    a = Solution()
    b = a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
    print(b)

# @lc code=end

