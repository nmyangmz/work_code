import my_py
import threading
import time

def single_tread():
    print("single_tread begin")
    for url in my_py.urls:
        my_py.craw(url)

    print("single_tread end")

def multi_tread():
    print("multi_tread begin")
    threads=[]
    for usr in my_py.urls:
        threads.append(
            threading.Thread(target=my_py.craw,args=(usr,))
        )

    for t in threads:
        t.start()

    for t1 in threads:
        t1.join()

    print("multi_tread end")


if __name__=="__main__":
    start=time.time()
    single_tread()
    end=time.time()
    print("single_tread 时间",end-start)

    start=time.time()
    multi_tread()
    end=time.time()
    print("multi_tread 时间",end-start)

