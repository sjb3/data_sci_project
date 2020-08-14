# HackerRank Day 7: Arrays | Python

# def arr(arr):
#     result = []
#
#     for i in arr[:: -1]:
#         result.append(i)
#
#     print(result)

# OR

# def arr(arr):
#     result = []
#
#     for i in reversed(arr):
#         result.append(i)
#
#     print(result)

# OR

def arr(arr):
    result = []

    for i in range(len(arr)):
        result.append(arr[len(arr)-i-1])

    print('-'.join(el for el in result))


arr(['!ot', '^0', '0^', 'to!'])
