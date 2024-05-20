### Bai 4
def sumPdivisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:

            total += i
            if i != n // i:
                total += n // i

    total -= n
    return total
number = int(input("Nhập một số nguyên n: "))
result = sumPdivisors(number)
print("Tổng của các ước số chính của", number, "là:", result)
