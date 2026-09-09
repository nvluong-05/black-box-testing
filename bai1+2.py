# bai 1: tinh chu vi HCN
# bai 2: tinh dien tich HCN


def chu_vi_hcn(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a va b phai la so")
    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("a va b phai la so")
    if a <= 0 or b <= 0:
        raise ValueError("Canh hinh chu nhat phai la so duong (> 0)")
    return 2 * (a + b)


def dien_tich_hcn(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("a va b phai la so")
    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("a va b phai la so")
    if a <= 0 or b <= 0:
        raise ValueError("Canh hinh chu nhat phai la so duong (> 0)")
    return a * b


if __name__ == "__main__":
    try:
        a = float(input("Nhap chieu dai a: "))
        b = float(input("Nhap chieu rong b: "))
        print("Chu vi:", chu_vi_hcn(a, b))
        print("Dien tich:", dien_tich_hcn(a, b))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)