### Bai 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    return factorial(n) / factorial(n - r)

def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

n = int(input("Nhập số phần tử n: "))
r = int(input("Nhập số phần tử lấy mỗi lần r: "))

if n < r:
    print("Lỗi: Số phần tử n phải lớn hơn hoặc bằng số phần tử lấy mỗi lần r.")
else:
    print("Số hoán vị của", n, "phần tử lấy", r, "phần tử mỗi lần là:", permutations(n, r))
    print("Số tổ hợp của", n, "phần tử lấy", r, "phần tử mỗi lần là:", combinations(n, r))
