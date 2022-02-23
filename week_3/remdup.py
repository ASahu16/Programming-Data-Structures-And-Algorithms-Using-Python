def remdup(l):
  distinct_list = []  
  for i in range(len(l)):
    if l[i] not in distinct_list:
      distinct_list.append(l[i])
  return distinct_list