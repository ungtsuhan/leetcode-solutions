"""
Date        : 8 August 2021
Runtime     : 36 ms, faster than 84.98% of Python3 online submissions for Print in Order.
Memory Usage: 14.7 MB, less than 65.81% of Python3 online submissions for Print in Order.
"""

from typing import Callable
from threading import Lock

class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        
        self.lock1.acquire() # initialize the state to locked
        self.lock2.acquire() # initialize the state to locked


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        self.lock1.acquire()

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.lock2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.lock2.acquire()

        # printThird() outputs "third". Do not change or remove this line.
        printThird()

        self.lock2.release()