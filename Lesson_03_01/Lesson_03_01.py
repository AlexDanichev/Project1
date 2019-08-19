def simple_decorator(*args):
    def actual_simple_decorator(func):
        def wrapper():
            print(args)
            print("hello")
            result = func()
            print("World")
            return result

        return wrapper
    return actual_simple_decorator

@simple_decorator("a","b")
def hi():
    print("hi")
    return False


erere = hi()
