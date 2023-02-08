num = []
sum = 0

for i in range(5):
    k = int(input("숫자를 입력하시오 : "))
    num.append(k)

for i in num:
    sum = sum +i

average = sum / 5
print("sum = ", sum)
print("average = ", average)
