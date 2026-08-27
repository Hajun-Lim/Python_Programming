# 문자열
# "", ''
a = "python"
print(a, type(a))
# I'll be back
print("I'll be back")
print("I'll be back")

multiline = """
Life is too short
You need python
"""
print(multiline)


def func():
    """이 함수는 아무것도 하지 않습니다."""
    pass


print(func.__doc__)

# 문자열 연결
print("python" + " is fun")

# 문자열 반복

print("hello" * 10)
print("*" * 50)

# 문자열끼리만 + 가능
# print("python" + "3.8")
print("hello" + str(10))

print("10" + "2")
print(int("10") + int("2"))

# 문자열 포맷팅 (f-string)
name = "pororo"
age = 23
print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")  # 대문자
pi = 3.141592
print(f"{pi:.3f}")  # 소수점 3자리까지
print(f"{pi:.0f}")  # 소수점 0자리까지


num = 123456789
print(f"{num:,}")  # 천 단위 구분자
print(f"{num:15d}")
print(f"{num:15d}")
print(f"{num:15,d}")
