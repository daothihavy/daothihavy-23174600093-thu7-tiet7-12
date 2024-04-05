# Bai 3
vy1 = int(input("Nhập vào một số nguyên: "))
vy2 = 0

if vy1 == 0:
    vy2 = 1
else:
    while vy1 != 0:
        vy2 += 1
        vy1 //= 10

print("Số chữ số của số nguyên là:", vy2)


# Bai 4
#A

n = int(input("Nhập số nguyên n (> 10): "))

while n <= 10:
    print("Số n phải lớn hơn 10. Vui lòng nhập lại.")
    n = int(input("Nhập số nguyên n (> 10): "))
a = 1
S1 = 6
ban = 6

while ban <= n:
    print("S", a, "=", ban)
    a += 1
    S1 *= 6
    ban += S1

#B
n = int(input("Nhập số nguyên n (> 10): "))
while n <= 10:
    print("Số n phải lớn hơn 10. Vui lòng nhập lại.")
    n = int(input("Nhập số nguyên n (> 10): "))
a = 1
bon = -1
S2 = 0

while a <= n:
    S2 += bon * a ** 2
    print("S", a, "=", S2)
    a += 1
    bon *= -1


#C
n = int(input("Nhập số nguyên n (> 10): "))
while n <= 10:
    print("Số n phải lớn hơn 10. Vui lòng nhập lại.")
    n = int(input("Nhập số nguyên n (> 10): "))
a = 1
S3 = 0
while a <= n:
    S3 += a * (a + 1) * (a + 2)
    print("S", a, "=", S3)
    a += 1


