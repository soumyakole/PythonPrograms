# Extract phone number and convert to integer
# https://www.youtube.com/watch?v=K8L6KVGG-7o
import re
text = """Frank,123 Main,925-555-1943,95122
Soumya, 7928 McCllelan Rd, 6506200809,95014
"""
matches = re.finditer(r'[1-9][0-9]{2}[.|-]?[0-9]{3}[.-]?[0-9]{4}', text)
for match in matches:
    ph = match.group(0)
    print(ph, end=' ==> ')
    int_ph = re.sub(r'[-.]', '', ph)
    print(int_ph)

# for txt in text:
#      ph = re.findall(r'[1-9][0-9]{2}[.-]?[0-9]{3}[.-]?[0-9]{4}', txt)
#      print(ph)
#      remove_delimeter = re.sub(r'[-.]', '', ph[0])
#      print(remove_delimeter)

# text2 = [
#     'Mr Sk',
#     'Mr. Adri',
#     'Mrs K',
#     'Ms Aadriti'
# ]
# # for txt in text2:
# #     # initial = re.findall(r'M[r,s,.]+', txt)
# #     # print(initial)
# #     initial1 = re.findall(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', txt)
# #     print(initial1)

text3 ="""
Mr Sk
Mr. Adri
Mrs K
Ms Aadriti
"""

patern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = patern.finditer(text3)
for match in matches:
    print(match.group(0))
# print(re.findall(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', text3))
# print(patern.findall(text3))