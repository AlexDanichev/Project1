

def decorator(num_of_repeats):
    print(num_of_repeats)
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            for i in range(num_of_repeats):
                print("The begin of wrapping")
                result = func(*args, **kwargs)
                print("The end of wrapping")
            return result, func.__name__
        return wrapper
    return actual_decorator


@decorator(10)
def addition(arg1, arg2):
    return arg1 + arg2

print(addition(1,2))


def test_func(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)




