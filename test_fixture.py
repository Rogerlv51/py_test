import pytest

# 使用autouse则不需要给测试函数传递固件名称了

def test_add(func):
    a=func
    print("添加会员")
    print(a)
def test_query():
    print("库存查询")

if __name__ == '__main__':
    pytest.main(['-q', __file__])

