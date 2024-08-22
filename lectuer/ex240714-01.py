# print 문 사용

# print("Life" "is" "too" "short")
# print("Life" + "is" + "too" + "short")
# print("Life", "is", "too", "short", sep = ' ')
# print("Life", "is", "too", "short", sep = '')
# print("Life", "is", "too", "short", sep = '*')

# print("first", end = '')
# print("second")
# print("third")
# print("fourth", end = ' ')
# print("fifth")


# 파일 읽고 쓰기

# 파일 생성

# 파일을 생성한다.

# f = open("newfile.txt", 'w', encoding = 'ut68')
# # 파일을 닫는다...
# f.close()

# 파일열기모드 종류

# 'w' : 쓰기 모드 - 파일을 새로 생성하고, 쓰기를 할때
#       만약 같은 이름의 파일이 이미존재할 때에는 기존의 내용을 삭제하고, 쓰기가 실행된다.


# 'r' : 읽기 모드 - 이미 존재하는 파일을 읽기만 한다.

# 'a' : 추가 모드 - 이미 존재하는 파일의 맨 마지막에 새로운 내용을 추가한다.

# 파일 쓰기 예 

# f = open("newfile.txt", 'w', encoding='utf8') # encoding='utf8'은 한글을 표현
# for i in range(1,11):
#     data = f"{i}번째 출입니다.\n"
#     f.write(data)


# f.close()

# 파일 읽기 예

# 파일 내용을 할줄씩 읽을 때
# f = open("newfile.txt", 'r', encoding='utf8')
# line = f.readline()
# print(line)
# f.close()

# f = open('newfile.txt', 'r', encoding = 'utf8')
# while True:
#     line = f.readline()
#     if not line :
#         break
#     print(line, end='')

# f.close()

# f =  open('newfile.txt', 'r', encoding='utf8')
# lines = f.readlines() # 한반에 file 내용을 모두 읽기
# for line in lines : 
#     print(line, end = '')
# f.close()

# 파일을 읽을 떄 줄바꿈 문자를 제거하고자 할때

# f = open('newfile.txt', 'r', encoding ='ut68')
# lines = f.readlines() 
# for line in lines :
#     print(line.strip())

# f.close()

# read 함수를 이용하여 파일 읽기
# f = open('newfile.txt','r', encoding='ut68')
# data = f.read()
# print(data)
# f.close()

# 파일 객체를 이용하여 읽는 방법

# f = open("newfile.txt",'r', encoding='utf8')
# for line in  f:
#     print(line)
# f.close


# f = open("newfile.txt", 'a', encoding='utf8')
# for i in range(11,21):
#     data = f"{i}번째 출입니다\n"
#     f.write(data)
# f.close()

#ith문과 함께 사용하기
# open후에 close() 할 필요가 없다.

with open("foo.txt", 'w', encoding='utf8') as f:
    f.write("Life is too short, you need Python")









