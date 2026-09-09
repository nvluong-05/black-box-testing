# Danh sách Test Case – Kiểm thử hộp đen (8 bài toán)

Ký hiệu kỹ thuật: **EP** = Phân lớp tương đương (Equivalence Partitioning),
**BVA** = Phân tích giá trị biên (Boundary Value Analysis),
**INV** = Dữ liệu không hợp lệ (Invalid Data).

---
## Bài 1 & 2: Chu vi / Diện tích hình chữ nhật
**Đầu vào:** `a` (chiều dài), `b` (chiều rộng) – số thực. Miền hợp lệ: `a > 0` và `b > 0`.
**Đầu ra mong đợi:** Chu vi = 2(a+b); Diện tích = a×b; báo lỗi nếu dữ liệu không hợp lệ.

| TC | Đầu vào (a, b) | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|----------------|----------|------------------|---------|
| TC01 | (5, 3) | EP – số dương bình thường | Chu vi=16, Diện tích=15 | PASS |
| TC02 | (0.0001, 0.0001) | BVA – cận dưới, sát 0 nhưng hợp lệ | Chu vi≈0.0004, Diện tích≈1e-8 | PASS |
| TC03 | (1 000 000, 1 000 000) | EP – số rất lớn | Chu vi=4 000 000, Diện tích=1e12 | PASS |
| TC04 | (2, 2) | EP – trường hợp đặc biệt (hình vuông) | Chu vi=8, Diện tích=4 | PASS |
| TC05 | (0, 5) | BVA/INV – cạnh bằng 0 (biên) | Báo lỗi (ValueError) | PASS |
| TC06 | (-3, 5) | INV – một cạnh âm | Báo lỗi | PASS |
| TC07 | (-3, -5) | INV – cả hai cạnh âm | Báo lỗi | PASS |
| TC08 | ("a", 5) | INV – sai kiểu dữ liệu | Báo lỗi | PASS |

---
## Bài 3: Giải phương trình bậc 2 ax²+bx+c=0
**Đầu vào:** `a, b, c` (số thực bất kỳ).
**Đầu ra mong đợi:** Số nghiệm và giá trị nghiệm theo dấu Δ=b²-4ac, hoặc các trường hợp suy biến khi a=0.

| TC | (a, b, c) | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|-----------|----------|------------------|---------|
| TC01 | (1, -3, 2) | EP – Δ>0 | 2 nghiệm phân biệt: x=1, x=2 | PASS |
| TC02 | (1, -2, 1) | BVA – Δ=0 (biên) | Nghiệm kép x=1 | PASS |
| TC03 | (1, 1, 1) | EP – Δ<0 | Vô nghiệm thực (nghiệm phức) | PASS |
| TC04 | (0, 2, -4) | BVA/EP – a=0, b≠0 (suy biến bậc 1) | x=2 | PASS |
| TC05 | (0, 0, 5) | EP – a=b=0, c≠0 | Vô nghiệm | PASS |
| TC06 | (0, 0, 0) | EP – a=b=c=0 | Vô số nghiệm | PASS |
| TC07 | ("x", 1, 1) | INV – sai kiểu dữ liệu | Báo lỗi | PASS |
| TC08 | (None, 1, 1) | INV – giá trị rỗng | Báo lỗi | PASS |

---
## Bài 4: Số ngày trong tháng
**Đầu vào:** `thang` (1–12), `nam` (>0) – số nguyên.
**Đầu ra mong đợi:** Số ngày của tháng đó trong năm đó (28/29/30/31).

| TC | (thang, nam) | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|--------------|----------|------------------|---------|
| TC01 | (1, 2024) | EP – tháng 31 ngày | 31 | PASS |
| TC02 | (4, 2024) | EP – tháng 30 ngày | 30 | PASS |
| TC03 | (2, 2024) | EP – tháng 2, năm nhuận | 29 | PASS |
| TC04 | (2, 2023) | EP – tháng 2, năm không nhuận | 28 | PASS |
| TC05 | (2, 2000) | BVA – chia hết 400 → nhuận | 29 | PASS |
| TC06 | (2, 1900) | BVA – chia hết 100, không chia hết 400 → không nhuận | 28 | PASS |
| TC07 | (1, 2024) | BVA – biên dưới tháng=1 | 31 | PASS |
| TC08 | (12, 2024) | BVA – biên trên tháng=12 | 31 | PASS |
| TC09 | (0, 2024) | INV/BVA – tháng=0 (ngoài biên dưới) | Báo lỗi | PASS |
| TC10 | (13, 2024) | INV/BVA – tháng=13 (ngoài biên trên) | Báo lỗi | PASS |
| TC11 | (1, -5) | INV – năm âm | Báo lỗi | PASS |
| TC12 | (1.5, 2024) | INV – tháng không phải số nguyên | Báo lỗi | PASS |

---
## Bài 5: Kiểm tra số nguyên tố
**Đầu vào:** `n` (số nguyên ≥ 0).
**Đầu ra mong đợi:** True nếu n là số nguyên tố, False nếu không, báo lỗi nếu n âm hoặc sai kiểu.

| TC | n | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|---|----------|------------------|---------|
| TC01 | 2 | BVA – số nguyên tố nhỏ nhất | True | PASS |
| TC02 | 3 | EP – số nguyên tố lẻ nhỏ | True | PASS |
| TC03 | 17 | EP – số nguyên tố thường | True | PASS |
| TC04 | 97 | EP – số nguyên tố lớn (2 chữ số) | True | PASS |
| TC05 | 0 | BVA – biên | False | PASS |
| TC06 | 1 | BVA – biên | False | PASS |
| TC07 | 4 | EP – hợp số chẵn nhỏ nhất | False | PASS |
| TC08 | 9 | EP – hợp số lẻ (bình phương số nguyên tố) | False | PASS |
| TC09 | 100 | EP – hợp số lớn | False | PASS |
| TC10 | -7 | **INV** – số âm | Báo lỗi (phát hiện lỗi thật, xem ghi chú) | PASS |
| TC11 | 3.5 | INV – không phải số nguyên | Báo lỗi | PASS |
| TC12 | "10" | INV – sai kiểu dữ liệu | Báo lỗi | PASS |

> **Ghi chú:** Ở lần chạy đầu tiên, TC10 (`n = -7`) đã **FAIL** vì bản đầu của hàm coi mọi `n < 2` là "không phải số nguyên tố" (trả về `False`) mà không phân biệt số âm là dữ liệu không hợp lệ. Đây là ca kiểm thử hộp đen đã phát hiện lỗi thực sự. Đã sửa mã nguồn để `n < 0` ném lỗi `ValueError`, chạy lại và PASS.

---
## Bài 6: Tổng S = 1 - 2 + 3 - 4 + ... ± n
**Đầu vào:** `n` (số nguyên dương).
**Đầu ra mong đợi:** Giá trị tổng S theo công thức đan xen dấu.

| TC | n | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|---|----------|------------------|---------|
| TC01 | 1 | BVA – biên dưới | S=1 | PASS |
| TC02 | 2 | EP – n chẵn nhỏ | S=-1 | PASS |
| TC03 | 3 | EP – n lẻ nhỏ | S=2 | PASS |
| TC04 | 10 | EP – n chẵn lớn hơn | S=-5 | PASS |
| TC05 | 11 | EP – n lẻ lớn hơn | S=6 | PASS |
| TC06 | 0 | INV/BVA – biên, không hợp lệ | Báo lỗi | PASS |
| TC07 | -5 | INV – số âm | Báo lỗi | PASS |
| TC08 | 2.5 | INV – không phải số nguyên | Báo lỗi | PASS |
| TC09 | "5" | INV – sai kiểu dữ liệu | Báo lỗi | PASS |

---
## Bài 7: Tìm UCLN của a và b
**Đầu vào:** `a, b` (số nguyên không âm, không đồng thời bằng 0).
**Đầu ra mong đợi:** Giá trị UCLN(a, b).

| TC | (a, b) | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|--------|----------|------------------|---------|
| TC01 | (12, 18) | EP – trường hợp thường | 6 | PASS |
| TC02 | (7, 13) | EP – hai số nguyên tố cùng nhau | 1 | PASS |
| TC03 | (0, 5) | BVA – một số bằng 0 | 5 | PASS |
| TC04 | (5, 0) | BVA – số còn lại bằng 0 | 5 | PASS |
| TC05 | (100, 100) | EP – hai số bằng nhau | 100 | PASS |
| TC06 | (1, 999999) | BVA – một số là 1 | 1 | PASS |
| TC07 | (0, 0) | INV/BVA – cả hai đều bằng 0 | Báo lỗi | PASS |
| TC08 | (-4, 8) | INV – số âm | Báo lỗi | PASS |
| TC09 | (4.5, 8) | INV – không phải số nguyên | Báo lỗi | PASS |
| TC10 | ("4", 8) | INV – sai kiểu dữ liệu | Báo lỗi | PASS |

---
## Bài 8: Tổng giai thừa S = 1! + 2! + ... + n!
**Đầu vào:** `n` (số nguyên dương).
**Đầu ra mong đợi:** Tổng các giai thừa từ 1! đến n!.

| TC | n | Kỹ thuật | Đầu ra mong đợi | Kết quả |
|----|---|----------|------------------|---------|
| TC01 | 1 | BVA – biên dưới | S=1 | PASS |
| TC02 | 2 | EP – giá trị nhỏ | S=3 | PASS |
| TC03 | 3 | EP – giá trị nhỏ | S=9 | PASS |
| TC04 | 5 | EP – giá trị thường | S=153 | PASS |
| TC05 | 10 | EP – giá trị lớn hơn | S=4 037 913 | PASS |
| TC06 | 0 | INV/BVA – biên, không hợp lệ | Báo lỗi | PASS |
| TC07 | -3 | INV – số âm | Báo lỗi | PASS |
| TC08 | 2.5 | INV – không phải số nguyên | Báo lỗi | PASS |
| TC09 | None | INV – giá trị rỗng | Báo lỗi | PASS |
| TC10 | giai_thua(0) | EP – quy ước 0!=1 (hàm phụ trợ) | 1 | PASS |

---
## Tổng kết
- Tổng số ca kiểm thử: **77**
- Kết quả: **77/77 PASS** (sau khi sửa 1 lỗi phát hiện được ở Bài 5)
- Công cụ chạy: `pytest`
