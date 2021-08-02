import multiprocessing as mp 
import time

def job(a,b,v):
    v[a] += b
    print(v[:])

if(__name__=='__main__'):
    v = mp.Array('i',[0,0,0,1])
    for i in range(4):
        p = mp.Process(target=job,args=(i,i+2,v))
        p.start()
        p.join()