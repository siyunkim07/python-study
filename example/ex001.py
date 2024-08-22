# 1.
a = 'Hello World'
print(a)

# 2.
a = "Mary's cosmetics"
print(a)

# 3.
a = '신씨가 소리질렀다. "도둑이야."'
print(a)

# 4.
a = "c:Windows"
print(a)

# 5.
print("오늘은" , "일요일") # print() 함수 내에서 ','의 역할은 공백을 채운다.
# ,는 sep""로 조정이 가능하다. 
print("오늘은" , "일요일", sep = " ") #기본값
print("오늘은" , "일요일", sep = ";") 

# 7.
print("naver", "kakao", "samsung", sep = ";")

# 8.
print("naver", "kakao", "samsung", sep = "/")

# print()문에서, end = ""를 사용해서 줄바꿈을 변경할 수 있다.
print("오늘은", end = '')
print("일요일", end = "\n")

# 9.
print("first", end = " ")
print("second", end = " ")
print()

#  10.
a = 5
b = 3
print( a / b)

# 11.
coffee = 5000
print( coffee * 5)

# 변수나 값의 data type을 알아보는 함수 type() 함수
a = 1
b = 3.14
c = "Python"
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 12.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13.
s = "hello"
t = "python"
print(s + "! " +t)

# 14.
print( (2 + 3) * 3)

# 15.
a = "132"
print(type(a))

# 형변환 (Data type) 변환

# 문자열 -> 정수 : int()
a = "124"
a = int(a)
print(a, type(a))

# 문자열 -> 실수 : flaot()
b = "3.14"
b = float(b)
print(b, type(b))

# 정수, 실수 -> 문자열 : str()
a = 123
a = str(a)
print(a, type(a))

# 16.
num_str = "720"
num_str = int(num_str)
print(num_str, type(num_str))

# 17.
num = 100
num = str(num)
print(num, type(num))

# 18.
a = "15.79"
a = float(a)
print(a, type(a))

# 19.
year = "2024"
year = int(year)
print(year)
print(year - 1)
print(year - 2)

# 20.
price =  48584
print( price * 36)

# 21.
letters = "Python"
print(letters[0], letters[2])

# 22.
license_plate = "24가 2210"
print(license_plate[-4:])

# 문자열 슬라이싱
# 문자열[시작인덱스 : 끝인덱스: step]
# 시작인덱스 생략 : 처음부터
# 끝 인덱스 생략 : 끝까지
# step = step의 값 만큼 건너 뛴다.
# step을 -1을 주면, 문자열의 순서를 바꾼다.
a = "abcdefgh"
print(a[::2])

print(a[::-1])

# 23.
string = "홀짝홀짝홀짝"
print(string[1::2])

# 24.
string = "Python"
print(string[::-1])

# 25.
phone_number = "010-1111-2222"
result = phone_number.replace("-" , " ") 
print(result)

# 26.
phone_number = "010-1111-2222"
result = phone_number.replace("-" , "") 
print(result)

# 27.
url = "http://sharebook.kr"
result = url.split(".")
print(result[1])

# 28.
# error가 발생함.

# 29.
string = 'abcdfe2a354a32a'
result = string.replace("a" , "A")
print(result)


# 30. 
# 문자열의 매서드나 함수는 원래의 문자열을 절대 바꾸지 않는다.
# 즉, 항상 새로운 문자열의 결과를 반환한다.
#result를 안찍었음으로 그대로 abcd나옴.

# 33.
print( "-" * 80)

# 34.
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " " ) * 4 )

# 35.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2))

# 36.
print("이름 : {0} 나이 : {1}".format(name1, age1))
print("이름 : {0} 나이 : {1}".format(name2, age2))

# 37.
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 38.
number = "5,969,782,550"
result = number.replace("," , "")
print(int(result))

# 39.
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40.
data = "  삼성전자  "
print(data.strip())

# 41.
ticker = 'btc_krw'
print(ticker.upper())

# 42.
ticker = "BTC_KRW"
print(ticker.lower())

# 43.
a = 'hello'
print(a.capitalize())

# 44.
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

# 45.
file_name = "보고서.xlsx"
print(file_name.endswith(('xlsx','xls')))

# 46.
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#47
a = "hello world"
result = a.split(" ")
print(result)

#48
ticker = 'btc_krw'
result = ticker.split("_")
print(result)

# 49
date = "2020-05-01"
result = date.split("-")
print(result)

# 50
data = "039290    "
result = data.rstrip()
print(result)


