import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai8 import tong_giai_thua, giai_thua


@test.mark.parametrize("n,expected", [
    (1, 1),      
    (2, 3),     
    (3, 9),     
    (5, 153),    
    (10, 4037913),  
])
def test_tong_giai_thua_hop_le(n, expected):
    assert tong_giai_thua(n) == expected


@test.mark.parametrize("n", [
    0,      
    -3,      
    2.5,     
    None,    
])
def test_tong_giai_thua_khong_hop_le(n):
    with test.raises(ValueError):
        tong_giai_thua(n)


def test_giai_thua_cua_0_bang_1():
    assert giai_thua(0) == 1