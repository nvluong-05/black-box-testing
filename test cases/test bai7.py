import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai7 import ucln


@test.mark.parametrize("a,b,expected", [
    (12, 18, 6),
    (7, 13, 1),     
    (0, 5, 5),     
    (5, 0, 5),     
    (100, 100, 100),
    (1, 999999, 1), 
])
def test_ucln_hop_le(a, b, expected):
    assert ucln(a, b) == expected


@test.mark.parametrize("a,b", [
    (0, 0),      
    (-4, 8),     
    (4.5, 8),    
    ("4", 8),    
])
def test_ucln_khong_hop_le(a, b):
    with test.raises(ValueError):
        ucln(a, b)