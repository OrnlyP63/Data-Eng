#ถ้าจะตรวจสอบว่าภารกิจนั้นทำไปเสร็จหรือยังก็ทำได้โดยใช้เมธอด .done() เช่นทำแบบนี้ก็จะป้องกันการเกิดข้อผิดพลาดได้

import asyncio

async def khunlek(a,b):
  return a*b

async def main():
  task = asyncio.create_task(khunlek(3.5,2))
  if(task.done()):    
      print(task.result())
  else:
      print('ยังไม่เสร็จเลย')

asyncio.run(main())