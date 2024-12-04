import mysql.connector

# Kết nối đến MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)
cursor = conn.cursor()

# Tạo cơ sở dữ liệu university_db
cursor.execute("CREATE DATABASE IF NOT EXISTS university_db")
cursor.execute("USE university_db")

# Tạo bảng students
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT
    )
""")
print("Bảng students đã được tạo.")


#BT2 TRUY VAN CO BAN
# Thêm dữ liệu vào bảng students
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (1, 'Nguyễn Văn A', 21)")
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (2, 'Trần Thị B', 19)")
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (3, 'Lê Văn C', 22)")
conn.commit()

# Lấy tất cả bản ghi từ bảng students
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

# Hiển thị kết quả dưới dạng bảng
print("Danh sách sinh viên:")
print("+-------------+----------------+-----+")
print("| student_id  | name           | age |")
print("+-------------+----------------+-----+")
for student in students:
    print(f"| {student[0]:<11} | {student[1]:<14} | {student[2]:<3} |")
print("+-------------+----------------+-----+")





# BT3  tao bang moi & sd WHERE
# Tạo bảng courses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INT PRIMARY KEY,
        course_name VARCHAR(100),
        credits INT
    )
""")

# Thêm dữ liệu vào bảng courses
cursor.execute("INSERT INTO courses (course_id, course_name, credits) VALUES (101, 'Toán Cao Cấp', 3)")
cursor.execute("INSERT INTO courses (course_id, course_name, credits) VALUES (102, 'Vật Lý Đại Cương', 4)")
cursor.execute("INSERT INTO courses (course_id, course_name, credits) VALUES (103, 'Hóa Học Đại Cương', 2)")
conn.commit()

# Lấy các khóa học có số tín chỉ > 2
cursor.execute("SELECT * FROM courses WHERE credits > 2")
courses = cursor.fetchall()

print("Khóa học có tín chỉ > 2:")
for course in courses:
    print(f"ID: {course[0]}, Tên: {course[1]}, Tín chỉ: {course[2]}")



# BT4Kết hợp nhiều điều kiện với WHERE
# Thêm thêm dữ liệu vào bảng students
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (4, 'Phạm Minh D', 20)")
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (5, 'Hoàng Thị E', 23)")
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (6, 'An Văn F', 18)")
conn.commit()

# Lấy sinh viên có tuổi > 20
cursor.execute("SELECT * FROM students WHERE age > 20")
print("Sinh viên có tuổi > 20:")
for student in cursor.fetchall():
    print(student)

# Lấy sinh viên có tên bắt đầu bằng 'A' hoặc tuổi < 22
cursor.execute("SELECT * FROM students WHERE name LIKE 'A%' OR age < 22")
print("Sinh viên có tên bắt đầu bằng 'A' hoặc tuổi < 22:")
for student in cursor.fetchall():
    print(student)




# BT5 SAP XEP KQ VOI ORDER BY
# Thêm thêm dữ liệu vào bảng courses
cursor.execute("INSERT INTO courses (course_id, course_name, credits) VALUES (104, 'Tin Học Cơ Bản', 3)")
cursor.execute("INSERT INTO courses (course_id, course_name, credits) VALUES (105, 'Văn Học Việt Nam', 2)")
conn.commit()

# Sắp xếp khóa học theo số tín chỉ tăng dần
cursor.execute("SELECT * FROM courses ORDER BY credits ASC")
print("Khóa học sắp xếp theo tín chỉ tăng dần:")
for course in cursor.fetchall():
    print(course)

# Sắp xếp khóa học theo tên giảm dần
cursor.execute("SELECT * FROM courses ORDER BY course_name DESC")
print("Khóa học sắp xếp theo tên giảm dần:")
for course in cursor.fetchall():
    print(course)




# BT6 Truy vấn kết hợp WHERE và ORDER BY
# Thêm thêm bản ghi vào bảng students
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (7, 'Bùi Văn G', 21)")
cursor.execute("INSERT INTO students (student_id, name, age) VALUES (8, 'Nguyễn Thị H', 22)")
conn.commit()

# Lấy sinh viên có tuổi từ 18 đến 22, sắp xếp theo tuổi tăng dần
cursor.execute("SELECT * FROM students WHERE age BETWEEN 18 AND 22 ORDER BY age ASC")
print("Sinh viên có tuổi từ 18 đến 22, sắp xếp theo tuổi tăng dần:")
for student in cursor.fetchall():
    print(student)

# Lấy sinh viên có tên chứa chữ 'e', sắp xếp theo tên
cursor.execute("SELECT * FROM students WHERE name LIKE '%e%' ORDER BY name ASC")
print("Sinh viên có tên chứa chữ 'e', sắp xếp theo tên:")
for student in cursor.fetchall():
    print(student)
