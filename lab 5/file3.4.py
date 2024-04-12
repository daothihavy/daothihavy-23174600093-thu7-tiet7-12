# Bài 4
def vy3(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

vy2 = input("Nhập chuỗi ký tự: ")

vy = ''.join(char for char in vy2 if char.isdigit())

if vy:
    vy4 = int(vy)
    if vy3(vy4):
        print(f"Chuỗi '{vy}' là số nguyên tố.")
    else:
        print(f"Chuỗi '{vy}' không phải là số nguyên tố.")
else:
    print("Chuỗi không chứa số nguyên.")