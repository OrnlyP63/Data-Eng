#ถ้าหากเป็นอะซิงโครนัสจะมีการใช้ตัวประมาณผลแค่ตัวเดียว ดังนั้นส่วนที่ใช้ CPU (สีแดง) จะซ้อนทับกันไม่ได้ ตรงขั้นตอนการรอรับส่งข้อมูล (สีม่วง) จะซ้อนกันก็ไม่เป็นอะไร ดังนั้นสามารถจัดสรรให้สลับการทำงานไปทำแต่ละงานโดยพยายามให้ CPU ได้ใช้งานตลอดก็จะเป็นแบบนี้

#ฟังก์ชันที่สร้างขึ้นด้วย async def จะเรียกว่าเป็น "ฟังก์ชันโครูทีน" (coroutine function) 

import asyncio

async def buaklek(a,b):
    return a+b

print(buaklek) # ได้ <function buaklek at 0x11c7a8710>
print(type(buaklek)) # ได้ <class 'function'>
coru = buaklek(5,4)
print(coru) # ได้ <coroutine object buaklek at 0x11c7a87a0>
print(type(coru)) # ได้ <class 'coroutine'>

phonbuak = asyncio.run(coru) # ทำการรันโครูทีนเพื่อให้ฟังก์ชันทำงาน
print('ผลบวก: %s'%phonbuak) # ได้ ผลบวก: 9