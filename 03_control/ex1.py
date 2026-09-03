# 조건문 : if문, match문(3.10이상)

age = 17

if age >= 18:
    print("성년")
else:
    print("미성년")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

# match문
grade = "A"

match grade:
    case "A":
        print("우수")
    case "B":
        print("양호")
    case "C":
        print("보통")
    case _:  # default에 해당
        print("알 수 없음")


year, month, day = input().split(" ")

print(f"오늘은 {year}년, {month}월, {day}일 입니다.")

blood, age, height, weight = input().split("")

print(f"혈액형: {blood}형 \n 나이: {age}살\n 키: {height}cm\n 몸무게: {weight}kg")
