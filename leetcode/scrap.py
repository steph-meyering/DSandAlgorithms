def move_zeros_to_left(A):
  offset = 0
  for i in range(len(A)-1, -1, -1):
    if A[i] == 0:
      offset += 1
    else:
      A[i + offset] = A[i]
  for i in range(offset):
    A[i] = 0
  return A


print(move_zeros_to_left([0,1,0]))
