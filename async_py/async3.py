#เพื่อที่จะเรียกให้ฟังก์ชันในภารกิจทำงานและคืนค่าออกมาทันที จะใช้คำสั่ง await แบบนี้

import asyncio

async def buaklek(a,b):
    c = a+b
    print('==ฟังก์ชันเริ่มทำงาน==')
    return c

async def main():
    coru = buaklek(13,10)
    task = asyncio.create_task(coru)
    phonbuak = await task
    print('ได้ผลบวก %s'%phonbuak)

maincoru = main()
asyncio.run(maincoru)

#ครั้งนี้ฟังก์ชันของภารกิจ task ถูกสั่งให้ทำงานโดยตรงด้วยคำสั่ง await จึงทำงานในจังหวะนั้นตรงนั้นเลย และจะให้ค่าคำตอบออกมา

#await ในที่นี้เป็นรูปแบบไวยากรณ์ใหม่ เช่นเดียวกับ async ไม่ใช่ฟังก์ชัน จึงไม่ต้องใส่วงเล็บ () และมีวิธีใช้ที่ตายตัว คือเขียน await ตามด้วยออบเจ็กต์ภารกิจที่ต้องการให้ทำงาน