contacts = {} # 변수 초기화

while True:
    name = input("(입력모드)이름을 입력하시오 : ")
    if not name:
        break;
    tel = input("전화번호를 입력하시오 : ")
    contacts[name] = tel # 이름이라는 키 값에 전화번호 저장

while True:
    name = input("(검색모드)이름을 입력하시오 : ")
    if not name:
        break;
    if name in contacts:
        print(name, "의 전화번호는", contacts[name], "입니다") #이름 검색 후 결과 도출
    else:
        print("없는 이름입니다")
