import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if i*i < n:
                divisors.append(int(n/i))
    return sorted(divisors)

print(get_divisors(100))
