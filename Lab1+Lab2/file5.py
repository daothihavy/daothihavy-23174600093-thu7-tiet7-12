# Bài 5
a,b,c = map(int,input("Nhập vào hệ số của phương trình: ").split())
if a == 0: 
    if b == 0:
        if c == 0:
            print("Phương trình bậc nhất có vô số nghiệm")
        else:
            print("Phương trình bậc nhất vô nghiệm")
    else:
        x = -c/b
        print("Phương trình bậc nhất có nghiệm là x =", x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình bậc hai vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình bậc hai có nghiệm kép x1 = x2 =", x)
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print("Phương trình bậc hai có hai nghiệm phân biệt x1 = {} và x2 = {}".format(x1, x2))