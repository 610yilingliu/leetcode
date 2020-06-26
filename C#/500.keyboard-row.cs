/*
 * @lc app=leetcode id=500 lang=csharp
 *
 * [500] Keyboard Row
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
public string[] FindWords(string[] words) 
{
	string[] rows = new string[]{ "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM" };
	int[] keyMasks = new int[rows.Length];

	for(int i = 0; i < rows.Length; i++)
	{
		int mask = 0;
		foreach(char c in rows[i])
		{
			mask |= (1 << (c - 'A'));
		}

		keyMasks[i] = mask;
	}

	List<string> result = new List<string>();
	foreach(var word in words)
	{
		bool isValid = false;            
		int mask = 0;

		foreach(char c in word)
		{                
			mask = mask | (1 << (char.ToUpper(c) - 'A'));
		}

		for(int i = 0; i < keyMasks.Length; i++)
		{
			if((keyMasks[i] & mask) == mask)
			{
				isValid = true;
				break;
			}
		}

		if(isValid)
		{
			result.Add(word);
		}
	}

	return result.ToArray();
}
}
// @lc code=end

