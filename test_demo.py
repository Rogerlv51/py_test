import pytest


@pytest.mark.a
@pytest.mark.skip(reason="此版本不执行")
def test_1():
    print(123)
    assert 1 == 1


@pytest.mark.b
@pytest.mark.skipif(1 == 0, reason='此版本不执行')
def test_2():
    print(123)
    assert 1 == 1

class Test_Add:
    def test(self):
        assert 12 > 100

if __name__ == '__main__':
    # pytest.main(['-s', __file__])   # 这里我们运行，测试结果会显示只通过了一个测试用例，说明pytest必须要以test命名开头
    # -s表示将print语句的结果输出，__file__是执行当前文件的意思
    # pytest.main(['-v', __file__])  -v输出详细测试信息
    # pytest.main(['-q', __file__])    # 极简输出
    pytest.main(['-q', __file__])

