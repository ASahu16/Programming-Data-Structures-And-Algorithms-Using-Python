# Write a Python function sumsquare(l) that takes a nonempty list of integers 
# and returns a list [odd,even], 
# where odd is the sum of squares all the odd numbers in l 
# and even is the sum of squares of all the even numbers in l.

# Here are some examples to show how your function should work.

# >>> sumsquare([1,3,5])
# [35, 0]

# >>> sumsquare([2,4,6])
# [0, 56]

# >>> sumsquare([-1,-2,3,7])
# [59, 4]

# We have to write a function that will accept a list of some number
# And we will return some list containing odd,even
# here odd will be the sum of square of all the odd nubers in the list(l)
# AND here even will be the sum of square of all the even nubers in the list(l)

# We will take two variables sum_even and sum_odd that will contain the sum of all the respective numbers in the list.


# Travse the list:
#  if the element is even sum_even = sum_even + (element ka square)
#  else we know the number is odd so, sum_odd = sum_odd + (element ka square)
# After the traversal loop is over return the sum_odd, sum_even in the list.

def sumsquare(l):
  sum_even = sum_odd = 0
  for i in l:
    if i%2 == 0:
      sum_even = sum_even + (i**2)
    else:
      sum_odd = sum_odd + (i**2)
  
  return [sum_odd,sum_even]

print(sumsquare([1,3,5]))
print(sumsquare([2,4,6]))
print(sumsquare([-1,-2,3,7]))
