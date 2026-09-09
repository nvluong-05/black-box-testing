# bai 7: tinh UCLN cua a va b

def ucln(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int) or isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("a va b phai la so nguyen")
    if a == 0 and b == 0:
        raise ValueError("a va b khong duoc dong thoi bang 0")
    if a < 0 or b < 0:
        raise ValueError("a va b phai la so nguyen khong am")
    a, b = int(a), int(b)
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        a = int(input("Nhap a: "))
        b = int(input("Nhap b: "))
        print("UCLN =", ucln(a, b))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)