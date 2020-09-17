# Binary Search in Python: Find First Entry in List with Duplicates

'''
Write a function that takes an array of  sorted integers and a key and
returns the index of the first occurence of that key from the array
'''

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 288]
target = 108


def find_simple(A, target):
    # for i in range(len(A)):
    #     if A[i] == target:
    #         return i
    # return None

    # OR

    for i in A:
        if i == target:
            return A.index(i)


print(find_simple(A, 108))
