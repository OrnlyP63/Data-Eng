import multiprocessing as mp 
import time

def job(a):
    return [a,a**2,a**3]

if(__name__=='__main__'):
    pool = mp.Pool(processes=1)
    a = pool.apply_async(job,(2,))
    b = pool.apply_async(job,(3,))
    print(a.get())
    print(b.get())