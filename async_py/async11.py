import asyncio
import time

async def ioioio(wela,chue_ngan):
    await asyncio.sleep(wela)
    print('โหลด%sเสร็จ ผ่านไปแล้ว %.6f วินาที'%(chue_ngan,time.time()-t0))
    return chue_ngan

async def main():
    cococoru = [ioioio(1.5,'เพลง'),ioioio(2.5,'อนิเมะ'),ioioio(0.5,'หนัง'),ioioio(2,'เกม')]
    setlaeo, yangmaiset = await asyncio.wait(cococoru,timeout=1.8)
    print('---')
    print('เสร็จแล้ว %d งาน ยังไม่เสร็จอีก %d งาน'%(len(setlaeo),len(yangmaiset)))
    print('---')
    for phara in setlaeo:
        khong = await phara
        print('~%s~ เสร็จไปแล้ว'%khong)
    print('---')
    for phara in yangmaiset:
        khong = await phara
        print('~%s~ เพิ่งเสร็จ'%khong)

t0 = time.time()
asyncio.run(main())