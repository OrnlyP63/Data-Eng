#ถ้าฟังก์ชันมีการ return คืนค่า นอกจากจะเอาค่าด้วย await แล้ว ยังสามารถเอาค่านั้นได้โดยใช้เมธอด .result()

import asyncio

async def khunlek(a,b):
    return a*b

async def main():
    task = asyncio.create_task(khunlek(17,4))
    await task
    print(task.result()) # ได้ 68

asyncio.run(main())

#แต่ถ้าภารกิจนั้นยังไม่ได้ทำงานจนจบก็จะไม่มีผลลัพธ์ออกมา เมื่อใช้ .result() ก็จะเกิดข้อผิดพลาด
#awiat คือ ทำให้ task ทำงานจนเสร็จแล้วคืนค่า