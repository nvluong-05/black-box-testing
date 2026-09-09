# bai 8: tinh tong S = 1! + 2! + 3! + ... + n! (trong do su dung ham tinh giai thua cua n)

def giai_thua(k: int) -> int:
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k phai la so nguyen")
    if k < 0:
        raise ValueError("k phai la so nguyen khong am")
    ket_qua = 1
    for i in range(2, k + 1):
        ket_qua *= i
    return ket_qua

def tong_giai_thua(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai la so nguyen duong (>= 1)")
    return sum(giai_thua(i) for i in range(1, n + 1))

if __name__ == "__main__":
    try:
        n = int(input("Nhap n: "))
        print("S =", tong_giai_thua(n))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)