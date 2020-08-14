# Algorithms in Python: Recursion -- Calculate String Length

input = 'aslfdhldfnal;ksfhqoifhqlknd'


def calc_str_length(str):
    if str == '':
        return 0

    return 1 + calc_str_length(str[1:])


print(len(input))
print(calc_str_length(input))
