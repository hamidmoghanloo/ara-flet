import psycopg2

# اتصال به دیتابیس
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# ساخت جدول
cursor.execute("""
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        father_name VARCHAR(50),
        age INTEGER,
        national_code VARCHAR(10),
        city VARCHAR(50),
        phone VARCHAR(15),
        average FLOAT
    );
""")

# وارد کردن اطلاعات دانش‌آموزان
cursor.execute("""
    INSERT INTO students
    (first_name, last_name, father_name, age,
     national_code, city, phone, average)
    VALUES
    ('Ali', 'Ahmadi', 'Reza', 19, '1234567890', 'Tehran', '09120000001', 18.5),
    ('Reza', 'Karimi', 'Hassan', 20, '1234567891', 'Shiraz', '09120000002', 17.5),
    ('Sara', 'Mohammadi', 'Ali', 18, '1234567892', 'Isfahan', '09120000003', 19.2),
    ('Amir', 'Hosseini', 'Mahmoud', 21, '1234567893', 'Tabriz', '09120000004', 16.8),
    ('Neda', 'Rahimi', 'Mehdi', 19, '1234567894', 'Mashhad', '09120000005', 20.0);
""")

# ذخیره تغییرات
conn.commit()

# دریافت اطلاعات
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

# نمایش اطلاعات
for student in students:
    print(student)

# بستن اتصال
cursor.close()
conn.close()