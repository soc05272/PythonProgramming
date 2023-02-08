#-*- coding: utf-8 -*-

# 파일명 : dict-list-6.windows_finalexam.py
# 학생 정보를 파일에 저장하고, 그 파일에서 학생정보를 읽어서 처리
# 작성자 : 최선완(sunchoi@anyang.ac.kr)
# 배포시 출처를 밝혀야 함

import sys

students = dict()
kor_sum = 0.0
math_sum = 0.0
kor_avg = 0.0
math_avg = 0.0
class_avg = 0.0
count = 0

def read_student():
    
    global count

    outfile = open("exam.txt","w") # 기존파일 덮어쓰기
    while True:
        std_nbr = input("학번 : ")
        if std_nbr == "-1":
            if count == 0:
                print("학생 수가 0명 입니다")
                continue
            else:
                break
        name = input("이름을 입력하시오 : ")
        sex = input("성별을 입력하시오(m/f) : ")
        kor = int(input("국어점수 : "))
        if kor > 100 or kor < 0 :
            print("국어 점수 오류 :",kor)
            sys.exit()

        math = int(input("수학점수 : "))
        if math > 100 or math < 0 :
            print("수학 점수 오류 :",math)
            sys.exit()

        #outfile = open("exam.txt","w") # 기존파일 덮어쓰기
        outfile.write(std_nbr)
        outfile.write(" ")
        outfile.write(name)
        outfile.write(" ")
        outfile.write(sex)
        outfile.write(" ")
        outfile.write(str(kor))
        outfile.write(" ")
        outfile.write(str(math))
        outfile.write(" ")
        outfile.write("\r\n") # 한 줄 띄

        count += 1

    outfile.close()                   

def fread_student():
    
    global students, count

    filep = open("exam.txt","r")
    #wcount = 0
    for line in filep:
        line = line.rstrip()
        print(line)
        field = line.split() # ['0001','choi', 'm', '77', '', 0.0 '88', '', 0.0, '99', '', 0.0]
        print(field)

        
        wcount = 0
        for word in field:
            if wcount == 0:
                std_nbr = word
            elif wcount == 1:
                name = word
            elif wcount == 2:
                sex = word
            elif wcount == 3:
                kor = int(word)
            else:
                math = int(word)

            wcount += 1

        students[std_nbr] = {"name":name,"sex":sex,
                             "kor":kor,"ckor":'',"fkor":0.0,
                             "math":math,"cmath":'',"fmath":0.0,
                             "avg":0.0}
        count += 1
        wcount = 0


def print_student():

    for keyval in sorted(students.keys()):
        print("학번 : %s 이름 : %s  %c" %(keyval,students[keyval]["name"],students[keyval]["sex"]))
        print("국어 : %d  %.1f  %c" %(students[keyval]["kor"],students[keyval]["fkor"],students[keyval]["ckor"]))
        print("수학 : %s  %.1f  %c" %(students[keyval]["math"],students[keyval]["fmath"],students[keyval]["cmath"]))
        print("평균 학점 : %.2f\n"%(students[keyval]["avg"]))
        
    print("학급 국어 평균 : %.2f 학급 수학 평균 : %.2f"
              %(kor_avg,math_avg))
    print("학급 전체 평균 : %.2f" %(class_avg))



def compute_score():
    global kor_sum, math_sum
    global kor_avg, math_avg, class_avg
    
    for keyval in sorted(students.keys()):
        k_score,kc_score = trans_score(students[keyval]["kor"])
        m_score, mc_score = trans_score(students[keyval]["math"])
        students[keyval]["fkor"] = k_score
        students[keyval]["fmath"] = m_score

        students[keyval]["ckor"] = kc_score
        students[keyval]["cmath"] = mc_score
        
        avg = (students[keyval]["fkor"] + students[keyval]["fmath"])/2
        students[keyval]["avg"] = avg
        
        kor_sum = kor_sum + students[keyval]["fkor"]
        math_sum = math_sum + students[keyval]["fmath"]
        print("kor_sum:",kor_sum, " ",
              "math_sum:",math_sum)

    kor_avg = kor_sum/float(count)
    math_avg = math_sum/float(count)
    class_avg = (kor_avg + math_avg)/2
    
def trans_score(score):
    if  score >= 90 and score <=100:
        return 4.0, 'A'
    elif score >=80 and score <=89:
        return 3.0, 'B'
    elif score >=70 and score <= 79:
        return 2.0, 'C'
    elif score >=60 and score <=69:
        return 1.0, 'D'
    else:
        return 0.0, 'F'
        
read_student()
fread_student()
compute_score()
print_student()


            
