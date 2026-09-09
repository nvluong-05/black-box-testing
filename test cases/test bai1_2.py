import sys, os, math
from tkinter import _test
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai1_2 import chu_vi_hcn, dien_tich_hcn

@_test.mark.parametrize("a,b,expected", [
    (5, 3, 16),         
    (0.0001, 0.0001, 0.0004),  
    (1000000, 1000000, 4000000), 
    (2, 2, 8),            
])
def test_chu_vi_hop_le(a, b, expected):
    assert math.isclose(chu_vi_hcn(a, b), expected, rel_tol=1e-9)


@_test.mark.parametrize("a,b,expected", [
    (5, 3, 15),
    (0.0001, 0.0001, 0.00000001),
    (1000000, 1000000, 1000000000000),
    (2, 2, 4),
])
def test_dien_tich_hop_le(a, b, expected):
    assert math.isclose(dien_tich_hcn(a, b), expected, rel_tol=1e-6)


@_test.mark.parametrize("a,b", [
    (0, 5),       
    (-3, 5),       
    (-3, -5),      
    ("a", 5),    
])
def test_chu_vi_khong_hop_le(a, b):
    with _test.raises(ValueError):
        chu_vi_hcn(a, b)


@_test.mark.parametrize("a,b", [
    (0, 5),
    (-3, 5),
    (-3, -5),
    (None, 5),
])
def test_dien_tich_khong_hop_le(a, b):
    with _test.raises(ValueError):
        dien_tich_hcn(a, b)