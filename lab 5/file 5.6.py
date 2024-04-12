# Bài 5
def havy(str1, str2):
    vy = ''
    vy2 = min(len(str1), len(str2))
    for i in range(vy2):
        vy += str1[i] + '-' + str2[i] + '-'
    if len(str1) > vy2:
        vy += str1[vy2:]
    elif len(str2) > vy2:
        vy += str2[vy2:]
    return vy
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
result = havy(str1, str2)
print("Chuỗi kết quả sau khi trộn:", result)


# Bài 6


