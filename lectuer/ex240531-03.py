# format 함수를 사용한 포매팅

print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))


number = 3 
str = "five"
statement = "I eat {0} apples. So I was sick for {1} days" .format(number, str)
print(statement)

# 이름으로 넣기
statement = "I eat {number} apples. So I was sick for {str} days" .format(number = 10, str = "five")
print(statement)

# format 정렬

print("{0:<10}".format("hi"))  # 왼쪽 정렬
print("{0:>10}".format("hi"))  # 오른쪽 정렬
print("{0:^10}".format("hi"))  # 가운데 정렬

# 공백 채우기

print("{0:=<10}".format("hi"))  # 왼쪽 정렬
print("{0:=>10}".format("hi"))  # 오른쪽 정렬
print("{0:=^10}".format("hi"))  # 가운데 정렬

# 소수점 표현하기

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{0:>10.4f}".format(y))
print("{0:<10.4f}".format(y))
print("{0:^10.4f}".format(y))
print("{0:*^10.4f}".format(y))


# {} 표현하기

print("{{ }}".format())
