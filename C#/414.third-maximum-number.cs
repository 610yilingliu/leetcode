/*
 * @lc app=leetcode id=414 lang=csharp
 *
 * [414] Third Maximum Number
 */

// @lc code=start
using System.Collections.Generic;	 
public class Solution {

	   public int ThirdMax(int[] nums) {
				int max1 = int.MinValue, max2 = int.MinValue, max3 = int.MinValue;

				bool firstMaxFound = false;
				bool thirdMaxFound = false;
				bool secondMaxFound = false;

				for (int i = 0; i < nums.Length; i++) {
					if ((firstMaxFound && nums[i] == max1) ||
						(secondMaxFound && nums[i] == max2)) continue;

					if (nums[i] >= max1) { // max1 < nums[i]
						max3 = max2;
						max2 = max1;
						max1 = nums[i];

						if (secondMaxFound) thirdMaxFound = true;
						if (firstMaxFound) secondMaxFound = true;

						firstMaxFound = true;

					} else if (nums[i] >= max2) { // max2 < nums[i] < max1
						max3 = max2;
						max2 = nums[i];

						if (secondMaxFound) thirdMaxFound = true;

						secondMaxFound = true;

					} else if (nums[i] >= max3) { // max3 < nums[i] < max2
						max3 = nums[i];
						thirdMaxFound = true;
					}
				}

				return thirdMaxFound ? max3 : max1;
			}

}
// @lc code=end

