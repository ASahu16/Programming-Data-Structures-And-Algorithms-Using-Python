def remdup(l):
    return(myremdup(l,[]))

def myremdup(l,s):
    if l == []:
        return([])
    else:
        if l[0] in s:
            return(myremdup(l[1:],s))
        else:
            return([l[0]]+myremdup(l[1:],s+[l[0]]))

####################

def even(n):
    return(n%2 == 0)

def sumsquare(l):
    oddsum = 0
    evensum = 0
    for n in l:
        if even(n):
            evensum += n*n
        else:
            oddsum += n*n
    return([oddsum,evensum])

###################

def transpose(l):
  outl = []
  for row in l[:1]:
    for i in range(len(row)):
      outl.append([])
  for row in l:   
    for i in range(len(row)):
      outl[i].append(row[i])
  return(outl)

###################

import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "remdup":
  arg = parse(farg)
  print(remdup(arg))

if fname == "sumsquare":
  arg = parse(farg)
  print(sumsquare(arg))

if fname == "transpose":
  arg = parse(farg)
  savearg = arg
  ans = transpose(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")