import unittest
def my_func1(a):
    if a == 1:
        return 2
    elif a == -1:
        return 3
    else:
        return 1

def my_func2(b):
    if b != "yes":
        raise ValueError("you can only say yes!")
    else:
        return True

class TestFunc(unittest.TestCase):
    def test_func1(self):  # my_func1函数没问题
        self.assertEqual(my_func1(1), 2)
        self.assertEqual(my_func1(-1), 3)
        for i in range(-100, 100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(my_func1(i), 1)

    def test_func2(self):  # 也没问题，测试应该显示通过
        self.assertTrue(my_func2("yes"))
        with self.assertRaises(ValueError):
            my_func2("nononono")

if __name__ == '__main__':
    unittest.main()
