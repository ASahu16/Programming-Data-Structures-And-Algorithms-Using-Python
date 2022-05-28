from typing import List


def longestCommonPrefix( strs: List[str]) -> str:
    res = ""
    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            try:
                print( strs[0][i], strs[j][i])
                if strs[0][i] != strs[j][i]:
                    return res
            except IndexError:
                print(i,j)
                return res

        res += strs[0][i]
    return res

print(longestCommonPrefix(["flower","flow","flight"]))