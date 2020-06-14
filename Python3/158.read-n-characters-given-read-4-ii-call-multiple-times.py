#
# @lc app=leetcode id=158 lang=python3
#
# [158] Read N Characters Given Read4 II - Call multiple times
#

# @lc code=start
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    head, tail, buffer = 0, 0, [''] * 4 ## 定义全局变量

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.head == self.tail: ## read4 的缓存区为空的时候
                self.head = 0
                self.tail = read4(self.buffer) ## 开始进缓存区
                if self.tail == 0:
                    break
            while i < n and self.head < self.tail:
                buf[i] = self.buffer[self.head] ## 读出缓存区的变量
                i += 1
                self.head += 1
        return i

        
# @lc code=end

