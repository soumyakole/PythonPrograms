import sys
def find_longest_growing_sequence(values):
    longest_subsequence = []
    current_subsequence = []
    last_value = sys.maxsize
    for current_value in values:
        if current_value >= last_value:
            last_value = current_value
            current_subsequence.append(current_value)
        else:
            # end of this sequence, start new sequence
            if len(current_subsequence) >= len(longest_subsequence):
                longest_subsequence = current_subsequence
            current_subsequence = []
            last_value = current_value
            current_subsequence.append(current_value)
        print('current_value', current_value, 'last_value', last_value, 'current_subsequence', current_subsequence,
             'longest_subsequence', longest_subsequence)
    # important, because otherwise the last sequence might not be considered
    if len(current_subsequence) >= len(longest_subsequence):
        longest_subsequence = current_subsequence
    return longest_subsequence

print(find_longest_growing_sequence([7, 2, 7, 1, 2, 5, 7, 1]))