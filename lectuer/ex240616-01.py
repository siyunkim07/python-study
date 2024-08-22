# if 문 : 조건문 

# 돈이 5000원 이상 : 택시 , 아니면 : 버스

# money = 6000

# if money > 5000 : 
#     print("택시를 타고 가라")
# else : 
#     print("버스를 타고 가라")

age = 14

if age >= 18 : 
    print("투표가 가능합니다.")
else : 
    print("투표가 불가능합니다.")


# 조건문 : 연산의 결과가 True, 혹은 False로 나타나는 문장
money = 6000
if money >  5000  :
    pass
else :
    pass

# 조건문의 연산자 : 비교 연산자 (True or False)

x = 3
y = 2 

print(x > y) # True 
print(x < y) # False 
print(x != y) # True 
print(x == y) # False
print(x <= y) # False
print(x >= y) # True

# 조건문의 연산자 : 논리 연산자 (and, or, not)
# 여러개의 조건문을 실행한 결과를 True, False로 반환

# 1.x and y 
# x와 y가 모두 True일때 : True 
# 그렇지 않으면 , 무조건 False

# 2. x or y
# x나 y중 하나라도 True이면 : True 
# 그렇지 않으면 : False

# 3. not x, not y
# x,y가 True이면 False이고, 
# x,y가 False이면 True이다.

price = 9.99
print(price > 0 and price < 10)
print(price > 10 and price < 20)
print(price > 10 or price < 20)
print(price > 10 or price < 5)
print(not price > 10)
print(not (price > 10 and price < 10))

# 논리 연산자의 우선순위

# not, and, or 연산자 순서이다.
# 왼쪽에서 오른쪽으로 연산을 수행한다.

money = 2000
card = True
if money >= 5000 or card:
    print('택시를 타고 가라')
else:
    print('버스를 타고 가라')

# in, not in 은 주로 리스트, 튜플, 문자열과 함께 사용된다.
# in : ~에 있다
# not in : ~에 없다.

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print(1 not in (1, 2, 3))
print('y' in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# if 문을 작성하는데, 아직 Logic이 완전하지 않다.
# 그렇지만, 큰 틀을 만들어 놓고 코딩을 하고자 한다.

# pass 문을 사용한다.
# pass 문은 아무것도 하지 않는 문장.

#  if(조건문): 
#     pass
#  elif(조건문):
#     pass
#  else
#     pass

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

pocket = ['paper', 'cellphone']
card = True

if 'money'in pocket:
    print('택시를 타고가라')
else:
    if card:
        print('택시를 타고가라')
    else:
        print('걸어가라')


if 'money' in pocket:
    print('택시를 타고가라')
elif card:
    print('택시를 타고가라')
else:
    print('걸어가라')


#
score = 65 
# if score >= 60:
#     message = 'sucess'
# else :
#     message = 'failure'

message = 'success' if score >= 60 else 'failure'
print(message)