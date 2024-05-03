# Bài 1
def tao_tu_dien(N):
    tu_dien = {}
    for x in range(1, N+1):
        tu_dien[x] = x ** 3
    return tu_dien

N = int(input("Nhập số nguyên N: "))
tu_dien = tao_tu_dien(N)
print("Từ điển:")
for key, value in tu_dien.items():
    print(f"{key}: {value}")



