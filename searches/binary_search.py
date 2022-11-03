def recursive_binary(lst, key, start, end):
    if start > end:
        return -1
    else:
        mid = (start + end)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
        # print(start, end, mid, lst[mid])
        return recursive_binary(lst, key, start, end)


def binary_search(lst, key):
    l, r = 0, len(lst)-1
    while r >= l:
        mid = (l + r)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__== "__main__":
    lst = [1,3,5,7,8,11,12]
    print(recursive_binary(lst, 12, 0, len(lst)-1))
    print(binary_search(lst, 12))
