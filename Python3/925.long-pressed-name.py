#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        check_queue = collections.deque(typed.split())
        lst = None
        for i in range(len(name)):
            if not check_queue and i < name - 1:
                return False
            if check_queue[0] == name[i]:
                lst = check_queue.popleft()
                while check_queue[0] == lst:
                    check_queue.popleft()
            else:
                if lst == name[i]:
                    continue
                else:
                    return False
        if check_queue:
            while check_queue and check_queue[0] == name[-1]:
                check_queue.popleft()
        return False if check_queue else True
        
# @lc code=end

