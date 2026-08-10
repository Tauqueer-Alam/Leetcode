from itertools import permutations
class Solution(object):

    def permute(self, nums):
        perm=[]
        for p in permutations(nums):
            perm.append(list(p))

        return perm    

        