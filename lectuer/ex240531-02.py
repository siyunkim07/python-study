# 문자열 포매팅

# % 포매팅

# 정수 삽입
str = "I eat %d apples." % 3
print(str)

# 문자열 삽입
str = "I eat %s apples." % "five"
print(str)

# 정수와 문자열을 여러개 동시에 삽입, 변수도 사용 가능

number = 10
day = "three"

str = "I eat %d apples. So I was sick for %s days" % (number, day)
print(str)

# %s에는 어떠한 Type의 data를 사용헤도 된다.

print('I have %s apples' % 3)
print("rate is %s" % 3.234 )
# 실수를 삽입할 때 : %f
print("rate is %f" % 3.234 )
print("rate is %.3f" % 3.234 )
print("rate is %0.3f" % 3.234 )
print("rate is %10.3f" % 3.234 )

# % 포매팅에서 문자열안에 %를 출력하고 싶을 때

print("Error is %d%%" % 89)

# 문자열을 정렬

print("%10s" % "hi") # 오른쪽 정렬
print("%-10s" % "hi") # 왼쪽 정렬

# 소수점 표시하기

print("%0.4f" % 3.4213123)
print("%10.4f" % 3.4213123)