### Bai 5
def sum_proper_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def are_amicable(num1, num2):
    return sum_proper_divisors(num1) == num2 and sum_proper_divisors(num2) == num1
number1 = int(input("Nhập số thứ nhất: "))
number2 = int(input("Nhập số thứ hai: "))

if are_amicable(number1, number2):
    print(number1, "và", number2, "là một cặp số amicable.")
else:
    print(number1, "và", number2, "không phải là một cặp số amicable.")
