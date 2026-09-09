# bai 5: kiem tra 1 so co phai so nguyen to hay khong

def la_so_nguyen_to(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n phai la so nguyen")
    if n < 0:
        raise ValueError("n phai la so nguyen khong am")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    try:
        n = int(input("Nhap n: "))
        print(f"{n} la so nguyen to:", la_so_nguyen_to(n))
    except ValueError as e:
        print("Loi du lieu dau vao:", e)