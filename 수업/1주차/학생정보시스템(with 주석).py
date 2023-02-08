import sys #C언어의 #include<sys>

#C언어와 파이썬의 차이점
# 1. 변수는 숫자나 특수문자로 시작 안 됨
# 2. 변수를 선언하지 않음

#변수 선언이유 : 메모리를 할당받기 위해서★★★
#메모리는 데이터를 저장할 공간을 할당밥기 위해서★★★


total_student = 0
kor_sum = 0.0
eng_sum = 0.0
math_sum = 0.0
while True: # 반복문(while & for)
# 조건이 0이 아니면 참, 0이면 거짓
# 괄호의 유무 차이
# ':' 조건문의 끝을 알리는 콜론!!!
# 중괄호 없는 대신 들여쓰기(반복문의 block을 의미)★★★★★
# 들여쓰기가 끝나면 block의 끝을 의미

    hakbun = int(input("학번 : ")) # 키보드 입력은 다 글자이다!! ☞ 숫자처럼 쓰고 싶다면 전환
    if hakbun == -1:
        break
    name = input("이름을 입력하시오 : ") # input = printf(); + scanf(); # 키보드 입력 → input ☞ 학번을 출력 후 입력을 기다림 #cf) atoi(); : ASCII to Integer
    kor = int(input("국어점수 : "))
    if kor < 0 or kor > 100: # if 조건문
        print("국어점수 오류 : ", kor)
        sys.exit() #'.'으로 함수를 엑세스한다
    math = int(input("수학점수 : "))
    if math < 0 or math > 100: # 조건문은 항상 ': 으로 끝남. 이후 들여쓰기
        print("수학점수 오류 : ", math)
        sys.exit()
    eng = int(input("영어점수 : "))
    if eng < 0 or eng > 100:
        print("영어점수 오류 : ", eng)
        sys.exit()

    if kor >= 90 and kor <= 100: # 관계 연산자(<, <=, >, =>, ==), 논리 연산자(and, or)
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
    print("평균 : %.2f" %avg) # %는 제어글자 #'%.2f : 소수점 두자리까지 출력하라(실수형으로) # %로 츨력문과 변수명을 구분한다
    print("+------------------------------------+")
# while 끝

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
