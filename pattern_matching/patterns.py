# Extract phone number and convert to integer
# https://www.youtube.com/watch?v=K8L6KVGG-7o
import re
text = [
'Frank,123 Main,925-555-1943,95122',
'Soumya, 7928 McCllelan Rd, 6506200809,95014'
]
for txt in text:
     ph = re.findall(r'[1-9][0-9]{2}[.-]?[0-9]{3}[.-]?[0-9]{4}', txt)
     print(ph)
     remove_delimeter = re.sub(r'[-.]', '', ph[0])
     print(remove_delimeter)
