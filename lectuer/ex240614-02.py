# 변수란 값을 저장하는 공간이다.

a = 1
b = "Python"
c = [1, 2, 3]
d = (1, 2, 3)
e = { 
    'firstName' : "Joun",
    'lastName' : "Doe",
    'age' : 17
}
f = set([1, 2, 3])
g = True

# 변수 = 값 -> 변수에 값을 할당한다.

# 변수는 프로그램이 실행될 때, 메모리에 생성되고,
# 프로그램이 종료되면, 메모리에서 삭제 된다.

a = [1, 2, 3]
print(id(a))


a = 10
b = a
print(id(a), id(b))

a = [1, 2, 3, 4]
# b = a
# a[0] = 5
# print(a , b)
# print(id(a), id(b))

# 복합 data를 복사하는 방법

# 1.
b = a[:] # 리스트 a를 새로 복사하여 b에 할당. (a, b가 완전히 다른 변수가 된다.)
a[0] = 5
print(a , b)
print(id(a), id(b)) 

# 2. copy라는 모듈을 사요한다.

from copy import copy
a = [1, 2, 3]
b = copy(a)
a[0] = 5
print(a , b)
print(id(a), id(b)) 

# 3. 메서드를 사용하는 방법
a = [1, 2, 3]
b = a.copy()
a[0] = 5
print(a , b)
print(id(a), id(b)) 

# 여러개의 변수를 한번에 할당하는 방법 : 언팩킹

a,b=('Python', 'Life') # 튜플 : a,b = 'Python', 'life'
print(a)
print(b)

a,b=['Python', 'Life'] # 리스트
print(a)
print(b)

a = 3
b = 5

a, b = b,a
print(a,b)

