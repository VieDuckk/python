import mysql.connector

# Kết nối MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

# Lấy danh sách khóa học, sắp xếp giảm dần và tính tổng tín chỉ
cursor.execute("""
    SELECT course_name, credits
    FROM courses
    ORDER BY credits DESC
    LIMIT 5
""")
courses = cursor.fetchall()

print("Danh sách các khóa học (5 đầu tiên):")
total_credits = 0
for course in courses:
    print(f"Khóa học: {course[0]}, Tín chỉ: {course[1]}")
    total_credits += course[1]

print(f"Tổng số tín chỉ: {total_credits}")


# Đếm số lượng sinh viên theo từng khóa học, su dung COUNT & GROUPBY
cursor.execute("""
    SELECT e.course_id, COUNT(e.student_id) AS student_count
    FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    GROUP BY e.course_id
    ORDER BY student_count DESC
""")
course_stats = cursor.fetchall()

print("Số lượng sinh viên theo từng khóa học:")
for stat in course_stats:
    print(f"Khóa học ID: {stat[0]}, Số lượng sinh viên: {stat[1]}")

# Tính điểm trung bình của mỗi khóa học và su dung HAVING de lọc điểm >= 7
cursor.execute("""
    SELECT e.course_id, c.course_name, AVG(e.grade) AS avg_grade
    FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    GROUP BY e.course_id
    HAVING avg_grade >= 7
""")
average_grades = cursor.fetchall()

print("Danh sách các khóa học có điểm trung bình từ 7 trở lên:")
for course in average_grades:
    print(f"Khóa học ID: {course[0]}, Tên: {course[1]}, Điểm trung bình: {course[2]:.2f}")

# Tính tổng số tín chỉ của từng sinh viên có tổng >= 10
cursor.execute("""
    SELECT s.student_id, s.name, SUM(c.credits) AS total_credits
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    GROUP BY s.student_id
    HAVING total_credits >= 10
    ORDER BY total_credits DESC
""")
student_credits = cursor.fetchall()

print("Danh sách sinh viên và tổng số tín chỉ:")
for student in student_credits:
    print(f"ID: {student[0]}, Tên: {student[1]}, Tổng tín chỉ: {student[2]}")

import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Kết nối MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

def show_student_details(event):
    selected_index = student_listbox.curselection()
    if not selected_index:
        return
    
    student_id = student_ids[selected_index[0]]
    cursor.execute("""
        SELECT s.name, s.age, c.course_name, c.credits, e.grade
        FROM students s
        JOIN enrollments e ON s.student_id = e.student_id
        JOIN courses c ON e.course_id = c.course_id
        WHERE s.student_id = %s
    """, (student_id,))
    details = cursor.fetchall()

    course_listbox.delete(0, tk.END)
    total_credits = 0
    total_grade = 0
    for detail in details:
        course_listbox.insert(tk.END, f"Môn: {detail[2]}, Tín chỉ: {detail[3]}, Điểm: {detail[4]}")
        total_credits += detail[3]
        total_grade += detail[4]

    average_grade = total_grade / len(details) if details else 0
    summary_label.config(text=f"Tổng tín chỉ: {total_credits}, Điểm TB: {average_grade:.2f}")

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Quản lý Sinh viên và Môn học")

# Danh sách sinh viên
student_frame = tk.Frame(root)
student_frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(student_frame, text="Danh sách Sinh viên").pack()

student_listbox = tk.Listbox(student_frame, height=15, width=30)
student_listbox.pack()
student_listbox.bind("<<ListboxSelect>>", show_student_details)

cursor.execute("SELECT student_id, name FROM students")
students = cursor.fetchall()
student_ids = []
for student in students:
    student_listbox.insert(tk.END, student[1])
    student_ids.append(student[0])

# Danh sách môn học
course_frame = tk.Frame(root)
course_frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(course_frame, text="Danh sách Môn học").pack()

course_listbox = tk.Listbox(course_frame, height=15, width=50)
course_listbox.pack()

# Tổng kết
summary_frame = tk.Frame(root)
summary_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

summary_label = tk.Label(summary_frame, text="Tổng tín chỉ: 0, Điểm TB: 0.0")
summary_label.pack()

root.mainloop()
