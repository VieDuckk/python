import tkinter as tk
from tkinter import messagebox
import pymongo

# Kết nối MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["TaskManager"]
tasks_collection = db["Tasks"]

# Hàm thêm công việc
def add_task():
    title = entry_title.get()
    description = text_description.get("1.0", tk.END).strip()

    if title and description:
        task = {
            "title": title,
            "description": description,
            "status": "Chưa hoàn thành"
        }
        tasks_collection.insert_one(task)
        messagebox.showinfo("Thành công", "Công việc đã được thêm!")
        update_task_list()
    else:
        messagebox.showerror("Lỗi", "Cần nhập đầy đủ tên công việc và mô tả.")

# Hàm hiển thị danh sách công việc
def update_task_list():
    listbox_tasks.delete(0, tk.END)
    tasks = tasks_collection.find()
    for task in tasks:
        listbox_tasks.insert(tk.END, f"{task['title']} - [{task['status']}]")

# Hàm đánh dấu công việc là hoàn thành
def mark_task_done():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        task_title = listbox_tasks.get(selected_task[0]).split(" - ")[0]
        tasks_collection.update_one(
            {"title": task_title},
            {"$set": {"status": "Hoàn thành"}}
        )
        messagebox.showinfo("Thành công", "Công việc đã được đánh dấu hoàn thành!")
        update_task_list()
    else:
        messagebox.showerror("Lỗi", "Vui lòng chọn công việc cần cập nhật.")

# Hàm xóa công việc
def delete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        task_title = listbox_tasks.get(selected_task[0]).split(" - ")[0]
        tasks_collection.delete_one({"title": task_title})
        messagebox.showinfo("Thành công", "Công việc đã được xóa!")
        update_task_list()
    else:
        messagebox.showerror("Lỗi", "Vui lòng chọn công việc cần xóa.")

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Quản lý Công Việc")

# Các thành phần giao diện
label_title = tk.Label(root, text="Tên công việc:")
label_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_title = tk.Entry(root, width=30)
entry_title.grid(row=0, column=1, padx=10, pady=10)

label_description = tk.Label(root, text="Mô tả công việc:")
label_description.grid(row=1, column=0, padx=10, pady=10, sticky="w")

text_description = tk.Text(root, height=5, width=30)
text_description.grid(row=1, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Thêm công việc", width=20, command=add_task)
button_add.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

button_mark_done = tk.Button(root, text="Đánh dấu hoàn thành", width=20, command=mark_task_done)
button_mark_done.grid(row=4, column=0, padx=10, pady=10)

button_delete = tk.Button(root, text="Xóa công việc", width=20, command=delete_task)
button_delete.grid(row=4, column=1, padx=10, pady=10)

# Cập nhật danh sách công việc khi khởi động
update_task_list()

# Chạy ứng dụng Tkinter
root.mainloop()
