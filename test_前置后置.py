import pytest

class Test:
    def setup_method(self):
        print("这是类前置\n")
    def teardown_method(self):
        print("这是类后置\n")
    def test1(self):
        assert 1 == 1
        print("test1 pass\n")
    def test2(self):
        assert 1 == 1
        print("test2 pass\n")
if __name__ == '__main__':
    pytest.main(['-s', __file__])