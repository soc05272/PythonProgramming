students = dict()
k = []
kor_sum = 0.0
math_sum = 0.0
kor_avg = 0.0
math_avg = 0.0
class_avg = 0.0
count = 0

def read_student():

    global students, count

    while True:
        std_nbr = input("학번 : ")
        if std_nbr == "-1":
            if count == 0:
                print("학생 수가 0명입니다!!")
                continue
            else:
                break

        name = input("이름을 입력하시오 : ")
        kor = int(input("국어 점수 : "))
        if kor > 100 or kor < 0:
            print("국어점수 오류 : ", kor)
            break
        math = int(input("수학 점수 : "))
        if math > 100 or math < 0:
            print("수학점수 오류 : ", math)
            break

        k.append(std_nbr)
        students[std_nbr] = [name, kor, 0.0, '', math, 0.0, '', 0.0]
        count += 1

def print_student():

    for list in k:
        print("이름 : ", students[list][0], "학번 : ", list)
        print("국어 : ", students[list][1], students[list][2], students[list][3])
        print("수학 : ", students[list][4], students[list][5], students[list][6])
        print("평균 학점 : %.2f\n" %(students[list][7]))

    print("학급 국어 평균 : %.2f  학급 수학 평균 : %.2f" %(kor_avg, math_avg))
    print("학급 전체 평균 : %.2f" %(class_avg))

def compute_score():
    global kor_sum, math_sum
    global kor_avg, math_avg, class_avg
    global count

    for list in k:
        k_score, kc_score = trans_score(students[list][1])
        m_score, mc_score = trans_score(students[list][4])
        students[list][2] = k_score
        students[list][5] = m_score

        students[list][3] = kc_score
        students[list][6] = mc_score

        avg = (students[list][2] + students[list][5]) / 2
        students[list][7] = avg

        kor_sum = kor_sum + students[list][2]
        math_sum = math_sum + students[list][5]

    kor_avg = kor_sum / count
    math_avg = math_sum / count
    class_avg = (kor_avg + math_avg) / 2

def trans_score(score):
    if score >= 90 and score <= 100:
        return 4.0, 'A'
    elif score >= 80 and score <= 89:
        return 3.0, 'B'
    elif score >= 70 and score <= 79:
        return 2.0, 'C'
    elif score >= 60 and score <= 69:
        return 1.0, 'D'
    else:
        return 0.0, 'F'


read_student()
compute_score()
print_student()
