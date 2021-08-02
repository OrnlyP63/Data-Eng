#การจะทำให้โครูทีนทำงานจำเป็นจะต้องเปลี่ยนโครูทีนแต่โครูทีนด้านในแค่ถูกสร้างขึ้นมาเฉยๆจะยังไม่ทำงาน แต่จะทำงานได้เมื่อมีการเปลี่ยนมันเป็นสิ่งที่เรียกว่า "ภารกิจ" (task)

import asyncio
    
async def buaklek(a,b):
    c = a+b
    print('ฟังก์ชัน buaklek เริ่มทำงาน a+b=%s'%c)
    return c

async def main():
    coru = buaklek(13,10)
    task = asyncio.create_task(coru)
    print(task)
    print(type(task))
    print('สิ้นสุด main')

maincoru = main()
asyncio.run(maincoru)

#ในตัวอย่างนี้ได้สร้างฟังก์ชัน ๒ อัน โดยใช้ async ทั้งคู่ ฟังก์ชัน main มีการสร้างโครูทีนของฟังก์ชัน buaklek ขึ้น จากนั้นเอาโครูทีนมาทำเป็นภารกิจ