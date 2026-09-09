import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai6 import tong_dan_xen


@test.mark.parametrize("n,expected", [
    (1, 1),    
    (2, -1),    
    (3, 2),     
    (10, -5),   
    (11, 6),    
])
def test_tong_dan_xen_hop_le(n, expected):
    assert tong_dan_xen(n) == expected


@test.mark.parametrize("n", [
    0,  
    -5,      
    2.5,     
    "5",    
])
def test_tong_dan_xen_khong_hop_le(n):
    with test.raises(ValueError):
        tong_dan_xen(n)