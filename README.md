# ScreenAutoClick
สคริปสำหรับงานคลิกเมาส์บนหน้าจออัตโนมัติ 

![Git](https://img.shields.io/github/v/release/NutCrazypanda/ScreenAutoClick) ![Git](https://img.shields.io/github/downloads/NutCrazypanda/ScreenAutoClick/total?color=green)

## Installation
1.  ดาวน์โหลดและติดตั้ง python เวอร์ชั่น 3 ขึ้นไป.
2.  Clone git หรือดาวน์โหลดไฟล์ sourcecode จากที่นี่
3.  เปิด Terminal แล้วไปยัง Folder ที่เก็บ sourcecode จากนั้นรันคำสั่ง  `pip3 install -r requirements.txt`

## วิธีการใช้งาน
1. รันไฟล์ findposition.py ด้วยคำสั่ง `python findposition.py`
2. การบันทึกตำแหน่งคลิกบนหน้าจอ (หากเคยบันทึกแล้วไม่มีการแก้ไขค่า สามารถข้ามขั้นตอนนี้ไปได้เลย)
    - กดปุ่มอักษร " s " ที่คีย์บอร์ด เพิ่มเริ่มการบันทึกตำแหน่งและเริ่มจับเวลา delay ในการคลิกแต่ละครั้ง
    - ลากเมาส์ไปในตำแหน่งที่ต้องการ จากนั้นกดปุ่มอักษร " c " ที่คีย์บอร์ด เพิ่มบันทึกตำแหน่งที่คลิก และระยะเวลาดีเลย์ 
    
      Update : สามารถคลิกเมาส์ตาม Step ที่ต้องการได้เลยไม่ต้องกดปุ่ม "c" ก็ได้ และสามารถใช้ scroll mouse ร่วมด้วยได้
    - กด ESC เมื่อต้องการจบการบันทึก โปรแกรมจะทำการบันทึกตำแหน่งคลิกบนหน้าจอและเซฟเก็บไว้ที่ไฟล์ Coordinates.txt

    ![image](https://user-images.githubusercontent.com/56244402/142717508-046a58ff-f314-4e3b-981c-13b43e500433.png)
    
3. รันไฟล์ autoClick.py เพื่อเริ่มทำงานด้วยคำสั่ง `python autoClick.py` เมื่อพร้อมแล้วให้กดปุ่ม " s " เพื่อสั่งให้โปรแกรมเริ่มทำงาน
    - หากไม่กำหนดไฟล์ที่เก็บตำแหน่งหน้าจอ โปรแกรมจะอ่านไฟล์ coordinates.txt เป็นค่าเริ่มต้น
    - ถ้าต้องการแยกไฟล์ตำแหน่งสำหรับการคลิก สามารถเรียกใช้ด้วยการเพิ่มพารามิเตอร์ -f <ชื่อไฟล์เก็บตำแหน่ง> 
    
      `python autoClick.py -f coordinates_2.txt` 
      
      ![image](https://user-images.githubusercontent.com/56244402/142723004-4f5948b0-40fa-4ce5-9f82-40122bbc6435.png)

      หากต้องการหน่วงเวลาการทำงานในแต่ละรอบ ให้กำหนดค่าช่วงเวลาได้ เช่น ต้องการให้คลิกตามที่บันทึกไว้ทุกๆ 30 วินาที ให้ใส่เลข 30 แต่ถ้าต้องการให้วนคลิกไปเรื่อยๆ ไม่รอเวลาให้ใส่ 0
      
      `Do auto click every(sec) [enter 0 for no timer] : 0`
      
      
4. หากต้องการหยุดการ Auto click ให้กดปุ่ม "ESC" ที่คีย์บอร์ด

**Note: autoClick.py จะทำงานวนไปเรื่อยๆ จนกว่าจะกดปุ่ม "ESC" ควรคำนวนเวลา Delay ระหว่างคลิกสุดท้าย กับ คลิกแรกสุดด้วย

## Support
กดติดตามเป็นกำลังใจช่องเกมของผมได้ที่ 

[![Youtube_Badge](https://img.shields.io/badge/Youtube-CrazypandaGaming-red)](https://www.youtube.com/channel/UC9PgjH7Bc0_P4tbc8c6K25Q)
[![Facebook Badge](https://img.shields.io/badge/Facebook-CrazypandaGaming-blue)](https://fb.com/crazypandagaming)

หรือช่วยสนับสนุนค่ากาแฟก็ยินดีนะครับ BTC : bc1qtczemkkmqdle9n838la3sk407jgzqx2ap03dtg

