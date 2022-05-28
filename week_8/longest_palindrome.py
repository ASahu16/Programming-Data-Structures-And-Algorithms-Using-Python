# As we all know, a palindrome is a word that equals its reverse. 
# Here are some examples of palindromes: malayalam, gag, appa, amma.

# We consider any sequence consisting of the letters of the English alphabet to be a word. 
# So axxb,abbba and bbbccddx are words for our purpose. And aaabbaaa, abbba and bbb are examples of palindromes.

# By a subword of a word, we mean a contiguous subsequence of the word. 
# For example the subwords of the word abbba are a, b, ab, bb, ba, abb, bbb, bba, abbb, bbba and abbba.

# In this task you will given a word and you must find the longest subword of this word that is also a palindrome.

# For example if the given word is abbba then the answer is abbba. 
# If the given word is abcbcabbacba then the answer is bcabbacb.



def is_palindrome(s):
  if s == s[::-1]:
    return True
  return False

def longest_palindrome(s,n):
  max_length = -1
  max_palindrome = ""
  for i in range(n):
    for j in range(i, n):
      subword = s[i:j+1]
      if max_length != -1 and len(subword)<max_length:
        continue
      if is_palindrome(subword) and len(subword)>max_length:
        max_palindrome = subword
        max_length = len(subword)
  
  return (max_length,max_palindrome)

n = int(input())
s = input()
(max_length,max_palindrome) = longest_palindrome(s,n)
print(max_length)
print(max_palindrome)


   
