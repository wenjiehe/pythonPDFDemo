from multiprocessing import Process, Queue
from random import randint
from time import time

#把1-1000001求和的计算密集型任务，利用多进程进行"分而治之"
def task_handler(cur_list, result_queue):
    total = 0
    for number in cur_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    result_queue = Queue()
    index = 0
    number_list = [x for x in range(1, 1000001)]
    numberTotal = 0
    startTime = time()
    for number in number_list:
        numberTotal += number
    print(numberTotal)
    endTime = time()
    print(endTime - startTime)
    #启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index + 125000], result_queue))
        index += 125000
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    #合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time:', (end - start), 's', sep='')

if __name__ == '__main__':
    main()