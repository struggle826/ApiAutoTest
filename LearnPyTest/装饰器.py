'''
装饰器：在运行中增加功能的一种方式
'''

'''
已经写好了一些测试用例，后面维护代码时，想增加这些用例的功能，比如增加日志，又不想改test_case01、test_case02的代码
将日志的功能定义成一个装饰器。装饰器是拿函数作为参数
'''

def log(func):
    def wrapper(*args,**kw):
        # 每个函数有一个__name__属性，返回函数的名字
        print(f"in 函数{func.__name__}")
        func(*args,**kw)
        print(f"out 函数{func.__name__}")

    return wrapper


def test_case01():
    print("in 函数 : test_case01")
    print("用例1")
    print("out 函数 : test_case01")

@log  #达到和test_case01一样的效果
def test_case02():
    print("用例2")

@log
def test_case03():
    print("用例3")
