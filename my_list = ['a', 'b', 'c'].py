def isPrime(n, i = 2):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return isPrime(n, i + 1)

def sum_prime_in_range(x,y):
    num = list(range(x, y+1, 1)) 
    return sum(num)


def sum(num):
    if len(num) == 0:
        return 0
    else:
        if isPrime(num[0]):
            return num[0] + sum(num[1:])
        else:
            return sum(num[1:])

print(sum_prime_in_range(3,3))