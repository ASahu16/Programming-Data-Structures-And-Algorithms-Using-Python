def count_odds(low:int, high:int) -> int:
  
  return (high + 1)//2 - (low)//2

print(count_odds(3,7))
print(count_odds(0,10))
print(count_odds(2,2))

