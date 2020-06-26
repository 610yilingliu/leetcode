/*
 * @lc app=leetcode id=443 lang=csharp
 *
 * [443] String Compression
 */

// @lc code=start
// public class Solution {
//         public int Compress(char[] chars) {
//             if(chars == null) return 0;
//             if(chars.Length == 1) return 1;
//             curchar = chars[0];
//             curpos = 0;
//             dup_counter = 1;
//             chars = chars;
//             for(int i = 1; i < chars.Length; i ++)
//             {
//                 if(chars[i] == chars[i - 1] && i < chars.Length - 1){
//                     dup_counter ++;
//                 }
//                 else{
//                     if(i == chars.Length - 1){
//                         if(chars[i] == chars[i - 1]){
//                             dup_counter ++;
//                         }
//                         else{
//                             chars[curpos] = curchar;
//                             curpos ++;
//                             chars[curpos] = chars[i];
//                             curpos ++;
//                             return curpos;
//                         }
//                     }
//                     if(dup_counter == 1){
//                         chars[curpos] = curchar;
//                         curpos += 1;
//                         curchar = chars[i];
//                     }
//                     else{
//                         chars[curpos] = curchar;
//                         curpos ++;
//                         string tmps = "";
//                         while(dup_counter > 0){
//                             int res = dup_counter % 10;
//                             tmps = res.ToString() + tmps;
//                             dup_counter = dup_counter / 10;
//                         }
//                         foreach(char c in tmps){
//                             chars[curpos] = c;
//                             curpos ++;
//                         }
//                         dup_counter = 1;
//                         curchar = chars[i];
//                     }
//                 }
//             }
//             return curpos;
//         }
// }


public class Solution {
public int Compress(char[] chars) {
        if(chars == null) return 0;
        if(chars.Length == 1) return 1;
        int curpos = 0;
        int dup_counter = 1;
        char prechar = chars[0];
        for(int i = 1; i < chars.Length; i ++){
            if(chars[i] == chars[i - 1]){
                if(i == chars.Length - 1){
                    dup_counter ++;
                    set_time(chars, ref curpos, ref dup_counter, ref prechar);
                }
                else{
                    dup_counter ++;
                }
            }
            else{
                if(i == chars.Length - 1){
                    set_time(chars, ref curpos, ref dup_counter, ref prechar);
                    chars[curpos] = chars[i];
                    curpos ++;
                }
                else{
                    set_time(chars, ref curpos, ref dup_counter, ref prechar);
                    prechar = chars[i];
                }
            }
        }
        return curpos;

    }
    public void set_time(char[] chars, ref int curpos, ref int dup_counter, ref char prechar){
        if(dup_counter == 1){
            chars[curpos] = prechar;
            curpos ++;
        }
        else{
            chars[curpos] = prechar;
            curpos ++;
            string tmpstr = "";
            while(dup_counter > 0){
                int res = dup_counter % 10;
                dup_counter = dup_counter / 10;
                tmpstr = res.ToString() + tmpstr;
            }
            foreach(char c in tmpstr){
                chars[curpos] = c;
                curpos ++;
            }
            dup_counter = 1;
        }
    }

}

// @lc code=end