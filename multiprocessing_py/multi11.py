import multiprocessing as mp 
import time

def job(a):
    for i in range(1,4):
        time.sleep(0.5)
        print(100*a+i)

# def job(a):
#     return a**2/2

if(__name__=='__main__'):
    pool = mp.Pool(processes=5)
    print(pool.map(job,[1,2,3,10,18]))