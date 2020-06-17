using System.Collections;
using System.Collections.Generic;

namespace debugging
{
    class Program
    {
        public bool IsPalindrome(int x) {
            string x_s = x.ToString();
            int l = 0;
            int r = x_s.Length;
            while(l < r){
                if(x_s[l] != x_s[r]) return false;
                l ++;
                r --;
            }
            return true;
        }
        static void Main(string[] args)
        {
            var a = new Program();
            int b = 121;
            var ans = a.IsPalindrome(b);
            System.Console.Write(ans);
            
        }
    }
}
