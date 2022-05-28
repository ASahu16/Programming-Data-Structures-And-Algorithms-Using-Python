from itertools import permutations
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(list(permutations(nums)))

print(Solution().permuteUnique([1,1,2])) 
        
