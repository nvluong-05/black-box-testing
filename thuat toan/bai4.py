# bai 4: tinh so ngay trong 1 thang

def la_nam_nhuan(nam: int) -> bool:
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang: int, nam: int) -> int:
    if not isinstance(thang, int) or isinstance(thang, bool):
        raise ValueError("Thang phai la so nguyen")
    if not isinstance(nam, int) or isinstance(nam, bool):
        raise ValueError("Nam phai la so nguyen")
    if thang < 1 or thang > 12:
        raise ValueError("Thang phai trong khoang 1..12")
    if nam <= 0:
        raise ValueError("Nam phai la so nguyen duong")

    thang_31 = {1, 3, 5, 7, 8, 10, 12}
    thang_30 = {4, 6, 9, 11}

    if thang in thang_31:
        return 31
    if thang in thang_30:
        return 30
    return 29 if la_nam_nhuan(nam) else 28

if __name__ == "__main__":
    try:
        thang = int(input("Nhap thang: "))
        nam = int(input("Nhap nam: "))
        print("So ngay:", so_ngay_trong_thang(thang, nam))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)