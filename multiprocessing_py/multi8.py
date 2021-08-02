#การกำหนดตัวแปรสากลที่ใช้ร่วมจะต้องทำโดยใช้ mp.Value
import multiprocessing as mp 
import time

def job(a,v):
    v.value +=1
    print(v.value)

if(__name__=='__main__'):
    v = mp.Value('i',0)
    p1 = mp.Process(target=job,args=(2,v))
    p1.start()
    p2 = mp.Process(target=job,args=(3,v))
    p2.start()