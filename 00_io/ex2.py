# 변수
a = 2
b = 3
print(a, end="  ")
print(b)
print(a, b, sep=", ")
a = 2
b = 3

print(a, b)  # 튜플 언패킹
a, b = 2, 3
print(a, b)

a = b = c = 0

a, b = b, a

# 변수명 규칙 (C 와 동일)
# 알파벳, 숫자, 언더스코어(_)로 만 사용가능
# 변수명은 숫자로 시작할 수 없음
# 대소문자 구분함
# 예약어 사용 불가
# snake_case
# camelCase
_name = "pororo"
