#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator, denominator):
            if(numerator<0 and denominator<0):numerator,denominator=-numerator,-denominator
            u=(numerator<0)^(denominator<0)
            a=abs(numerator)
            b=abs(denominator)
            a=a%b
            if(a==0):return str(numerator//denominator)
            s=str(abs(numerator)//b)+'.'#计算整数部分
            q={}
            l=[]
            while(a<b):
                a=a*10
                l.append(a)
                q[a]=a//b
            a=a%b*10
            while(a not in q and a!=0):#a in q时表示已经有一段循环了，当前位置是循环的结尾
                l.append(a)        
                q[a]=a//b
                a=a%b
                a=a*10
            for i in range(0,len(l)):
                if(a==l[i]):s=s+'('
                s=s+str(q[l[i]])
            if('(' in s ):s=s+')'
            if(u):s='-'+s
            return s
                            
        
# @lc code=end

