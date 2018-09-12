import functools
import time


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


@do_twice
def say_hi():
    print("hello")


@do_twice
def greet(name):
    print(f"Hello {name}")
    return f"Hi {name}"


@do_twice
def invite(name, age):
    print(f"I want to invite {name}, a person have {age} year old")


say_hi()
invite("Huy", 20)
print(greet("Huy"))
waste_some_time(10)