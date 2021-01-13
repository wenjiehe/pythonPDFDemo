from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
from threading import Thread

#继承Thread类
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成!耗费了%d秒' % (self._filename, time_to_download))


# def download_task(fileName):
#     print('开始下载%s...' % fileName)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成!耗费了%d秒' % (fileName, time_to_download))

def main():
    #使用Process建立进程
    #注意:当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间
    # start = time()
    # p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    # p1.start()
    # p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    # p2.start()
    # p1.join()
    # p2.join()
    # end = time()
    # print('总共耗费了%.2f秒' % (end - start))

    #使用Thread建立线程
    # start = time()
    # t1 = Thread(target=download_task, args=('Python从入门到住院.pdf', ))
    # t1.start()
    # t2 = Thread(target=download_task, args=('Peking Hot.avi', ))
    # t2.start()
    # t1.join()
    # t2.join()
    # end = time()
    # print('总共耗费了%.3f秒' % (end - start))


    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()