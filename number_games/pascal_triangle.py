# https://www.youtube.com/watch?v=nPVEaB3AjUM

def pascal_triangle(depth):
    result =[[1]]
    for d in range(depth-1):
        prev_row = [0] + result[-1] + [0]
        row = []
        for n in range(len(result[-1]) +1):
            row.append(prev_row[n] + prev_row[n+1])
        result.append(row)
    return result


print(pascal_triangle(5))