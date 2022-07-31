import pytest
# 同一个函数测试多组用例
@pytest.mark.parametrize('a,b,c', [(1, 2, 3), (0, 1, 1), (-1, 1, 0)])
def test(a, b, c):

    assert a + b == c

if __name__ == '__main__':
    pytest.main(['-v', __file__])