#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = dict()
        self.stack = []

    def get(self, key: int):
        if key not in self.d:
            return -1
        self.stack.remove(key)
        self.stack.append(key)
        return self.d[key]

    def put(self, key: int, value: int):
        if key in self.d:
            self.d[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if len(self.stack) >= self.cap:
                to_delete = self.stack[0]
                self.stack = self.stack[1:]
                del self.d[to_delete]
            self.d[key] = value
            self.stack.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

