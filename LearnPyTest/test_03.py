'''
1.测试前置和后置
2.类级别和方法级别
'''

# 测试类使用Test开头，里面不能有__init__构造方法
import pytest
class TestClass:
    def setup_class(self):
        print("测试前置，类里所有用例开始前执行")

    def teardown_class(self):
        print("测试后置，类里所有用例结束后执行")

    def setup(self): #也可以使用setup_method
        print("测试前置，每个方法前执行")

    def teardown(self): #也可以使用teardown_method
        print("测试后置，每个方法后执行")

    def test_case01(self):
        print("用例1")

    def test_case02(self):
        print("用例2")

# if __name__ == '__main__':
#     pytest.main(["-v -n 2","D:\ApiAutoTest\LearnPyTest\test_03.py"])