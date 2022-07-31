import pytest

from PIL import ImageGrab
@pytest.fixture(name='func', autouse=True, params=[1,2,3,4])
def login():
    print("登录")
    yield "注销"    # 实现后置，yield是生成器