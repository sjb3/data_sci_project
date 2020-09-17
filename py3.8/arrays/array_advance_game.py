# Arrays in Python: Array Advance Game

'''
Given an array of non-negative integers
  e.i A = [3,3,1,0,2,0,1]
  Each number represents the maximum you can advance in the array

  logistics:
  1) from A[0] move 1 position to the right
  2) A[1] move 3 positions forward
  3) use A[4] till the end of the array

  if B = [3,2,0,0,2,0,1]
  => cannot adavance

'''


def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0

    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


A1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A1))

A2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A2))
