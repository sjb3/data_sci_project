'''
  Given: an array of non-negative digits that represent a decimal int
  Problem: add one to the int.  Assume the solution still works
  even if implemented in a language with finite-precision arithmetic

  also: add 1 to the rightmost digit
      -> propagate carry throughout array
'''

A = [1, 4, 9]
B = [9, 9, 9]

# simple way
# s = ''.join(map(str, A))
# print(s)
# new_s = str(int(s) + 1)
# print(new_s)
# print([i for i in new_s])


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(B))
