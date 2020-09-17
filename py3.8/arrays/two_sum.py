'''
Given a sorted array of integer, return the two numbers such that
they add up to a specific target.
You may assume that each input would have exactly one soution.
And you may not use the same element twice.
'''

A = [-2, 1, 2, 4, 7, 11]
target = 13

# 1, Brute force approcach
# Time complexity = O(n^2)
# Space complexity = constant(no auxillary data structure or store anything)


def two_sum_brute_force(A, target_val):
    # using double loop
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target_val:
                print(A[i], A[j])
                return True
    return False


# print(two_sum_brute_force(A, 20))

# 2. use hash table
# TIme complexity: O(n)
# Space complexity: O(n)

def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        # print(i, A[i], ht)
        # ht[target-A[i]] = A[i]
        if A[i] in ht:
            print(ht[A[i]], A[i])
            # print(i, A[i], ht[A[i]])
            return True
        else:
            ht[target-A[i]] = A[i]

    return ht


# print(two_sum_hash_table(A, 13))

# 3.
# Using the fact that this is sorted array

def two_sum(A, target):
    i = 0
    j = len(A)-1
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i] + A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:  # A[i] + A[j] > target:
            j -= 1
    return False


# As it's single looping, time complexity is O(n)
# also not using any storing auxillary data structure complexity is constant
print(two_sum(A, 20))
