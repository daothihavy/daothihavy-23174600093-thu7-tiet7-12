# Bài 7
def havy(string):
    vy1 = 0
    vy2 = 0
    vy3 = 0
    vy4 = 0

    for char in string:
        if char.islower():
            vy1 += 1
        elif char.isupper():
            vy2 += 1
        elif char.isdigit():
            vy3 += 1
        else:
            vy4 += 1

    return vy1, vy2, vy3, vy4

def main():
    vy123 = input("Nhập chuỗi: ")
    vy1, vy2, vy3, vy4 = havy(vy123)

    print("Số lượng chữ thường:", vy1)
    print("Số lượng chữ hoa:", vy2)
    print("Số lượng chữ số:", vy3)
    print("Số lượng ký tự đặc biệt:", vy4)

if __name__ == "__main__":
    main()

