from typing import List


def findUnsortedSubarray(nums: List[int]) -> int:
    if not nums:
        return 0
    srt = nums[:]
    nums.sort()
    min = -1
    max = -1
    l = len(nums)
    for i in range(l):
      if min == -1 and nums[i] != srt[i]:
        min = i
      
      if max == -1 and nums[-(i+1)] != srt[-(i+1)]:
        max = l-(i+1)
      
      if max != -1 and min != -1:
        return max - min + 1
        
    return 0

print(findUnsortedSubarray([2,6,4,8,10,9,15]))
print(findUnsortedSubarray([1,2,3,4]))
print(findUnsortedSubarray([2,1]))