#
# @lc app=leetcode id=609 lang=python3
#
# [609] Find Duplicate File in System
#

# @lc code=start
class Solution:
    def findDuplicate(self, paths):
        if not paths:
            return []
        contents = dict()
        for item in paths:
            # don't need to split by '/', simply split by ' ', that is all I need to do!!!!
            base = item.split('/')
            files = base[-1].split(' ')
            base[-1] = files[0]
            # after that, base become ["root", "a"]
            files = files[1:]
            for f in files:
                # file name and content, name:f_c[0], content:f_c[1]
                f_c = f.split('(')
                if f_c[1] not in contents:
                    contents[f_c[1]] = ["/".join(base) + '/' + f_c[0]]
                else:
                    contents[f_c[1]].append("/".join(base) + '/' + f_c[0])
        ans = []
        for key in contents:
            if len(contents[key]) > 1:
                ans.append(contents[key])
        return ans

                


if __name__ == '__main__':
    a = Solution()
    b = a.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
    print(b)
# @lc code=end

