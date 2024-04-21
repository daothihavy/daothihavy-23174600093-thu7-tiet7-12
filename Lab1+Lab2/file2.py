# Bài 2
diem_chuyen_can = float(input("Nhập điểm chuyên cần của sinh viên: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ của sinh viên: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ của sinh viên: "))
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
print("Điểm trung bình của sinh viên là:", diem_trung_binh)
if diem_trung_binh >= 9:
    print("Loại điểm: A")
elif diem_trung_binh >= 7 and diem_trung_binh < 9:
    print("Loại điểm: B")
elif diem_trung_binh >= 5 and diem_trung_binh < 7:
    print("Loại điểm: C")
else:
    print("Loại điểm: D")
