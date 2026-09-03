# 연산자

# 산술연산자

a = 10
b = 3

print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈
print(a % b)  # 나머지

# 복합 대임 연산자
a = 0
a += 4
print(a)

a -= 2
print(a)

# 증감 연산자 없음

# b = a++
a += 1

# 비교 연산자

print(a == b)  # 같음
print(a != b)  # 같지 않음
print("apple" > "apble")

print(1 < 2 < 3)  # 연속 비교 가능
print(1 < 3 < 2)  # 연속 비교 가능

print(not b)

# short circuit 테스트

if a > 0 or b / 0 > 0:  # 앞의 조건이 True이면 뒤의 조건은 실행되지 않음
    print("True")
