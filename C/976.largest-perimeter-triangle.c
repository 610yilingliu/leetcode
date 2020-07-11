/*
 * @lc app=leetcode id=976 lang=c
 *
 * [976] Largest Perimeter Triangle
 */

// @lc code=start

int cmp(int * a, int * b){
    return *(int *)b - *(int*)a;
}

int largestPerimeter(int* A, int ASize){
    qsort(A, ASize, sizeof(A[0]), cmp);
    for(int i = 0; i < ASize - 2; i ++){
         if(A[i]<A[i+1]+A[i+2]){
            return A[i]+A[i+1]+A[i+2];
         }
    }
    return 0;
}


// @lc code=end

