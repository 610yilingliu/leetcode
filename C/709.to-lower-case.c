/*
 * @lc app=leetcode id=709 lang=c
 *
 * [709] To Lower Case
 */

// @lc code=start


char * toLowerCase(char * str){
    int l = strlen(str);
    for(int i = 0; i < l; i ++){
        if(str[i] >= 65 && str[i] <= 90){
            str[i] += 32;
        }
    }
    return str;
}
// @lc code=end

