# 딕셔너리의 특징 
# key, value로 쌍을 이루는 속성으로 구성된다.
# 인덱싱과 슬라이싱이 불가하다(순서가 없어서)
# key를 이용해서 값을 참조할 수 있다.

# 딕셔너리의 정의 

dic = {
    'name': 'pey',
    'phone': '010-3123-1232',
    'birth': '1123'
}
print(dic)
a = {
    1 :'hi'
}

a = {
    'a' : [1, 2, 3]
}

# 딕셔너리의 key를 다양한 유형을 사용할 수 있지만, 리스트는 key로 사용할 수 없다.

# a = {
#     [1, 2, 3] : 'hi'
# }

# 딕셔너리의 속성 추가 방법

dic = {
    'first_name' : 'john',
    'last_nmae' : 'Doe'
}

dic['age'] = 18 # 속성을 추가 (기존에 속성이 없는 경우)
dic['first_name'] = 'smith' # 속성 값을 변경 (기존에 속성이 존재하는 경우)
 
print(dic)

# 딕셔너리 속성을 삭제 : del 함수를 사용

dic = {
    'first_name' : 'john',
    'last_nmae' : 'Doe',
    'age' : 18,
    'eyecolor' :'blue'
}

del dic['age'] # key가 'age'이 속성을 삭제한다.
print(dic)

# 다른 방법으로, pop() 함수를 사용할 수 있다.


dic.pop('eyecolor')

print(dic)

# 딕셔너리의 사용

persons = {
    '김연아' : '피겨스케이팅',
    '류현진' : '야구',
    '손흥민' : '축구',
    '귀도' : '파이썬'
}

# 딕셔너리에서 key를 이용하여 값을 얻기

print(persons['김연아'])
print(persons['손흥민'])

a = {
    1:'hi'
}

print(a[1]) # 1은 인덱스가 아니고, key다

dic = {
    'name' : 'pey',
    'phone' : '010-9999-1234',
    'birth' : '1113'
}

print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 딕셔너리 만들 때 주의사항
# key값으로 리스트는 사용할 수 없다.
# 만약 같은 key가 중복되면, 맨 마지막에 정의된 속성만 존재한다.

a = {
    1:'a',
    1:'b'
}
print(a)



