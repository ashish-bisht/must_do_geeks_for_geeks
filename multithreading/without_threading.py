import threading
import time


start = time.perf_counter()


def working_on_something():
    print("Sleeping for a sec")
    time.sleep(1)
    print("Woke up")


working_on_something()
working_on_something()

finish = time.perf_counter()

print("total time taken is ", finish - start)
