# Bài 5
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def tinh_hoa_don(mua_hang):
    hoa_don = {}
    tong_tien = 0
    for mat_hang, so_luong in mua_hang.items():
        don_gia = gia_tien[mat_hang]
        thanh_tien = don_gia * so_luong
        tong_tien += thanh_tien
        hoa_don[mat_hang] = {
            'so_luong': so_luong,
            'don_gia': don_gia,
            'thanh_tien': thanh_tien
        }
    hoa_don['tong_tien'] = tong_tien
    return hoa_don


def in_hoa_don(hoa_don):
    print("Hóa đơn mua hàng:")
    for mat_hang, thong_tin in hoa_don.items():
        if mat_hang != 'tong_tien':
            print(f"Mặt hàng: {mat_hang}")
            print(f"Số lượng: {thong_tin['so_luong']}")
            print(f"Đơn giá: {thong_tin['don_gia']}")
            print(f"Số tiền: {thong_tin['thanh_tien']}")
            print()
    print(f"Tổng số tiền của hóa đơn: {hoa_don['tong_tien']}")


def cap_nhat_kho(mua_hang):
    for mat_hang, so_luong in mua_hang.items():
        kho[mat_hang] -= so_luong

mua_hang = {"banana": 2, "apple": 3, "orange": 1, "pear": 2}

hoa_don = tinh_hoa_don(mua_hang)
in_hoa_don(hoa_don)

cap_nhat_kho(mua_hang)

print("\nSố lượng của các mặt hàng trong kho sau khi mua hàng:")
print(kho)
