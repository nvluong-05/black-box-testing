import sys, os, math
from tkinter import _test
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "thuat toan"))
import test
from bai3 import giai_pt_bac2

def test_hai_nghiem_phan_biet():
    kq = giai_pt_bac2(1, -3, 2)
    assert kq[0] == "hai_nghiem_phan_biet"
    assert set(round(v, 6) for v in kq[1:]) == {1.0, 2.0}


def test_nghiem_kep():
    kq = giai_pt_bac2(1, -2, 1)
    assert kq == ("nghiem_kep", 1.0)


def test_vo_nghiem_thuc_delta_am():
    kq = giai_pt_bac2(1, 1, 1)
    assert kq[0] == "vo_nghiem_thuc"


def test_phuong_trinh_bac_1_a_bang_0():
    kq = giai_pt_bac2(0, 2, -4)
    assert kq == ("nghiem_don", 2.0)


def test_a_b_bang_0_c_khac_0():
    kq = giai_pt_bac2(0, 0, 5)
    assert kq == ("vo_nghiem",)


def test_a_b_c_bang_0():
    kq = giai_pt_bac2(0, 0, 0)
    assert kq == ("vo_so_nghiem",)


@_test.mark.parametrize("a,b,c", [
    ("x", 1, 1),     
    (None, 1, 1),    
])
def test_du_lieu_khong_hop_le(a, b, c):
    with _test.raises(ValueError):
        giai_pt_bac2(a, b, c)