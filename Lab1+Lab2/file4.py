# Bài 4
tuoi = int(input("Nhập tuổi của hành khách: "))
thoi_gian_dat_ve = int(input("Nhập số ngày hành khách đặt vé trước: "))
gia_ve_ban_dau = 120000  
if tuoi >= 0 and tuoi <= 5: 
    print("Hành khách là trẻ em, vé là miễn phí.")
elif tuoi >= 6 and tuoi <= 12:  
    print("Hành khách là trẻ em, giá vé: 50.000 đồng.")
elif tuoi >= 13 and tuoi <= 59:  
    if thoi_gian_dat_ve < 7:  
        print("Hành khách là người lớn, giá vé: 100.000 đồng.")
    else:
        print("Hành khách là người lớn, giá vé: 120.000 đồng.")
elif tuoi >= 60:
    gia_ve_giam_gia = gia_ve_ban_dau * 0.75
    print("Hành khách là người cao tuổi, giá vé sau khi giảm giá: {:.0f} đồng.".format(gia_ve_giam_gia))
else:
    print("Thông tin tuổi không hợp lệ.")
