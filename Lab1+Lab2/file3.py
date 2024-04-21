#Bai 3
a,b,c = map(int, input("Nhập vào số đo tam giác cần kiểm tra: ").split())
if (a + b) > c and (a + c) > b and (b + c) > a: 
    if (a == b) and (a == c) and (b == c): 
        print("Đây là tam giác đều")
    elif (a == b) or (a == c) or (b == c):
        print("Đây là tam giác cân")
    elif (int(a**2 + b**2) == int(c**2)) or (int(a**2 + c**2) == int(b**2)) or (int(c**2 + b**2) == int(a**2)):
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là tam giác")