global name
global kor, math, eng
global avg, sum

def read_student():
    global name
    global kor
    global math
    global eng

    name = input("이름을 입력하시오 : ")
    kor = int(input("국어점수 :  "))
    math = int(input("수학점수 : "))
    eng = int(input("영어점수 : "))

def print_student():
    print("이름 : ", name, "국어 : ", kor, "수학 : ", math, "영어 : ", eng, "합 : ", sum, "평균 : ",avg)

def compute_score():
    global avg
    global sum

    sum = kor + eng + math
    avg = sum / 3

for i in range(3):
    read_student()
    compute_score()
    print_student()
