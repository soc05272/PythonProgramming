#chapter 7장 - 함수
# 08 - 변수의 범위 global 수정

global result

def calculate_area():
    global result

    result = 3.14 + radius**2
    

radius = float(input("원의 반지름 : "))
area = calculate_area()
print(result)
