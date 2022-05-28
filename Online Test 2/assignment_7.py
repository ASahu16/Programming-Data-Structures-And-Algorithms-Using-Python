pattern = input()
l = []
while True:
    a = input()
    if a == "":
      break
    l.append(a)
    
for i in l[::-1]:
    if i.find(pattern) != -1:
        print(i)
        break



