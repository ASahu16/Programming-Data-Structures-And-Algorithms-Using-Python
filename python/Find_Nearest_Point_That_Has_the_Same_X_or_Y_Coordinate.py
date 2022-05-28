def nearestValidPoint( x, y, points):
  distance = -1
  result = -1
  for idx,item in enumerate(points):
    if x != item[0] and y != item[1]:
      continue
    else:
      if( abs(x-item[0])+abs(y-item[1]) < distance or distance == -1):
        distance = abs(x-item[0])+abs(y-item[1])
        result = idx
        
  return result

print(nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))
