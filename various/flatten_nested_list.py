from collections.abc import Iterable

print(isinstance(1, Iterable))

def flatten(lst):
    print(f"flatten called with {lst}")
    for i in lst:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from flatten(i)
        else:
            yield i

ls = [1, [2, 3], [4, [5, 6]], [7, [8, [9, 10]]]]
print(list(flatten(ls)))

ls1=[[1,2],[3,4],[5,6]]
for l in ls1:
    for i in l:
        print(i)
print([i for l in ls1 for i in l])