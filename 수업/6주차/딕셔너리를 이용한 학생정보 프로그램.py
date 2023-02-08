global name
global kor, math
global avg, sum
global students

students = dict()

def read_student():
    global students, name, kor, math
    
    name = input("이름 : ")
    kor = int(input("국어점수 : "))
    math = int(input("수학점수 : "))
    
    students[name] = {"국어":kor, "수학":math, "합계":0, "평균":0.0}
    print(students)
    print(students.keys(), students.values())

def print_student():

    for key in students.keys():
        print("이름 : ", key, end="")
        print("  국어 : ", students[key]["국어"], end="")
        print("  수학 : ", students[key]["수학"], end="")
        print("  합계 : ", students[key]["합계"], "평균 : ", students[key]["평균"])

def compute_score():
    global students

    for key in students.keys():
        print("이름 : ", key)
        print("국어 : ", students[key]["국어"])
        print("수학 : ", students[key]["수학"])
        students[key]["합계"] = students[key]["국어"] + students[key]["수학"]
        students[key]["평균"] = students[key]["합계"] / 2

for i in range(2):
    read_student()
    compute_score()
    print_student()
