#
# @lc app=leetcode id=444 lang=python3
#
# [444] Sequence Reconstruction
#
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        size = len(org)
        indeg = [0] * size
        sucset = [set() for x in range(size)]
        if not seqs: return False
        for seq in seqs:
            if any(s > size or s < 1 for s in seq):
                return False
            for i in range(1, len(seq)):
                if seq[i] not in sucset[seq[i - 1] - 1]:
                    indeg[seq[i] - 1] += 1
                    sucset[seq[i - 1] - 1].add(seq[i])

        q = [i for i in org if not indeg[i - 1]]
        for x in range(size):
            if len(q) != 1 or q[0] != org[x]:
                return False
            nq = []
            for suc in sucset[q[0] - 1]:
                indeg[suc - 1] -= 1
                if not indeg[suc - 1]:
                    nq.append(suc)
            q = nq
        return True
            
a = Solution()
b = a.sequenceReconstruction([4,1,5,2,6,3],[[5,2,6,3],[4,1,5,2]])
print(b)
        
# @lc code=end

