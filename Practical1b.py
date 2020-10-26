mat1 = [[1, 2], [3, 4]]
mat2 = [[1, 2], [3, 4]]
mat3 = [[0, 0], [0, 0]]

for i in range(0, 2):    
   for j in range(0, 2):       
       mat3[i][j] = mat1[i][j] + mat2[i][j]
       print("Addition of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
       print(mat3[i][j], end = "")
       print()

mat1 = [[7, 4], [6, 4]]
mat2 = [[8, 2], [4, 3]]
mat3 = [[0, 0], [0, 0]]

for i in range(0, 2):    
   for j in range(0, 2):       
       mat3[i][j] = mat1[i][j] - mat2[i][j]
       print("Subtraction of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
       print(mat3[i][j], end = "")
       print()

mat1 = [[7, 4], [6, 4]]
mat2 = [[8, 2], [4, 3]]
mat3 = [[0, 0], [0, 0]]

for i in range(0, 2):
   for j in range(0, 2):
       mat3[i][j] = mat1[i][j] * mat2[i][j]
       print("Multiplication of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
       print(mat3[i][j], end = "")
       print()
