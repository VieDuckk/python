import sqlite3

#tao co so du lieu va bang students
def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        major TEXT
    )
    ''')
    conn.commit()
    conn.close()
# ham them sinh vien moi vao bang
def add_student(name, age, major):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (name, age, major) VALUES (?, ?, ?)
    ''', (name, age, major))
    conn.commit()
    conn.close()

#ham lay toan bo danh sach sinh vien 
def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM students
    ''')
    students = cursor.fetchall()
    conn.close()
    return students
 # ham tim kiem sinh vien theo nganh
def search_students_by_major(major):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(' SELECT * FROM students WHERE major = ?', (major,))
    students = cursor.fetchall()
    conn.close()
    return students 

def main(): 
    create_database()
    while True: 
        print("\n=== Quan ly sinh vien ===")
        print("1. Them sinh vien")
        print("2. Hien thi danh sach sinh vien")
        print("3. Tim kiem sinh vien theo nganh")
        print("4. Thoat")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            name = input("Nhap ten:")
            age = int(input("Nhap tuoi:"))
            major = input("Nhap nganh :")
            add_student(name, age, major)
            print("Them sinh vien thanh cong")
        elif choice == "2":
            students = get_students()
            print("Danh sach sinh vien:")
            for student in students:
                print(f"ID: {student[0]}, Ten: {student[1]}, Tuoi: {student[2]}, Nganh: {student[3]}")
        elif choice == "3":
            major = input("Nhap nganh can tim:")
            students = search_students_by_major(major)
            print("danh sach can tim")
            for student in students:
                print(f"ID: {student[0]}, Ten: {student[1]}, Tuoi: {student[2]}, Nganh: {student[3]}")
        elif choice == "4":
            print("Thoat")
            break 
        else:
            print("Lua chon khong hop le")
if __name__ == "__main__":
    main()

