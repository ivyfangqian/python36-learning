# 装饰器：使用额外的代码包装一个函数，可以定义一个装饰器函数，
# 装饰器函数可以接收一个函数作为参数，并返回一个函数
# https://www.jianshu.com/p/f51dbe1eaa4d

import time
from functools import wraps, partial


# 添加一个装饰器
def timethis(func):
    '''Decorator that reports the excution time.'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


# 使用装饰器
@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(1000000)
# 一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数。 这样写与上面的写法是一致的。
res = timethis(countdown(1000000))


# 顺便说一下，内置的装饰器比如 @staticmethod, @classmethod,@property 原理也是一样的。 例如，下面这两个代码片段是等价的：

class A:
    @classmethod
    def method(cls):
        pass


class B:
    # Equivalent definition of a class method
    def method(cls):
        pass

    method = classmethod(method)


print(countdown.__doc__)
print(countdown.__name__)
print(countdown.__wrapped__)
from inspect import signature

print(signature(countdown))
print(countdown.__wrapped__)


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


add(2, 3)
print(add.__wrapped__(2, 3))

# 定义一个可接收参数的装饰器
import logging


# 初看起来，这种实现看上去很复杂，但是核心思想很简单。
# 最外层的函数 logged() 接受参数并将它们作用在内部的装饰器函数上面。
# 内层的函数 decorate() 接受一个函数作为参数，然后在函数上面放置一个包装器。
# 这里的关键点是包装器是可以使用传递给 logged() 的参数的。
def logged(level, name=None, message=None):
    """Add logging to a function."""

    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 使用装饰器
@logged(logging.DEBUG)
def multi(x, y):
    return x * y


@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam!")


multi(2, 3)


# 定义一个接受参数的包装器看上去比较复杂主要是因为底层的调用序列。特别的，如果你有下面这个代码：

# @decorator(x, y, z)
# def func(a, b):
#     pass
# 装饰器处理过程跟下面的调用是等效的;

# def func(a, b):
#     pass
# func = decorator(x, y, z)(func)


# 可选参数装饰器

def logged(func, *, level=logging.DEBUG, name=None, message=None):
    """Add logging to a function."""
    if func is None:
        return partial(logged(level=level, name=name, message=message))

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def sub(x, y):
    return x - y


sub(1, 2)
