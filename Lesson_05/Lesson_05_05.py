import threading
from threading import Thread


def thread_decorator(thread_name, thread_daemon):
    def actual_decorator(func):
        def wrapper():
            thread = Thread( target=func, daemon=thread_daemon )
            thread.start()
            print( f"thread{thread_name} is started" )
        return wrapper
    return actual_decorator


@thread_decorator(" some_name", True)
def hi():
    print("hi")

a = hi()


