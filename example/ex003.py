# 71.

my_variable = ()
print(my_variable,type(my_variable))

# 72.
movie_rank = ('닥터스트레인지', '스플릿', '럭키')

# 73. 
t = (1,)
print(type(t))

# 74.

#튜플은 값을 변경할 수 없다.

# 75.
t = 1, 2, 3, 4 # 튜플은 괄호를 생략할 수 있다.

# 76.

t = ('a', 'b', 'c')
t = ('A', 'B', 'C')

# 77.

interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 78.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 79.
a = tuple(range(2, 100, 2))
print(a)

# 80.
# 언팩킹 : 리스트나 튜플을 한번에 여러개의 변수에 할당하는 방법
a = [1, 2, 3, 4]
b, c, d ,e = a
print(b)
print(c)
print(d)
print(e)

# * 표현식
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, *c = my_list
print(a)
print(b)
print(c)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, *c, b = my_list
print(a)
print(b)
print(c)

# 값 바꾸기

a = 5
b = 3

a,b =  b,a
print(a,b)

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a)
print(b)
print(c)


# 81.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*a , b, c = scores
print(a)

# 82.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*a = scores
print(a)

# 83.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*a,_ = scores
print(a)

# 84.
temp = { 

}
print(type(temp))

# 85.

dic = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}

# 86.
# 딕셔너리에 새로운 속성을 추가하는 방법: 딕셔너리에 추가하고자 하는 key가 없을 경우
# 딕셔너리에 속성이 존재하는 경우 : 값을 변경한다.
dic = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}
dic['죠스바'] = 1200
dic['월드콘'] = 1500
dic['폴라포'] = 1500
print(dic)

# 87.
ice = {
    '메로나': 1000,
'폴로포': 1200, 
'빵빠레': 1800, 
'죠스바': 1200, 
'월드콘': 1500
}
print(ice['메로나'])

# 88.
ice = {'메로나': 1000,
'폴로포': 1200, 
'빵빠레': 1800, 
'죠스바': 1200, 
'월드콘': 1500}
ice['메로나'] = 1300
print(ice)

# 89.
ice = {
    '메로나': 1000,
'폴로포': 1200, 
'빵빠레': 1800, 
'죠스바': 1200, 
'월드콘': 1500
}

del ice ['메로나']
print(ice)

# 90.

# 딕셔너리에 없는 key값을 참조하려 했기 때문에  error 발생

# 91.

inventory = {
    '메로나' : [300 , 20],
    '비비빅' : [400 , 3],
    '죠스바' : [250 , 100]
}
print(inventory)

# 92.
inventory = {
    '메로나' : [300 , 20],
    '비비빅' : [400 , 3],
    '죠스바' : [250 , 100]
}
print(inventory['메로나'][0],'원')

# 93.
inventory = {
    '메로나' : [300 , 20],
    '비비빅' : [400 , 3],
    '죠스바' : [250 , 100]
}
print(inventory['메로나'][1],'개')

# 94.
inventory = {
    '메로나' : [300 , 20],
    '비비빅' : [400 , 3],
    '죠스바' : [250 , 100]
}
inventory['월드콘'] = [500, 7]
print(inventory)

# 95.
icecream = {
    '탱크보이': 1200,
      '폴라포': 1200,
        '빵빠레': 1800, 
        '월드콘': 1500, 
        '메로나': 1000
        }
print(list(icecream.keys()))

# 96.
icecream = {
    '탱크보이': 1200,
      '폴라포': 1200,
        '빵빠레': 1800, 
        '월드콘': 1500, 
        '메로나': 1000
        }
print(list(icecream.values()))

# 97.
icecream = {
    '탱크보이': 1200,
      '폴라포': 1200,
        '빵빠레': 1800, 
        '월드콘': 1500, 
        '메로나': 1000
        }
print(sum(list(icecream.values())))

# 98.
icecream = {
    '탱크보이': 1200,
      '폴라포': 1200,
        '빵빠레': 1800, 
        '월드콘': 1500, 
        '메로나': 1000
        }
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)

#99.
keys = ("apple", "pear", "peach") 
vals = (300, 250, 400)

result = dict(zip(keys, vals))

print(result)

# 100.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

result = dict(zip(date, close_price)) 
print(result)