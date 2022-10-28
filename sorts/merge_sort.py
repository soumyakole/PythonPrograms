def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        midpoint = len(array)//2
        return merge(merge_sort(array[:midpoint]),
                     merge_sort(array[midpoint:]))

def merge(left, right):
    print("************")
    print('left', left)
    print('right', right)
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

print(merge_sort([2,3,1,4,6,7]))