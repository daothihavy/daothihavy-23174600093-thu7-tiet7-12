# Bai 5
def he(hehe):

    if len(hehe) <= 2:
        return True

    diff = hehe[1] - hehe[0]
    for i in range(1, len(hehe) - 1):
        if hehe[i + 1] - hehe[i] != diff:
            return False
    return True
try:
    hehe = input("Nhập dãy số, cách nhau bởi dấu phẩy: ").split(',')
    hehe = [int(num) for num in hehe]
except ValueError:
    print("Vui lòng nhập vào các số nguyên.")
else:
    if he(hehe):
        print("Dãy số", hehe, "tạo thành cấp số cộng.")
    else:
        print("Dãy số", hehe, "không tạo thành cấp số cộng.")
