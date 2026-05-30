import json
import os

FILE_NAME = "data.json"
student_list = []

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(student_list, f, indent=4)

def get_rank(avg_score):
    if avg_score < 5.0: return "Yếu"
    elif avg_score < 7.0: return "Trung Bình"
    elif avg_score < 8.0: return "Khá"
    else: return "Giỏi"

def display_all():
    print(f"\n{'Mã SV':<10} | {'Tên':<20} | {'ĐTB':<8} | {'Xếp loại'}")
    for s in student_list:
        print(f"{s['id']:<10} | {s['name']:<20} | {s['avg_score']:<8.2f} | {s['rank']}")

def add_student():
    sid = input("Nhập Mã SV: ")
    if any(s['id'] == sid for s in student_list):
        print("Mã đã tồn tại!")
        return
    name = input("Nhập Tên: ")
    math = float(input("Điểm Toán: "))
    phys = float(input("Điểm Lý: "))
    chem = float(input("Điểm Hóa: "))
    avg = (math + phys + chem) / 3
    student_list.append({"id": sid, "name": name, "avg_score": avg, "rank": get_rank(avg)})
    save_data()
    print("Thêm thành công!")

def update_student():
    sid = input("Nhập Mã SV cần sửa: ")
    for s in student_list:
        if s['id'] == sid:
            s['avg_score'] = float(input("Nhập ĐTB mới: "))
            s['rank'] = get_rank(s['avg_score'])
            save_data()
            return
    print("Không tìm thấy!")

def delete_student():
    sid = input("Nhập Mã SV cần xóa: ")
    for i, s in enumerate(student_list):
        if s['id'] == sid:
            if input(f"Bạn có chắc muốn xóa {s['name']}? (y/n): ").lower() == 'y':
                student_list.pop(i)
                save_data()
                print("Đã xóa sinh viên thành công!")
            return
    print("Không tìm thấy!")

def search_student():
    key = input("Nhập tên hoặc mã: ").lower()
    for s in student_list:
        if key in s['id'].lower() or key in s['name'].lower():
            print(f"Tìm thấy: {s['name']} - ĐTB: {s['avg_score']}")

def sort_students():
    choice = input("1. ĐTB giảm dần | 2. Tên A-Z: ")
    if choice == '1': student_list.sort(key=lambda x: x['avg_score'], reverse=True)
    else: student_list.sort(key=lambda x: x['name'])
    display_all()

def stats():
    ranks = {"Giỏi": 0, "Khá": 0, "Trung Bình": 0, "Yếu": 0}
    for s in student_list: ranks[s['rank']] += 1
    print(f"\nThống kê: {ranks}")

def min_max():
    if not student_list: return
    best = max(student_list, key=lambda x: x['avg_score'])
    worst = min(student_list, key=lambda x: x['avg_score'])
    print(f"Cao nhất: {best['name']} ({best['avg_score']})")
    print(f"Thấp nhất: {worst['name']} ({worst['avg_score']})")

def classify():
    for s in student_list:
        print(f"{s['name']}: {s['rank']}")

def menu():
    global student_list
    student_list = load_data()
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ SINH VIÊN ---")
        print("1.  Hiển thị danh sách sinh viên")
        print("2.  Thêm mới sinh viên")
        print("3.  Cập nhật thông tin sinh viên")
        print("4.  Xoá sinh viên")
        print("5.  Tìm kiếm sinh viên")
        print("6.  Sắp xếp danh sách sinh viên")
        print("7.  Thống kê điểm TB")
        print("8.  Liệt kê sinh viên có điểm TB cao nhất / thấp nhất")
        print("9.  Phân loại học lực sinh viên")
        print("10. Thoát")
        
        choice = input("\nNhập lựa chọn của bạn (1-10): ")
        
        if choice == '1': display_all()
        elif choice == '2': add_student()
        elif choice == '3': update_student()
        elif choice == '4': delete_student()
        elif choice == '5': search_student()
        elif choice == '6': sort_students()
        elif choice == '7': stats()
        elif choice == '8': min_max()
        elif choice == '9': classify()
        elif choice == '10': break
        else: print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()