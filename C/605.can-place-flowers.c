/*
 * @lc app=leetcode id=605 lang=c
 *
 * [605] Can Place Flowers
 */

// @lc code=start


bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    int i = 0;
    int prev = 0;
    for(i = 0;i < flowerbedSize - 1; i ++){
        if(flowerbed[i] == 0 && prev == 0 && flowerbed[i + 1] == 0){
            prev = 1;
            n --;
            if(n == 0) return 1;
        }
        else{
            prev = flowerbed[i];
        }
    }
    if(flowerbed[i] == 0 && prev == 0){
        n--;
    }
    return n <= 0;
}

// @lc code=end

