import asyncio,time

async def ioioio(wela,chue_ngan):
    print('เริ่ม%s เวลาผ่านไปแล้ว %.5f วินาที'%(chue_ngan,time.time()-t0))
    await asyncio.sleep(wela)
    print('%sเสร็จแล้ว เวลาผ่านไปแล้ว %.5f วินาที'%(chue_ngan,time.time()-t0))
    return

async def main():
    print('เริ่มต้นฟังก์ชัน')
    phara1 = asyncio.create_task(ioioio(1.5,'โหลดเพลง'))
    phara2 = asyncio.create_task(ioioio(2.5,'โหลดอนิเมะ'))
    phara3 = asyncio.create_task(ioioio(0.5,'โหลดหนัง'))
    print('สร้างภารกิจเสร็จแล้ว')
    await phara2
    print('สิ้นสุดฟังก์ชัน')

t0 = time.time()
asyncio.run(main())

#ในที่นี้เราได้ใช้ asyncio.create_task() เพื่อสร้างภารกิจออกมา 3 ตัว จากนั้นเมื่อมีการใช้คำสั่ง await ให้กับตัวใดตัวหนึ่ง ภารกิจทั้ง 3 ก็จะเร่ิมขึ้นทันที

#เมื่อคำสั่งที่ถูกสั่ง await นั่นคือโหลดอนิเมะเสร็จ ฟังก์ชันก็จะสิ้นสุดลง

#ในการใช้งานจริงเราคงไม่อาจรู้ได้แน่ชัดว่างานไหนจะเสร็จก่อนดังนั้นวิธีเขียนแบบนี้จึงไม่เหมาะจะ.ใช้จริง