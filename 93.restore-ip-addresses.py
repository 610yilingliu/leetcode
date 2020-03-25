#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s):
        # ip address range from 0.0.0.1 to 255.255.255.255
        if len(s) < 4 or len(s) > 12:
            return []
        self.ans = []
        self.helper(s, "", 0)
        return self.ans

    def helper(self, s, string, count):
        if len(s) == 0 and count == 4:
            self.ans.append(string)
            # if somethings like 1.1.1.1 + ? or 1.1.1.1 + "111" happend
        if count > 3 or len(s) == 0:
            return
        for i in range(1,4):
            if i > len(s):
                continue
            substr = s[:i]
            # # check length
            if len(substr) > (4-count) * 3:
                return
            # each field should belong to interval[0, 255].Things like 00, 01 is not valid
            if int(substr) > 255:
                return
            if int(substr) > 0 and substr[0] == '0':
                return
            if int(substr) == 0 and len(substr) > 1:
                return
            if count ==  3:
                self.helper(s[i:], string + substr, count + 1)
            else:
                self.helper(s[i:], string + substr + '.', count + 1)
                
                

                
    
# @lc code=end

