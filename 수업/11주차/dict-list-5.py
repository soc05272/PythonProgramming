# 파일에서 학생정보 읽기, 딕셔너리의 item을 키밗으로 이용하여 접근

import sys

students = dict()
kor_sum = 0.0
eng_sum = 0.0
math_sum = 0.0
math_sum  =0.0
kor_avg = 0.0
eng_avg = 0.0
math_avg = 0.0
class_avg = 0.0
count = 0

def read_student():

    global students, count

    filep = open("C:\\2020_0210\datafile.txt", "r")
    for line in filep:
        line = line.rstrip()
        field =line.split()
        std_nbr = int(field[0])

        if std_nbr == -1:
            if count == 0:
                print("학생 수가 0명입니다")
                continue
            else:
                break

        name = field[1]
        sex = feild[2]

        kor = int(field[3])
        if kor > 100 or kor < 0:
            print("국어점수 오류 : %d", kor)
            sys.exit()

        eng = int(field[4])
        if eng > 100 or eng < 0:
            print("어점수 오류 : %d", eng)
            sys.exit()

        math = int(field[5])
        if math > 100 or math < 0:
            print("수학점수 오류 : %d", math)
            sys.exit()

        students[std_nbr] = {"name":name, "sex":sex,
                             "kor":kor, "ckor":'', "fkor":0.0}
