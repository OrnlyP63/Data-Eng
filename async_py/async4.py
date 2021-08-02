#await นอกจากจะใช้กับภารกิจแล้วยังใช้กับโครูทีนโดยตรงได้เลย ในกรณีนี้ภารกิจจะถูกสร้างขึ้นจากโครูทีนโดยอัตโนมัติแล้วก็ทำงานทันที
import asyncio 

async def buaklek(a,b):
    return a+b

async def main():
    phonbuak = await buaklek(13,10)
    print('ได้ผลบวก %s'%phonbuak)

asyncio.run(main())