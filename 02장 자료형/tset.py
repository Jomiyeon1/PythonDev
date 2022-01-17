#print("python Programing")
#print("python Programing_test2")
name = input("이름을 입력하세요.: ")
# print("입력하신 이름은", name, "입니다.")
kor = input("국어점수를 입력하세요.:")
eng = input("영어점수를 입력하세요.:")
math = input("수학점수를 입력하세요.:")

total = int(kor) + int(eng) + int(math)
# input은 str타입이기 때문에 int로 형변환 시켜준다.
avg = total/3
print(name,"님의 총점은 ", total, "입니다.")
print(name,"님의 평균은 ", avg, "입니다.")
# print(type(name)) :: str타입.