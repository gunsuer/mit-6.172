import sys, random
from time import *

n = 128

A = [[random.random()
      for row in range(n)]
      for column in range(n)]

B = [[random.random()
      for row in range(n)]
      for column in range(n)]

C = [[0
      for row in range(n)]
      for column in range(n)]

start = time()
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] = A[i][k] * B[k][j]

end = time()
print(end-start)