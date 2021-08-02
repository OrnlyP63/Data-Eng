#ภารกิจสามารถถูกสร้างขึ้นโดยตรงได้จากการสร้างอินสแตนซ์ของคลาส asyncio.tasks.Task โดยป้อนโครูทีนเข้าไปเช่น

import asyncio

async def khunlek(a,b):
    print('%s × %s = %s'%(a,b,a*b))

async def main():
    task = asyncio.tasks.Task(khunlek(4,28))
    print(task)

asyncio.run(main())

#แต่ปกติจะไม่แนะนำให้ทำอย่างนั้น โดยทั่วไปจะแนะนำให้สร้างขึ้นด้วย asyncio.create_task() มากกว่า
