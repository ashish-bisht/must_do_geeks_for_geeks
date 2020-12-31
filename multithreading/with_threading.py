import threading
import time


start = time.perf_counter()


def working_on_something():
    print("Sleeping for a sec")
    time.sleep(1)
    print("Woke up")


thread1 = threading.Thread(target=working_on_something)
thread2 = threading.Thread(target=working_on_something)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

finish = time.perf_counter()

print("total time taken is ", finish - start)
