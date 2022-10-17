def check_balance(in_str):
    stack = []
    paren_map = {')': '(',
                 '}': '{',
                 ']': '['}
    for c in in_str:
        if c in paren_map:
            if stack and paren_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        elif c in paren_map.values():
            stack.append(c)
        else:
            pass
    return len(stack) == 0

print(check_balance("{1}()"))