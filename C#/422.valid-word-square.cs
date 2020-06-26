/*
 * @lc app=leetcode id=422 lang=csharp
 *
 * [422] Valid Word Square
 */

// @lc code=start
public class Solution {
    public bool ValidWordSquare(IList<string> words) {
        int ll = words.Count;
        for(int i = 0; i < ll; i ++){
            string curword = words[i];
            for(int j = 0; j < curword.Length ; j++){
                try{
                    if(curword[j] != words[j][i])
                        return false;
                    }
                catch{
                    return false;
                }
            }
        }
        return true;
    }
}
// @lc code=end

