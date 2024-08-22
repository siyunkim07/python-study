 # 부울 (Bool,Boolean) 자료형

# 부울 자료형은 True, False 값만 존재한다.

a = True  # 변수값에 할당
b = False

print(a, type(a))
print(b, type(b))

print(1 == 1) # 조건문
print(3 > 2)
print(3 < 2)

# 자료값에 의해 True, False를 가리는 경우
# 어떤 변수나 값이, 값을 가지고 있으면 : True 
#                  값이 없으면 : False


# 자료형의 활용

a = [1, 2, 3, 4]
while a:
    print(a.pop())


if [1, 2, 3] : 
    print("참")
else:
    print("거짓")


# bool 연산 : bool() 함수

print(bool("Python"))
print(bool(""))
print(bool(6))
print(bool())


