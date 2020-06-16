#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and self.checkIPv4(IP):
            return "IPv4"
        elif ':' in IP and self.checkIPv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def checkIPv4(self, IP):
        numbers = IP.split('.')
        if len(numbers) != 4: return False
        for num in numbers:
            if not num or (not num.isdecimal()) or (num[0] == '0' and len(num) != 1) or int(num) > 255:
                return False
        return True

    def checkIPv6(self, IP):
        IP = IP.lower()
        valid16 = "0123456789abcdef"
        if "::" in IP: return False
        numbers = IP.split(':')
        if len(numbers) > 8: return False
        for num in numbers:
            if not num: continue
            if len(num) >= 5: return False
            for n in num:
                if n not in valid16:
                    return False
        return True

# @lc code=end

