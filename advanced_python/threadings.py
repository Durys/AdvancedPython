import time
from threading import *


class ThreadingTest:
    s = 0

    def __init__(self):
        self.lock = Lock()

        self.thread1 = Thread(target=self.execute, args=("Thread One", 1))
        self.thread2 = Thread(target=self.execute, args=("Thread Two", 2))

        self.thread1.start()
        self.thread2.start()

    def execute(self, thread_name, increment):
        self.lock.acquire()
        copy_s = self.s
        copy_s += increment
        time.sleep(0.1)
        self.s = copy_s
        self.lock.release()
        print(thread_name, copy_s)

    def join(self):
        self.thread1.join()
        self.thread2.join()


if __name__ == "__main__":
    test = ThreadingTest()
    test.join()
