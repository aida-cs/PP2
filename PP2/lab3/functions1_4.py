def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

print(filter_prime([10, 15, 3, 7, 19, 22, 29]))