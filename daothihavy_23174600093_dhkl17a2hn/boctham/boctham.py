import random
import csv

# Tạo một danh sách để lưu trữ tên của 15 người tham gia
danh_sach = ["Dinh Dac Bui", "Le Hong Hoa", "Vu Thi Nhan", "Pham Hong Ngoc", "Duong Van Duc",
             "Vu Phuong Thoa", "Nguyen Kim Dan", "Do Dinh Anh", "Bui Van Toan", "Luu Huu Phuoc",
             "Dao Thi Huyen Thu", "Dong Ha Linh", "Hoang Huy Nham", "Nguyen Tung Benh", "Vu Van Huu"]

# Tạo một danh sách để lưu trữ tên của 15 người tham gia
danh_sach_chia_nhom = set()

# Tạo một dictionary để lưu trữ số lượng người trong mỗi nhóm.
so_luong = 3
group_dict = {f'Nhóm {i//so_luong + 1}': [] for i in range(len(danh_sach))}

print(f"Danh sách lưu trữ tên của những người đã được chia vào nhóm: {danh_sach_chia_nhom}")
print(f"Số lượng người trong mỗi nhóm: {group_dict}")

# Chia ngẫu nhiên các người tham gia vào các nhóm, mỗi nhóm có 3 thành viên
def chia_nhom(danh_sach, so_luong):
    random.shuffle(danh_sach)
    so_luong_nhom = len(danh_sach) // so_luong
    nhom = [danh_sach[i * so_luong:(i + 1) * so_luong] for i in range(so_luong_nhom)]
    return nhom

# Tính xác suất một người được chia vào một nhóm cụ thể
def tinh_xac_suat(danh_sach, nhom):
    tong_thanh_vien = len(danh_sach)
    tong_nhom = len(nhom)
    kich_thuoc_nhom = len(nhom[0])
    return kich_thuoc_nhom / tong_thanh_vien

# Hiển thị danh sách nhóm và thành viên trong mỗi nhóm
def display_groups(nhom):
    for idx, group in enumerate(nhom):
        print(f"Nhóm {idx + 1}: {', '.join(group)}")

# Lưu lại kết quả của quá trình chia nhóm vào một file CSV
def save_to_csv(danh_sach, nhom, filename="group_assignment.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Tên người tham gia", "Tên nhóm", "Xác suất được chia vào nhóm"])
        for idx, group in enumerate(nhom):
            probability = tinh_xac_suat(danh_sach, nhom)
            for member in group:
                writer.writerow([member, f"Nhóm {idx + 1}", f"{probability:.2f}"])

def menu():
    print("===== Chia nhóm ngẫu nhiên =====")
    print("1. Chia nhóm")
    print("2. Hiển thị danh sách nhóm")
    print("3. Lưu kết quả vào file CSV")
    print("4. Thoát")

def main():
    nhom = []
    
    while True:
        menu()
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            nhom = chia_nhom(danh_sach, so_luong)
            print("Đã chia nhóm ngẫu nhiên.")
        elif choice == "2":
            if nhom:
                display_groups(nhom)
            else:
                print("Chưa có nhóm nào được chia.")
        elif choice == "3":
            if nhom:
                save_to_csv(danh_sach, nhom)
                print("Danh sách nhóm đã được lưu vào file group_assignment.csv")
            else:
                print("Chưa có nhóm nào được chia để lưu.")
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
