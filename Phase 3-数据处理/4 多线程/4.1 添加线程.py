import threading

# 添加线程：threading.Thread(target = )
def thread_job():
    print('这是新添加的线程')

def main():
    added_thread = threading.Thread(target = thread_job)   # 添加线程
    added_thread.start()   # 启动线程

    print(threading.active_count())   # 算一下现在有多少个激活了的线程
    print(threading.enumerate())   # 显示哪几个线程在运行
    print(threading.current_thread())   # 显示一下当前正在运行哪个线程

if __name__ == '__main__':
    main()