import sys

total_student = 0
kor_sum = 0.0
eng_sum = 0.0
math_sum = 0.0
while True:

    hakbun = int(input("학번 : "))
    if hakbun == -1:
        break
    name = input("이름을 입력하시오 : ")
    kor = int(input("국어점수 : "))
    if kor < 0 or kor > 100:
        print("국어점수 오류 : ", kor)
        sys.exit()
    math = int(input("수학점수 : "))
    if math < 0 or math > 100:
        print("수학점수 오류 : ", math)
        sys.exit()
    eng = int(input("영어점수 : "))
    if eng < 0 or eng > 100:
        print("영어점수 오류 : ", eng)
        sys.exit()

    if kor >= 90 and kor <= 100:
        kore = 4.0
        korc = 'A'
    elif kor >= 80 and kor <= 89:
        kore = 3.0
        korc = 'B'
    elif kor >= 70 and kor <= 79:
        kore = 2.0
        korc = 'C'
    elif kor >= 60 and kor <= 79:
        kore = 1.0
        korc = 'D'
    else:
        kore = 0.0
        korc = 'F'

    kor_sum = kor_sum + kore

    if math >= 90 and math <= 100:
        mathe = 4.0
        mathc = 'A'
    elif math >= 80 and math <= 89:
        mathe = 3.0
        mathc = 'B'
    elif math >= 70 and math <= 79:
        mathe = 2.0
        mathc = 'C'
    elif math >= 60 and math <= 79:
        mathe = 1.0
        mathc = 'D'
    else:
        mathe = 0.0
        mathc = 'F'

    math_sum = math_sum + mathe

    if eng >= 90 and eng <= 100:
        enge = 4.0
        engc = 'A'
    elif eng >= 80 and eng <= 89:
        enge = 3.0
        engc = 'B'
    elif eng >= 70 and eng <= 79:
        enge = 2.0
        engc = 'C'
    elif eng >= 60 and eng <= 79:
        enge = 1.0
        engc = 'D'
    else:
        enge = 0.0
        engc = 'F'

    eng_sum = eng_sum + enge

    avg = (kore + mathe + enge) / 3

    total_student += 1
    print("+------------------------------------+")
    print("이름 : ", name, "학번 : ", hakbun)
    print("국어 : ", kor, kore, korc,
          "수학 : ", math, mathe, mathc,
          "영어 : ", eng, enge, engc)
    print("평균 : %.2f" %avg)
    print("+------------------------------------+")

if total_student == 0:
    print("학생 수는 0명입니다")
    sys.exit()
else:
    kor_avg = kor_sum / total_student
    math_avg = math_sum / total_student
    eng_avg = eng_sum / total_student
    class_avg = (kor_avg + math_avg + eng_avg) / 3

    print("+------------------------------------+")
    print("학급 학생 수 : ", total_student)
    print("학급 평균 : %.2f" % class_avg)
    print("국어평균 : %.2f  수학평균 : %.2f  영어평균 : %.2f" % (kor_avg + math_avg + eng_avg))
