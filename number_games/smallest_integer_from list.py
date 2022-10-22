import functools

test_list = [23, 65, 98, 3, 4]

#solution 1
from itertools import permutations
all_permutations = permutations(test_list)
lst = [''.join(map(str,t)) for t in all_permutations]
s = sorted(lst, key = lambda x: int(x))
print(s[0])

#solution 2
def key_gen(i, j):
    return -1 if int(str(j) + str(i)) > int(str(i) + str(j)) else 1

s = sorted(test_list, key = functools.cmp_to_key(key_gen))
print(int(''.join(map(str,s))))