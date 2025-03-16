import threading

import my_py
import queue

def p_num(s_data:queue.Queue,f_data:queue.Queue):
    while True:
        data=s_data.get()

        f_data.put(data)

        print(threading.current_thread().name+" "+f"生产数据——{data}")


def c_num(f_data:queue.Queue):

    while True:

        num=f_data.get()
        xx=my_py.collect_num(num)
        print(threading.current_thread().name+" "+f"消费数据——{xx}")


if __name__=="__main__":

    v_data=queue.Queue()
    f_data=queue.Queue()

    n=my_py.getnum(my_py.list_num)

    for s in n:
        v_data.put(s)

    for i in range(3):

        t=threading.Thread(target=p_num,args=(v_data,f_data),name=f"p_num_{i}")

        t.start()

    for i in range(3):

        t=threading.Thread(target=c_num,args=(f_data,),name=f"c_num_{i}")

        t.start()

