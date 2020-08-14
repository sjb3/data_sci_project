import itertools

word = 'sample'
given = '_plmeas_'

permu = itertools.permutations(given, len(word))

# ans = [answer for answer in permu if ''.join(answer) == word]

print([answer for answer in permu])
# for answer in permu:
#   print(answer)
  # if ''.join(answer) == word:
  #   print('Match!')
  #   print(answer)
  #   break
  # else:
  #   print('No Match')
