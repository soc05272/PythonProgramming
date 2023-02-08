import random # 랜덤함수

quotes = [] # 변수 초기화
quotes.append("꿈을~~")   # ".append"를 활용하여 속담 추가
quotes.append("분노는~~")
quotes.append("고생없이~~")
quotes.append("사람은~~")
quotes.append("시작이~~")

for i in range(5):
    dailyQ = random.choice(quotes)
    print(dailyQ)
