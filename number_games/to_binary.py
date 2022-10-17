def to_bin(num):
    l = len(num) - 1
    val = 0
    for c in num:
        val = val + (int(c) * (2 ** l))
        l -= 1
    print(val)
to_bin("101")