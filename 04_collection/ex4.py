# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

print(t.count(1))  # 1이 몇개 있는지?

# 2의 첫번째 인덱스는?
print(t.index(2))

# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
a = list(t)
print(a)

# list -> tuple 변환
print(tuple(a))


# 튜플을 이용해서 swap하기
a, b = 10, 20
a, b = b, a
# 튜플 언패킹
t = (1, 2, 3, 4)


print(*t)
a, b, c, d = t
print(a, b, c, d)

a, *b, c = t
print(a, b, c)

t2 = (10, 20, 30, 40, 50)
print((*t, *t2))  # 튜플 합치기

# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
print(tuple(zip(subjects, scores)))


# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================
# generator 표현식
gen = (x for x in range(1, 11))
print(gen)  # <generator object <genexpr> at 0x000001F3D8C1A5E0>
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

for i in gen:
    print(i, end=" ")  # 4 5 6 7 8 9 10
print()

# 하나의 generator는 한 번 순회하면 끝이므로, 다시 순회하려면 새로 만들어야 함
# list comprehension vs generator 표현식
a = [x for x in range(1, 11)]  # list comprehension
b = (x for x in range(1, 11))  # generator 표현식
print(a, b)
print(sum(a), sum(b))

print(
    sum(b)
)  # generator는 한 번 순회하면 끝이므로, sum(b) 이후에는 b를 다시 순회할 수 없음

# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
result = (x**2 for x in range(1, 11))
print(result)


# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦


# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기
p1 = (1, 2, 3)
p2 = (10, 20, 30)
result = tuple(x + y for x, y in zip(p1, p2))
print(result)

# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일", "월", "화", "수", "목", "금", "토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
weekday = sum(hours[1:6])
print(f"{weekday}시간")
# ✅ 15시간


# 2️⃣ 가장 많이 공부한 시간 출력하기
max_hours = max(hours)
print(f"{max_hours}시간")
# ✅ 6시간


# 3️⃣ 가장 많이 공부한 요일 출력하기
max21 = hours.index(max_hours)
print(f"{days[max21]}요일")
# ✅ 토요일


# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)
print(f"max 점수: {max(scores)}점, min 점수: {min(scores)}점")

result = sorted(scores)
print(f"max 점수: {result[-1]}점, min 점수: {result[0]}점")


# ✅ max 점수: 92점, min 점수: 76점


# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", 1000, 5),
    ("바나나", 2000, 3),
    ("체리", 5000, 2),
)

# 총 재고 금액 출력
total = sum(price * qty for _, price, qty in stocks)
print(f"총액: {total}원")

stocks = (
    ("사과", "바나나", "체리"),
    (1000, 2000, 5000),
    (5, 3, 2),
)

total = sum(price * qty for _, price, qty in zip(*stocks))
print(f"{total}원")
