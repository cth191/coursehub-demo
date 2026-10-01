#1
print("CourseHub - Buoi 1")
#2
students = [
{"id": "24001668", "name": "Cao Trung Hieu", "major": "KHDL"},
{"id": "24001722", "name": "Nguyen Son Tung", "major": "KHDL"},
]
courses = [
{
"code": "INT2204",
"name": "Co so du lieu Web va he thong thong tin",
"capacity": 3,
"enrolled": 2,
},
{
"code": "INT2205",
"name": "Khai pha du lieu",
"capacity": 2,
"enrolled": 2,
},
]
enrollments = [
{"student_id": "24001683", "course_code": "INT2204"}
]
#4
for course in courses:
    remaining = course["capacity"] - course["enrolled"]
    print(course["code"], "- con", remaining, "cho")
#5
def find_course(course_code):
    for course in courses:

        if course["code"] == course_code:
            return course
    return None

print(find_course("INT2204"))
#6
def can_enroll(student_id, course_code):
    course = find_course(course_code)

    if course is None:
        return False, "Hoc phan khong ton tai"

    duplicated = any(
            item["student_id"] == student_id and item["course_code"] == course_code
            for item in enrollments
        )
    if duplicated:
            return False, "Sinh vien da dang ky hoc phan nay"
    if course["enrolled"] >= course["capacity"]:
        return False, "Lop da du so luong"
    
    
        
    return True, "Co the dang ky"
print(can_enroll("22000002", "INT2204"))
#7
try:
    limit = int(input("Nhap so luong hoc phan muon hien thi: "))
    print(courses[:limit])
except ValueError:
    print("So luong phai la so nguyen")
#8
def search_courses(keyword):
    normalized = keyword.strip().lower()
    results = []

    for course in courses:
        code = course["code"].lower()
        name = course["name"].lower()
        if normalized in code or normalized in name:
            results.append(course)

    return results

print(search_courses("web"))
#btvn
#1.code enroll_student
def enroll_student(student_id, course_code):
    student_exists = any(student["id"] == student_id for student in students)
    if not student_exists:
        return False, "Sinh viên không tồn tại"
    
    allowed, message = can_enroll(student_id, course_code)
    if not allowed:
        return False, message
    
    enrollments.append({"student_id": student_id, "course_code": course_code})
    course = find_course(course_code)
    course["enrolled"] += 1

    return True, "Đăng kí học phần thành côngg"

#2.tạo 5th kiểm tra
print("\n--- KIỂM TRA CHƯƠNG TRÌNH (5 TÌNH HUỐNG) ---")

print("1. Dang ky thanh công:", enroll_student("24001668", "INT2204"))

print("2. Dang ky trùng:", enroll_student("24001668", "INT2204"))

print("3. Lop day:", enroll_student("24001668", "INT2205"))

print("4. Hoc phan khong ton tai:", enroll_student("24001668", "INT9999"))

print("5. Sinh vien khong ton tai:", enroll_student("99999999", "INT2204"))
