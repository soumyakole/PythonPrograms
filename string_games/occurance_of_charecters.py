from collections import defaultdict
def occurance_of_charecters(in_str):
    char_count = defaultdict(int)
    for c in in_str:
        char_count[c.lower()] += 1
    print(dict(char_count))

occurance_of_charecters('Soumyabratas')

#using Counter
from collections import Counter
def occurance_of_charecters2(in_str):
    c = Counter(in_str.lower())
    print(dict(c))
occurance_of_charecters2('Soumyabratas')
