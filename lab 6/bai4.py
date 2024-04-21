# Bai 4

# # # Phan A
def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    hihi = [0, 1]

    [hihi.append(hihi[-1] + hihi[-2]) for _ in range(2, n)]
    return hihi
n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))
hoho = fibonacci(n)
print("Danh sách", n, "số Fibonacci đầu tiên là:", hoho)




# # # Phan B
def hihi(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
hehe = [num for num in range(2, 100) if hihi(num)]
print("Danh sách các số nguyên tố nhỏ hơn 100 là:", hehe)

