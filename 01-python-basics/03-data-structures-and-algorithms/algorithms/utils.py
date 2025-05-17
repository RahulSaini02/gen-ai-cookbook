import time


def log_time(func):
    """
    Decorator to log the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"⏱ Total execution time for {func.__name__}: {end_time - start_time:.10f} seconds"
        )
        return result

    return wrapper
