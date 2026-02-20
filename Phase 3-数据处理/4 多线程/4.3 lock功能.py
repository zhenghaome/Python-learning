# 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
import threading

# 用 lock 能使两个线程互不干扰
def func1():
    global A, lock   # A 是全局变量，如果不用lock，两个线程就会同时对A操作
    lock.acquire()   # 要执行的代码前面放一个锁
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()   # 执行完了再放一个锁，这样中间的代码就被锁住了

def func2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()

A = 0
lock = threading.Lock()
t1 = threading.Thread(target = func1)
t2 = threading.Thread(target = func2)
t1.start()
t2.start()
t1.join()
t2.join()