
# Bài 1
def tinh_tong_chan_le(arr):
    tong_chan = 0
    tong_le = 0
    for so in arr:
        if so % 2 == 0:
            tong_chan += so
        else:
            tong_le += so
    return tong_chan, tong_le
n = int(input("Nhập số lượng phần tử : "))
arr = []
for i in range(n):
        so = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr.append(so)
    
tong_chan, tong_le = tinh_tong_chan_le(arr)
    
print("Tổng của các số chẵn là:", tong_chan)
print("Tổng của các số lẻ là:", tong_le)


