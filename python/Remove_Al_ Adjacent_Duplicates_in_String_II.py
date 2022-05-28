from itertools import count


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        counter = 1
        l = len(s)
        while i < l - 1:
          if s[i] == s[i+1]:
            counter += 1
          else:
            counter = 1
          i += 1
          if counter == k:
            s = s[:i-counter+1] + s[i+1:]
            counter = 1
            l = len(s)
            i =  0
        return s  


# print(Solution().removeDuplicates("abcd",2))
print(Solution().removeDuplicates("deeedbbcccbdaa",3))