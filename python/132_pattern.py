from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums)<3:
            return False
        min_val = (0, nums[0])
        max = smax = (-1, -10**9)
        for i in range(1,len(nums)-1):
            if nums[i] > max[1]:
              if i > max[0]:
                smax = max
              max = (i,nums[i])
            elif nums[i] > smax[1] and nums[i] != max[0]:
              smax = (i,nums[i])
            if nums[i] < min_val[1]:
              min_val = (i,nums[i])

        print(min_val)  
        print(max)  
        print(smax)  
        if min_val[0] < max[0] and min_val[0] < smax[0] and max[0] < smax[0]:
            return True
        else:
            return False
          

print(Solution().find132pattern([3,1,4,2]))