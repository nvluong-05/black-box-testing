# bai 3: giai phuong trinh bac 2

import math


def giai_pt_bac2(a: float, b: float, c: float):
    for v in (a, b, c):
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            raise ValueError("a, b, c phai la so")

    if a == 0:
        if b == 0:
            if c == 0:
                return ("vo_so_nghiem",)
            return ("vo_nghiem",)
        return ("nghiem_don", -c / b)

    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return ("hai_nghiem_phan_biet", x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return ("nghiem_kep", x)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-delta) / (2 * a)
        return ("vo_nghiem_thuc", real, imag)


if __name__ == "__main__":
    try:
        a = float(input("Nhap a: "))
        b = float(input("Nhap b: "))
        c = float(input("Nhap c: "))
        print(giai_pt_bac2(a, b, c))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)