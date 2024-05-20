### Bai 1
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes():
    twin_primes_list = []
    for i in range(2, 1000):
        if is_prime(i) and is_prime(i + 2):
            twin_primes_list.append((i, i + 2))
    return twin_primes_list

twin_primes_list = twin_primes()
print("Các số nguyên tố sinh đôi nhỏ hơn 1000 là:")
for pair in twin_primes_list:
    print(pair[0], "và", pair[1])
