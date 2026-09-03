# for문

# for x in iterable객체:
#   ...

for i in range(5):  # 0 ~ 4
    print(i, end=" ")

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

#  5 4 3 2 1 거꾸로
for i in range(5, 0, -1):
    print(i, end=" ")
print()


# 1 ~ 10까지의 합
total = 0
for i in range(1, 11):
    total += i
print("1 ~ 10까지의 합:", total)

print("1 ~ 10까지의 합:", sum(range(1, 11)))  # 1 ~ 10까지의 합

s = "hi안녕安寧"

for c in s:
    print(c, end=" ")

print(len(s))  # 문자열 길이

# 구구단 출력
# 2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 ... 2 * 9 = 18
# 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 ... 3 * 9 = 27
# ..

for j in range(2, 10):
    for i in range(1, 10):
        print(f"{j} * {i} = {j*i}", end="|")
    print()
