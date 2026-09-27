print("CourseHub - Buoi 1")
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

for course in courses:
    remaining = course["capacity"] - course["enrolled"]
    print(course["code"], "- con", remaining, "cho")

def find_course(course_code):
    for course in courses:

        if course["code"] == course_code:
            return course
    return None

print(find_course("INT2204"))