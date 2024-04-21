# Bai 3
he = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()
    
if len(he) == 0:
    print("Dãy số trống.")
else:
    numbers = [float(num) for num in he]
    
if len(numbers) == 0:
    print("Không có số hợp lệ trong dãy số.")
else:  

    lon = max(numbers)
    nho = min(numbers)
    
print("Số lớn nhất là:", lon)
print("Số nhỏ nhất là:", nho)


