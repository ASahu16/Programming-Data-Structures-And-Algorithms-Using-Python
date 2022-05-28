
def romanToInt(s: str) -> int:
        symbols = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        sum = 0
        for i in range(len(s)-1,-1,-1):
          try:
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X') :
              sum -= symbols[s[i]]
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C') :
              sum -= symbols[s[i]]
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M') :
              sum -= symbols[s[i]]
            else:  
              sum += symbols[s[i]]
          except:
              sum += symbols[s[i]]
        print(sum)

romanToInt('MCMXCIV')