#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#

# @lc code=start

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.nxt = None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.nxt == None:
            self.nxt = self.iter.next()
        return self.nxt

    def next(self):
        """
        :rtype: int
        """
        if self.nxt is not None:
            temp = self.nxt
            self.nxt = None
            return temp
        return self.iter.next()

        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nxt is not None:
            return True
        return self.iter.hasNext()

# @lc code=end

