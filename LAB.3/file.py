#Bài 1
#a
def tinh_tong(n):
    tong = n * (n + 1) // 2
    return tong
n = int(input("Nhập vào số nguyên n: "))
ket_qua = tinh_tong(n)
print(f"Tổng của dãy số từ 1 đến {n} là: {ket_qua}")


#Bài 2
#a
def tong():
    tong = 0
    for i in range(2000, 4001):
        if i % 7 == 0 and i % 5 != 0:
            tong += i
    return tong
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là:", tong())

#b
def tong():
    tong = 0
    for i in range(500, 1001):
        if i % 4 == 0 and i % 6 != 0:
            tong += i
    return tong

print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000 là:", tong())


#Bài 3
#b
def chinh_phuong(n):
    if n < 0:
        return False
    flag = False
    for i in range(1, n):
        if i * i == n:
            flag = True
            break
    return flag
def in_so_chinh_phuong():
    for i in range(1, 1001):
        if chinh_phuong(i):
            print(i, end=" ")
print("Các số chính phương từ 1 đến 1000 là:")
in_so_chinh_phuong()

#d
def kiem_tra_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def in_so_hoan_hao():
    for i in range(1, 500):
        if kiem_tra_so_hoan_hao(i):
            print(i, end=" ")
print("Các số hoàn hảo bé hơn 500 là:")
in_so_hoan_hao()

#e
def tinh_tong_so_ngu_giac(n):
    return (n * (3 * n - 1)) // 2
def tong_cac_so_ngu_giac():
    tong = 0
    for i in range(1, 201):
        tong += tinh_tong_so_ngu_giac(i)
    return tong
print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 là:", tong_cac_so_ngu_giac())

#Bài 4
#Hình 1
def ve_hinh_thoi(kich_thuoc):
    for i in range(1, kich_thuoc + 1):
        print(" " * (kich_thuoc - i) + "*" * (2 * i - 1))
    for i in range(kich_thuoc - 1, 0, -1):
        print(" " * (kich_thuoc - i) + "*" * (2 * i - 1))
kich_thuoc = int(input("Nhập kích thước của hình thoi: "))
ve_hinh_thoi(kich_thuoc)

#Hình 2
def ve_muoi_ten(chieu_dai, chieu_rong):
    for i in range(1, chieu_dai + 1):
        print(" " * (chieu_dai - i) + "*" * (2 * i - 1))
    for _ in range(chieu_rong):
        print(" " * (chieu_dai - chieu_rong) + "*" * (2 * chieu_rong - 1))
chieu_dai = int(input("Nhập chiều dài của mũi tên: "))
chieu_rong = int(input("Nhập chiều rộng của cán mũi tên: "))
ve_muoi_ten(chieu_dai, chieu_rong)