from src.calc import * # 関数を読み込む

def test_mul():
    assert 6 == mul(3, 2)

def test_div():
    assert 6 == div(12,2)