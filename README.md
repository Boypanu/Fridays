# README.md

## วิธีการติดตั้งและใช้งานโปรเจกต์นี้

1. **Clone โปรเจกต์จาก GitHub**

   เปิด Command Prompt หรือ Terminal แล้วรันคำสั่งนี้ (เปลี่ยน `your-username` และ `your-repo` ให้ตรงกับ repository จริง):

   ```
   git clone https://github.com/Boypanu/Friday.git
   ```

2. **เข้าไปในโฟลเดอร์โปรเจกต์**

   ```
   cd Friday
   ```

3. **ติดตั้ง dependencies ที่จำเป็น**

   แนะนำให้ใช้ Python virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **รันแอปพลิเคชัน**

   ```
   python app.py
   ```

5. **ทดสอบ API**

   เปิดเบราว์เซอร์หรือใช้โปรแกรมเช่น Postman ไปที่  
   [http://localhost:5001/api2](http://localhost:5001/api2)

---
**หมายเหตุ:**  
- ตรวจสอบให้แน่ใจว่าติดตั้ง Python เวอร์ชัน 3.7 ขึ้นไป
- หากยังไม่มีไฟล์ `requirements.txt` ให้เพิ่มชื่อไลบรารีที่ใช้

# Two APIs with Docker Compose

## 📦 Setup

1. Clone this repository
2. Run:

   ```bash
   docker-compose up --build
   ```
