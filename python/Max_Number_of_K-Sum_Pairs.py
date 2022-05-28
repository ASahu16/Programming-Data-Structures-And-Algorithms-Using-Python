from typing import List
from collections import Counter


def maxOperations( nums: List[int], k: int) -> int:
        if not nums:
            return 
        cnt, ans = Counter(n for n in nums if n < k), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2

print(maxOperations([3,1,3,4,3],6))
# print(Counter([3,1,3,4,3]))