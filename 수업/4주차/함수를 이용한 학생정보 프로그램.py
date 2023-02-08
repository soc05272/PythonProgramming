import sys

global hak,name
global kor, math
global clkoravg, clmathavg, clavg
global mysum

def read_student():
    global hak, name
    global kor, math

    hak = int(input("학번을 입력하시오 : "))
    if hak == -1:
        return(-1)

    name = input("이름을 입력하시오 : ")

    kor = int(input("국어점수 : "))
    result = iscorrect_score(kor)
    if result == -1:
        print("올바르지 않은 국어점수!!", kor)
        return -2

    math = int(input("수학점수 : "))
    result = iscorrect_score(math)
    if result == -1:
        print("올바르지 않은 수학점수!!", math)
        return -2

    return 0

def print_student():
    print("-"*60)
    print("학번 : ", hak, "이름 : ",name,
          "국어 : ", kor,ckor,ekor,
          "수학 : ", math, cmath, emath)
    print("평균 : %.2f" %myavg)

def print_class():

    global clkoravg, clmathavg, myavg, clavg

    clkoravg = clkorsum/no_of_student
    clmathavg = clmathsum/no_of_student
    clavg = (clkoravg + clmathavg) / 2

    print("-"*60)
    print("학급 전체 평균 : %.2f" %clavg)
    print("국어 평균 : %.2f,  수학 평균 : %.2f"
          %(clkoravg, clmathavg))
    print("-"*60)

def iscorrect_score(score):
    if score < 0 or score > 100:
        return -1

def compute_score(score):
    if score >=90 and score <=100:
        return('A', 4.0)
    elif score >=80 and score <=89:
        return('B', 3.0)
    elif score >=70 and score <=79:
        return('C', 2.0)
    elif score >=60 and score <=69:
        return('D', 1.0)
    else:
        return('F', 0.0)

def s_init():
    global clkorsum, clmathsum
    global clkoravg, clmathavg
    global no_of_student

    no_of_student = 0
    clkorsum = clmathsum = 0.0
    clkoravg = clmathavg = 0.0

# 시작
s_init()

while True:
    result = read_student()
    no_of_std = 0
    if result == -1:
        if no_of_std == 0:
            print("0명의 학생입니다")
            continue
        else:
            break
    elif result == -2:
        print("점수 오류")
        sys.exit()

    ckor,ekor = compute_score(kor)
    cmath,emath = compute_score(math)

    clkorsum += ekor
    clmathsum += emath

    myavg = (ekor + emath) / 2

    no_of_std += 1

    print_student()

if no_of_std != 0:
    print_class()
