# Bai 6
qw = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

def hai(ba):
    bon = ''
    for digit in ba:
        bon += qw[digit] + ' '
    return bon.strip()

while True:
    num = input("Nhập một số: ")

    if not num.isdigit():
        print("Vui lòng chỉ nhập số nguyên dương.")
        continue
    
    print("Số", num, "được viết bằng chữ là:", hai(num))

    cont = input("Bạn có muốn tiếp tục không? (c/k): ")
    if cont.lower() != 'c':
        break
    