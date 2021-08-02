import asyncio
#ตั้งช่อให้กับ task

async def thamkapkhao():
    return 'กับข้าว'

async def main():
    task = asyncio.create_task(thamkapkhao())
    print('โครูทีน: %s'%task.get_coro())
    print('ชื่อภารกิจ: '+task.get_name())
    print('---ตั้งชื่อ---')
    task.set_name('ทำกับข้าว')
    print('ชื่อภารกิจ: '+task.get_name())

asyncio.run(main())