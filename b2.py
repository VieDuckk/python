import sqlite3

#tao co so du lieu va bang products
def create_database():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS products(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   price REAL,
                   quantity INTEGER
    )
''')
    conn.commit()
    conn.close()

#them san pham vao bang 
def add_product(name, price, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)
''', (name, price, quantity))
    conn.commit()
    conn.close()

# hien thi danh sach san pham 
def get_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM products
''')
    products = cursor.fetchall()
    conn.close()
    return products

#cap nhat so luong ton kho cua 1 san pham 
def update_quantity(id, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(
        '''
        UPDATE products SET quantity = ? WHERE id = ?
        ''',
        (quantity, id)
    )
    conn.commit()
    conn.close()

# tinh tong tien
def total():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''
    SELECT SUM(price * quantity) FROM products
    ''')
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0
def main():
    create_database()
    while True:
        print("\n=== Quan ly san pham ===")
        print("1. Them san pham")
        print("2. Hien thi danh sach san pham")
        print("3. Cap nhat so luong ton kho")
        print("4. Tinh tong gia tri cua toan bo sp")
        print("5. Thoat")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            name = input("Nhap ten:")
            price = float(input("nhao don gia: "))
            quantity = int(input("Nhap so luong: "))
            add_product(name, price, quantity)
            print("Them san pham thanh cong")
        elif choice == "2":
            products = get_products()
            print("danh sach san pham: ")
            for product in products:
                print(f"ID: {product[0]}, Ten: {product[1]}, Don gia: {product[2]}, So luong: {product[3]}")
        elif choice == "3":
            id = int(input("nhap id san pham: "))
            quantity = int(input("Nhap so luong moi: "))
            update_quantity(id, quantity)
            print("Cap nhat thanh cong")
        elif choice == "4":
            total_products = total()
            print("tong gia tri san pham la:",total_products)
        elif choice == "5":
            print("Thoat")
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.")
if __name__ == "__main__":
    main()