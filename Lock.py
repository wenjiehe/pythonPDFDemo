from time import sleep, time
from threading import Thread, Lock

#加入锁来保护"临界资源"，没有得到锁的线程只能被阻塞起来，直到获得锁的线程释放了锁，其他线程才有机会获得锁，进而访问被保护的"临界资源"
class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
    for t in threads:
        t.start()
        t.join()
    print('账户余额为:%d元' % account.balance)

if __name__ == '__main__':
    main()