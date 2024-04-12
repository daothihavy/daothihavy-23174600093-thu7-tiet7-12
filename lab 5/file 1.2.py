# Bài 1
def vy(n):
    if n == 0:
        return '0'
    vy2 = ''
    while n > 0:
        vy2 = str(n % 2) + vy2
        n //= 2
    return vy2
vy3 = int(input("Nhập số nguyên dương (số thập phân): "))
vy3 = vy(vy3)
print(f"Số nhị phân tương ứng là: {vy3}")


# Bài 2
def he(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    hehe = 0
    hehehe = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > hehe:
                    hehe = dp[i][j]
                    hehehe = i
            else:
                dp[i][j] = 0

    hem = hehehe - hehe
    return str1[hem:hehehe]
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")


hemm = he(str1, str2)

if hemm:
    print("Chuỗi con chung có độ dài ngắn nhất là:", hemm)
else:
    print("Không có chuỗi con chung.")

