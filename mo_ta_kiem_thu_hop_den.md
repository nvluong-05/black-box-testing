# Mô tả cách áp dụng kiểm thử hộp đen cho từng bài toán

Nguyên tắc chung: chỉ dựa vào **đặc tả đầu vào/đầu ra** của mỗi bài toán
(không xem cấu trúc code bên trong) để chia miền dữ liệu thành các lớp
tương đương, chọn giá trị biên của từng lớp, và bổ sung dữ liệu sai/không
hợp lệ để kiểm tra khả năng xử lý ngoại lệ.

---
### Bài 1 & 2 — Chu vi / Diện tích hình chữ nhật
Miền hợp lệ của cạnh là số dương (`a > 0`, `b > 0`). Áp dụng:
- **EP:** chia thành lớp "số dương bình thường", "số rất lớn", "hình vuông (a=b)".
- **BVA:** chọn giá trị sát 0 (0.0001) làm biên dưới của miền hợp lệ.
- **Dữ liệu không hợp lệ:** cạnh = 0 (đúng biên nhưng ngoài miền cho phép),
  cạnh âm, và sai kiểu dữ liệu (chuỗi thay vì số).

### Bài 3 — Giải phương trình bậc 2
Đặc tính bài toán phụ thuộc dấu của Δ = b²-4ac và trường hợp suy biến khi a=0.
- **EP:** chia theo 3 miền của Δ (>0, =0, <0) và 2 miền suy biến (a=0,b≠0
  và a=b=0).
- **BVA:** chọn đúng giá trị làm Δ=0 (biên giữa 2-nghiệm và vô nghiệm thực).
- **Dữ liệu không hợp lệ:** truyền chuỗi hoặc giá trị rỗng thay vì số.

### Bài 4 — Số ngày trong tháng
Kết quả phụ thuộc nhóm tháng (31/30/28-29 ngày) và quy tắc năm nhuận.
- **EP:** chia tháng thành 3 nhóm theo số ngày; chia năm thành nhuận/không nhuận.
- **BVA:** kiểm tra biên tháng (1 và 12), và biên đặc biệt của quy tắc năm
  nhuận (năm 1900 – chia hết 100 nhưng không nhuận; năm 2000 – chia hết 400
  nên nhuận).
- **Dữ liệu không hợp lệ:** tháng nằm ngoài khoảng 1–12 (0, 13), năm âm,
  tháng không phải số nguyên.

### Bài 5 — Kiểm tra số nguyên tố
- **EP:** chia thành số nguyên tố, hợp số chẵn, hợp số lẻ (bình phương của
  số nguyên tố), số nguyên tố lớn.
- **BVA:** kiểm tra các giá trị biên 0, 1, 2 (số nguyên tố nhỏ nhất).
- **Dữ liệu không hợp lệ:** số âm, số thực, sai kiểu dữ liệu. Chính ca số
  âm đã giúp phát hiện lỗi thực tế trong lần chạy đầu tiên (hàm coi số âm
  là "không nguyên tố" thay vì báo lỗi dữ liệu sai).

### Bài 6 — Tổng S = 1-2+3-4+...±n
- **EP:** chia theo tính chẵn/lẻ của n vì dấu của số hạng cuối khác nhau.
- **BVA:** kiểm tra biên dưới n=1.
- **Dữ liệu không hợp lệ:** n=0 hoặc âm (ngoài miền n≥1), n không phải số
  nguyên.

### Bài 7 — Tìm UCLN của a và b
- **EP:** trường hợp UCLN thường, hai số nguyên tố cùng nhau (UCLN=1),
  hai số bằng nhau.
- **BVA:** một trong hai số bằng 0 (UCLN(0,b)=b), hoặc bằng 1.
- **Dữ liệu không hợp lệ:** cả hai số cùng bằng 0 (không xác định), số âm,
  số thực, sai kiểu dữ liệu.

### Bài 8 — Tổng giai thừa S = 1!+2!+...+n!
- **EP:** các giá trị n nhỏ và n lớn hơn để kiểm tra độ chính xác phép nhân
  tích lũy.
- **BVA:** biên dưới n=1; kiểm tra riêng quy ước 0!=1 của hàm giai thừa phụ trợ.
- **Dữ liệu không hợp lệ:** n=0 hoặc âm, n không phải số nguyên, giá trị rỗng.

---
**Kết quả áp dụng:** tổng cộng 77 ca kiểm thử cho 8 bài, chạy bằng `pytest`,
đạt 77/77 PASS sau khi sửa 1 lỗi phát hiện được ở Bài 5 (xem chi tiết trong
`TESTCASES.md` và `ket_qua_kiem_thu.txt`).
