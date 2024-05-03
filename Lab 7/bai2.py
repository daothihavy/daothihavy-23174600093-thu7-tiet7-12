# Bài 2
def xep_loai_diem(diem):
    if diem < 4.0:
        return 'F'
    elif diem < 5.5:
        return 'D'
    elif diem < 7.0:
        return 'C'
    elif diem < 8.5:
        return 'B'
    else:
        return 'A'

def thong_ke_loai_hoc_luc(sinh_vien):
    loai_hoc_luc = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for sv in sinh_vien:
        loai = xep_loai_diem(sv['diem'])
        loai_hoc_luc[loai] += 1
    return loai_hoc_luc

sinh_vien = []
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên {i}: ")
    diem = float(input(f"Nhập điểm của sinh viên {i}: "))
    sinh_vien.append({'ten': ten, 'diem': diem})

print("Xếp loại học lực của sinh viên:")
for sv in sinh_vien:
    print(f"{sv['ten']}: {xep_loai_diem(sv['diem'])}")

thong_ke = thong_ke_loai_hoc_luc(sinh_vien)
print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for loai, so_luong in thong_ke.items():
    print(f"{loai}: {so_luong}")
