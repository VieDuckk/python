import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["stores"]
invoices_collection = db["invoices"]

#ham them hoa don 
def add_invoice(customer_name, items):
    try:
        total = sum(item["quantity"] * item["price"] for item in items)
        invoice = {
            "customer_name": customer_name,
            "items": items,
            "total": total
        }
        
        invoices_collection.insert_one(invoice)
        print("Hóa đơn đã được thêm thành công!")
    except Exception as e:
        print(f"Lỗi khi thêm hóa đơn: {e}")

# ham hien thi tat ca hoa don 
def get_invoices():
    invoices = invoices_collection.find()
    if invoices_collection.count_documents({}) == 0:
        print("Không có hóa đơn nào.")
        return
    
    for invoice in invoices:
        print(f"\nCustomer: {invoice['customer_name']}")
        print("Items:")
        for item in invoice["items"]:
            print(f"Product: {item['product']}, Quantity: {item['quantity']}, Price: {item['price']}")
        print(f"TOtal: {invoice['total']}")
# ham tim hoa don theo ten khach hang
def find_invoices_by_name(customer_name):
    invoices = invoices_collection.find({"customer_name": customer_name})
    found = False 
    for invoice in invoices: 
        found = True 
        print(f"\nCustomer: {invoice['customer_name']}")
        for item in invoice["items"]:
            print(f'Product: {item['product']}, Quantity: {item['quantity']}, Price: {item['price']}')
        print(f"total: {invoice['total']}")
    if not found:
        print("khong tim thay hoa don")
#ham tinh tong doanh thu
def total_revenue():
    total_revenue = 0
    invoices = invoices_collection.find()
    for invoice in invoices: 
        total_revenue += invoice['total']
    return total_revenue 
def main(): 
    while True:
        print("\n=== Quan ly hoa don ===")
        print("1. Them hoa don ")
        print("2. Hien thi danh sach hoa don")
        print("3. Tim hoa don theo ten khach hang")
        print("4. Tinh tong doanh thu")
        print("5. Thoat")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            customer_name = input("Nhap ten khach hang:")
            num_items = int(input("nhap so lg san pham: "))
            items = []
            for _ in range(num_items):
                product = input("Ten san pham :")
                quantity = int(input("Nhap so luong: "))
                price = float(input("Nhap don gia: "))
                items.append({"product":product, "quantity": quantity, "price": price})
            add_invoice(customer_name, items)
        elif choice == "2":
            get_invoices()
        elif choice == "3":
            customer_name = input("nhap ten khach hang : ")
            find_invoices_by_name(customer_name)
        elif choice == "4":
            total_revenue = total_revenue()
            print(f"tong doanh thu la : {total_revenue}")
        elif choice =="5":
            print("Thoat")
            break 
        else:
            print("Lua chon khong hop le. Vui long nhap lai.")
if __name__ == "__main__":
    main()


