import multiprocessing as mp

def job():
    print('เริ่มทำงาน')
    for i in range(1000000):
        2**2
    print('งานเสร็จแล้ว')


if(__name__=='__main__'):
    p = mp.Process(target=job)
    p.start()
    print('สั่งงาน')