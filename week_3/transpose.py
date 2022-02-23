def transpose(m):
  row = len(m)
  column = len(m[0])
  transposed_matrix = []
  for i in range(column):
    temp = []
    for j in range(row):
      temp.append(m[j][i])
    transposed_matrix.append(temp[:])
    temp.clear()
  return transposed_matrix

