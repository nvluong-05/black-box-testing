# bai 6: tinh tong s = 1-2 +3-4+...+n

def tong_dan_xen(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai la so nguyen duong (>= 1)")
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            s += i
        else:
            s -= i
    return s

if __name__ == "__main__":
    try:
        n = int(input("Nhap n: "))
        print("S =", tong_dan_xen(n))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)