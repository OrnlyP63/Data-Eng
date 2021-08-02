import multiprocessing as mp 
import time

def job(s,ro,q):
    time.sleep(ro)
    q.put(s)

if(__name__=='__main__'):
    q = mp.Queue()
    p1 = mp.Process(target=job,args=('p1',3,q))
    p1.start()
    p2 = mp.Process(target=job,args=('p2',2,q))
    p2.start()
    print(q.get())
    print(q.get())