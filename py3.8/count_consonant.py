# Algorithms in Python: Recursion -- Count Consonants in String

input_str_1 = 'abc de'
input_str_2 = 'LuCiDPrGrammINg'

vowel = 'aeiou'


def iterative_count_consonants(str):
    count = 0
    # for i in range(len(str)):
    #     if str[i].lower() not in vowel and str[i].isalpha():
    #         count += 1

    # OR

#     for i in str:
#         if i.lower() not in vowel and i.isalpha():
#             count += 1
#     return count


# print(iterative_count_consonants(input_str_1))

# def recursive_count_consonants(str):
#     if str == '':
#         return 0

#     if str[0].lower() not in vowel and str[0].isalpha():
#         return 1 + recursive_count_consonants(str[1:])
#     else:
#         return recursive_count_consonants(str[1:])


# print(recursive_count_consonants(input_str_2))
