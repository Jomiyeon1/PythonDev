# 사용자로부터 주민번호를 입력받아 출생년도와 나이, 성별을 출력해주는 프로그램을 작성하시오.
# pin = "8811201068234"

# 입력받은 주민번호
pin = input("주민등록번호를 포함해 입력해주세요.")
#주민번호 앞자리 추출
yymmdd= pin[:5 + 1]
#성별
gender = pin[5 + 1]
#출생년도
year=""
#나이
age = 0

year = '19' + yymmdd[:1+1]
if gender in "12":
    year = '19' + yymmdd[:1+1]
elif gender in "34":
    year = '19' + yymmdd[:1+1]

age = 2022 - int(year) + 1

print("당신의 출생년도는 {}년 ".format(year))
print("당신의 나이는{}세".format(age))

if int(gender) % 2 == 0:
    print("여성입니다.")
else :
    print("남성입니다.")