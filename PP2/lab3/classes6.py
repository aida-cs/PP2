is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

numbers = [10, 15, 3, 7, 19, 22, 29, 31]
print(list(filter(is_prime, numbers)))