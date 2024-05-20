### Bai 3
### 1
def cubesum(n):
    digits = str(n)
    total = 0
    for digit in digits:
        total += int(digit) ** 3
    return total

number = int(input("Nhập số nguyên n: "))
result = cubesum(number)
print("Tổng của các lập phương của các chữ số riêng lẻ của", number, "là:", result)


###2
## A
def cubesum(n):
    digits = str(n)

    total = 0
    for digit in digits:
        total += int(digit) ** 3
    return total

def PrintArmstrong():
    print("Các số Armstrong là:")
    for num in range(1, 1001):

        if cubesum(num) == num:
            print(num)

PrintArmstrong()


## B
def cubesum(n):
    digits = str(n)
    total = 0

    for digit in digits:
        total += int(digit) ** 3
    return total

def isArmstrong(n):
    return cubesum(n) == n
number = int(input("Nhập một số nguyên n: "))
result = isArmstrong(number)
if result:
    print(number, "là số Armstrong.")
else:
    print(number, "không là số Armstrong.")

