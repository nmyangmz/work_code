import queue,sys
import my_py
import time,random
import threading
def do_craw(p_url_queue:queue.Queue,c_html_queue:queue.Queue):
    while True:
        v_url=p_url_queue.get()
        v_html=my_py.craw(v_url)
        c_html_queue.put(v_html)
        print(threading.current_thread().name,f"craw_{v_url}",f"queue_size_{p_url_queue.qsize()}")
        time.sleep(random.randint(1,2))

def do_pasers(c_html_queue:queue.Queue,fout):
    while True:
        v_html=c_html_queue.get()
        res=my_py.parse(v_html)
        for r in res:
            fout.write(str(r)+"\n")
        print(threading.current_thread().name,f"pasers_{res}",f"queue_size_{c_html_queue.qsize()}")
        time.sleep(random.randint(1,2))

if __name__=="__main__":
    p_url_queue=queue.Queue()
    c_html_queue=queue.Queue()

    for url in my_py.urls:
        p_url_queue.put(url)

    for idx in range(3):
        t=threading.Thread(target=do_craw,args=(p_url_queue,c_html_queue),name=f"craw{idx}")

        t.start()

    f=open("e:/01.data.txt","w")

    for idx in range(3):
        t=threading.Thread(target=do_pasers,args=(c_html_queue,f),name=f"parser{idx}")

        t.start()




