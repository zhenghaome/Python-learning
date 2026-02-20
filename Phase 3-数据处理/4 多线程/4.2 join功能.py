import threading
import time

def thread1():
    print('t1 start\n')
    time.sleep(2)   # 故意让T1等两秒，看看哪个线程先结束
    print('t1 finish\n')

def thread2():
    print('t2 start\n')
    print('t2 finish\n')

def main():
    added_thread1 = threading.Thread(target = thread1)
    added_thread2 = threading.Thread(target=thread2)
    added_thread1.start()   # 没有 join，几个线程会同时进行但是随机结束
    added_thread2.start()
    added_thread1.join()   # join 使得t1运行完之后主线程再结束
    print('all done')

if __name__ == '__main__':
    main()