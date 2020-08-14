'''
    Sample input: 6
    Sample output: 5(0,1,1,2,3,5)
'''

# def fibo(n):
#     if n == 1:
#         return 0
#     elif n <= 3:
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
# print(fibo(5))

# More efficient way using hash table

def fibo(n, calculated = {1:0, 2:1, 3:1}):
    if n in calculated:
        return calculated[n]

    calculated[n] = (fibo(n-1, calculated) + fibo(n-2, calculated))
    return calculated[n]

print(fibo(4))
