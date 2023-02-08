#chapter 7장 - 함수
# 08 - 변수의 범위

def calculate_area(radius):
    result = 3.14 + radius**2
    return result

r = float(input("원의 반지름 : "))
area = calculate_area(r)
print(area)
