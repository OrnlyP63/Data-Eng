#หากมีคำสั่งบางอย่างที่ต้องการรอให้งานที่สั่งไปเสร็จก่อนแล้วค่อยทำ จำเป็นจะต้องใช้เมธอด join
import multiprocessing as mp 
import time

def job(a):
    for i in range(2):
        time.sleep(0.5)
        print('งานที่ %d รอบที่ %d'%(a,i+1))

if(__name__=='__main__'):
    pp = []
    for j in range(4):
        p = mp.Process(target=job,args=(j+1,))
        p.start()
        pp.append(p)
    print('เริ่มงานได้แล้ว')
    for p in pp:
        p.join()
    print('เก็บกวาดหลังเลิกงาน')