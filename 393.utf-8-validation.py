#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            #find number of 1's followed by 0
            num = data[i]
            n_byte = 0
            mask = 1 << 7
            while mask & num:
                n_byte += 1
                mask = mask >> 1
                
            if n_byte == 0:
                i += 1
                continue
            
            #10 is invalid(for starting byte), > than 4 bits is invalid
            if n_byte == 1 or n_byte > 4:
                return False
            
            # I need atleast n_byte - 1 more items atleast for valid utf
            n_byte -= 1
            # I need n_byte - 1 more items atleast
            # needed bytes are greater than remaining bytes
            if n_byte > (n-i-1):
                return False
            
            i += 1
            # now check for '10'
            mask1 = 1 << 7
            mask2 = 1 << 6
            while n_byte > 0:
                if not (data[i] & mask1 and not (data[i] & mask2)):
                    return False
                i += 1
                n_byte -= 1
        return True
# @lc code=end

