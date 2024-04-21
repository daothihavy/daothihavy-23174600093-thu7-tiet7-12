# Bài 2
def kiem_tra_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def kiem_tra_so_hoan_hao(num):
    tong = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            tong += i
            if i != num // i:
                tong += num // i
    return tong == num


n = int(input("Nhập số lượng phần tử : "))
arr = []
for i in range(n):
        num = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr.append(num)
    
print("Các số nguyên tố là:")
for num in arr:
        if kiem_tra_nguyen_to(num):
            print(num, end=" ")
    
print("\nCác số hoàn hảo là:")
for num in arr:
        if kiem_tra_so_hoan_hao(num):
            print(num, end=" ")

