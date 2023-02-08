#-*- coding: utf-8 -*-

#student_dict_list-4.py : 파일로 부터 학생 정보를 읽음
#작성자 : 최선완(sunchoi@anyang.ac.kr)
# 배포시 출처를 밝혀야 함

import sys

students = dict()
k = []
kor_sum = 0.0
eng_sum = 0.0
math_sum = 0.0
kor_avg = 0.0
eng_avg = 0.0
math_avg = 0.0
class_avg = 0.0
count = 0

def read_student():
    
    global students, count

    filep = open("C:\\2020_0210\datafile.txt","r") # 읽기모드
    for line in filep: # filep : 파일 디스크립터 # 파일의 한 줄 읽기 # line : 한 줄(파일을 한 즐로 다루는 객체)
        line = line.rstrip() # "\n" 제거
        field = line.split() # 스페이스를 기준으로 단어별로 자름 # 리스트 형태로 저장 # field [0001, BTS, m, 77, 88, 99]
        std_nbr = int(field[0]) # 지역변수, field[0] 인덱스에 문자열로 저장 → 정수형으로 변환
        if std_nbr == -1: # 프로그램 종료
            if count == 0:
                print("학생 수가 0명 입니다")
                continue # 반목문으로 다시 돌아감
            else:
                break # 반복문 for 나가기

        name = field[1] # 이름 저장
        sex = field[2] # 성별 저장
        kor = int(field[3]) # 국어점수 저장(정수형 변환)
        if kor > 100 or kor < 0 :
#            print("국어 점수 오류 :",end=' ')
            print("국어 점수 오류 : %d" %kor)
            sys.exit() # 프로그램 종료
        eng = int(field[4]) # 영어점수 저장(정수형 변환)
        if eng > 100 or eng < 0 :
            print("영어 점수 오류 : %d" %eng)
            sys.exit() # 프로그램 종료
        math = int(field[5]) # 영어점수 저장(정수형 변환)
        if math > 100 or math < 0 :
            print("수학 점수 오류 : %d" %math)
            sys.exit() # 프로그램 종료
            
        k.append(std_nbr) # 키값인 학번을 리스트에 저장(append)
    
        students[std_nbr] = [name,kor,0.0,'',eng,0.0,'', math,0.0,'', 0.0]
        count += 1
        
def print_student():

    for list in k: # k : key값이 저장. 
        print("학번 : %d 이름 : %s " %(list,students[list][0])) # 리스트(key값) 출력, 이름 출력
        print("국어 : %d  %.1f  %c" %(students[list][1],students[list][2],students[list][3]))
        print("영어 : %s  %.1f  %c" %(students[list][4],students[list][5],students[list][6]))
        print("수학 : %s  %.1f  %c" %(students[list][7],students[list][8],students[list][9]))
        print("평균 학점 : %.2f\n"%(students[list][10]))
        
    print("학급 국어 평균 : %.2f 학급 영어 평균 : %.2f 학급 수학 평균 : %.2f"
              %(kor_avg,eng_avg,math_avg))
    print("학급 전체 평균 : %.2f" %(class_avg))



def compute_score():
    global kor_sum, eng_sum, math_sum
    global kor_avg, math_avg, eng_avg, class_avg
    
    for list in k:
        k_score,kc_score = trans_score(students[list][1])
        e_score, ec_score = trans_score(students[list][4])
        m_score, mc_score = trans_score(students[list][7])
        students[list][2] = k_score
        students[list][5] = e_score
        students[list][8] = m_score

        students[list][3] = kc_score
        students[list][6] = ec_score
        students[list][9] = mc_score
        
        avg = (students[list][2] + students[list][5] + students[list][8])/3
        students[list][10] = avg
        
        kor_sum = kor_sum + students[list][2]
        eng_sum = kor_sum + students[list][5]
        math_sum = kor_sum + students[list][8]

    kor_avg = kor_sum/count
    eng_avg = eng_sum/count
    math_avg = math_sum/count
    class_avg = (kor_avg + eng_avg + math_avg)/3
    
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
compute_score()
print_student()


            
