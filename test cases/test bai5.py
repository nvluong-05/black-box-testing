import sys, os
from tkinter import _test
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai5 import la_so_nguyen_to


@_test.mark.parametrize("n,expected", [
    (2, True),     
    (3, True),     
    (17, True),    
    (97, True),    
    (0, False),    
    (1, False),    
    (4, False),   
    (9, False),    
    (100, False),
])
def test_nguyen_to_hop_le(n, expected):
    assert la_so_nguyen_to(n) == expected


@_test.mark.parametrize("n", [
    -7,    
    3.5,     
    "10",    
])
def test_nguyen_to_khong_hop_le(n):
    with _test.raises(ValueError):
        la_so_nguyen_to(n)