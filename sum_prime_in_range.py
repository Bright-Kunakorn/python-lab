def isPrime(n, i = 2):
    # Return False if n is less than 2
    if (n <= 2):
        return True if(n == 2) else False
    # Return False if n is divisible by i
    if (n % i == 0):
        return False
    # Return True if i*i is greater than n
    if (i * i > n):
        return True
    # Recursively check the next value of i
    return isPrime(n, i + 1)

def sum_prime_in_range(x, y):
    # Create a list of numbers from x to y, inclusive
    num = list(range(x, y+1, 1)) 
    # Return the sum of the prime numbers in the list
    return sum(num)

# This function calculates the sum of the elements in a list
def sum(num):
    # If the list is empty, return 0
    if len(num) == 0:
        return 0
    # If the first element is prime, add it to the sum of the rest of the list
    elif isPrime(num[0]):
        return num[0] + sum(num[1:])
    # If the first element is not prime, ignore it and calculate the sum of the rest of the list
    else:
        return sum(num[1:])

# Test the sum_prime_in_range function
print(sum_prime_in_range(3,3))
