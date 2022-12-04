import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"time: {self.end_time - self.start_time}")
        if exc_val:
            raise


@contextmanager
def cm_timer_2():
    try:
        error = 0
        start_time = time.time()
        yield
    except Exception as err:
        error = err
    finally:
        end_time = time.time()
        print(f"time: {end_time - start_time}")
        if error:
            raise


def main():
    with cm_timer_1():
        time.sleep(0.5)
    with cm_timer_2():
        time.sleep(0.5)


if __name__ == "__main__":
    main()
