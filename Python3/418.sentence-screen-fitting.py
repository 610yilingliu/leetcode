#
# @lc app=leetcode id=418 lang=python3
#
# [418] Sentence Screen Fitting
#

# @lc code=start
class Solution(object):
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        x = 0 
        y = 0 
        
        word = 0
        ans = 0
        
        for w in sentence:
            if len(w) > cols:
                return 0
        
        memo = {}
        
        while y < rows:
            x = 0
            
            start_word = word
            
			# If the given starting word is not in our cache, compute the results for it
			
            if (start_word not in memo):
			
                comp_flag = 0
				# Count the number of completed sentences on this line, and what the starting word on the next line will be
                while x < cols: 

                    diff = cols - x 
                    if (len(sentence[word]) > diff):
                        break
                    else:
                        x += (len(sentence[word])+1)
                        word += 1
                        word = word%len(sentence)
                        if (word == 0):
                            comp_flag += 1 
                            ans += 1
						# Cache the result
                        memo[start_word] = [word, comp_flag]
            else:
				# If the given word is in our cache, simply updated our answer with the # of completed sentences 
                word, com = memo[start_word] 
                ans += com
            y += 1
            
        return ans
# @lc code=end

