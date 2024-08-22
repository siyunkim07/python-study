# 문자열의 인덱싱

a = "Life is too short, You need Python"

print(a[0])
print(a[17])
print(a[28])

# 인덱스 No.를 음수로 주면, 문자열의 뒤부터 count한다.
# 문자열의 맨 끝 글자는 -1이다.

print(a[-1])
print(a[-6]) # a[28]와 같음.

# 문자열의 슬라이싱 : 문자열에서 문자열의 일부를 잘라낸다.
# 문자열[시작인덱스:끝인덱스]

print(a[0:4]) # 끝 인덱스는 포함하지 않는다. -1 위치까지 잘라낸다.

print(a[8:11])

# 슬라이싱을 할 때, 시작 인덱스를 생략하면 : 처음부터 
# 슬라이싱을 할 때, 끝 인덱스를 생략하면 : 끝까지

print(a[:26])
print(a[28:])
print(a[:])

print(a[-6:])

print(a[-8:-6]) #음수를 사용할 경우 앞의 수가 더 작아야 오류X

# 예제 

a = "20230331Rainy"
date = a[:8]
print(date)
weather = a[8:]
print(weather)

year = a[:4]
print(year)
month = a[4:6]
print(month)
day = a[6:8]
print(day)

