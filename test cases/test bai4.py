import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai4 import so_ngay_trong_thang


@test.mark.parametrize("thang,nam,expected", [
    (1, 2024, 31),    
    (4, 2024, 30),  
    (2, 2024, 29),    
    (2, 2023, 28),    
    (2, 2000, 29),   
    (2, 1900, 28),   
    (1, 2024, 31),    
    (12, 2024, 31),   
])
def test_so_ngay_hop_le(thang, nam, expected):
    assert so_ngay_trong_thang(thang, nam) == expected


@test.mark.parametrize("thang,nam", [
    (0, 2024),     
    (13, 2024),    
    (1, -5),       
    (1.5, 2024),   
])
def test_so_ngay_khong_hop_le(thang, nam):
    with test.raises(ValueError):
        so_ngay_trong_thang(thang, nam)