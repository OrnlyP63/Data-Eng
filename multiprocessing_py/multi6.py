import multiprocessing as mp 

def job(a,b,q):
    q.put(a*b)
    q.put(a**b)

if(__name__=='__main__'):
    q = mp.Queue()
    p = mp.Process(target=job,args=(2,3,q))
    p.start()
    print(q.get())
    print(q.get())