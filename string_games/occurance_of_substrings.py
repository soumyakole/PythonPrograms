"""
Number of  occurances
"""


#Built-in method
print("hellohe".count("he"))


#Implementation-1
def count_substrings(text, value_to_find, allow_overlap=False):
    # recursive termination
    count = 0
    if len(text) < len(value_to_find):
        return count
    remaining = ""
    # does the text start with the search string?
    if text.startswith(value_to_find):
        # match: continue the search for the found
        # term after the location where it was found
        if allow_overlap:
            remaining = text[1:]
        else:
            remaining = text[len(value_to_find):]
        count = 1
    else:
        # remove first character and search again
        remaining = text[1:]
    # recursive descent
    return count_substrings(remaining, value_to_find, allow_overlap) + count

print(count_substrings("hellohe", "he"))
print(count_substrings("xxxx", "xx", allow_overlap=True))
print(count_substrings("xxxx", "xxt", allow_overlap=True))

def count_substrings_loop(text: str, value_to_find: str):
    count = 0
    increment = 0
    if len(value_to_find) > len(text):
        return 0
    else:
        for p, l in enumerate(text):
            if text[increment:].startswith(value_to_find):
                increment = increment+len(value_to_find)
                count +=1
            else:
                increment +=1
    return count
print(count_substrings_loop("xxxxaa", "aa"))
