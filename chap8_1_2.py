# chap8_1_1.py 를 객체 형식으로 변환

# 딕셔너리를 리턴하는 함수를 선언
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(Student):
    return student_get_sum(student) / 4

def student_tostring(Student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

# 학생 리스트 생성
students = [
    { "name" : "윤인성", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
    { "name" : "연하진", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
    { "name" : "구지연", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
    { "name" : "나선주", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
    { "name" : "윤아린", "korean" : 95, "math" : 98, "english" : 98, "science" : 98}
]

# 메인
print("이름", "총점", "평균", sep = "\t")
for student in students:
    print(student_tostring(student))