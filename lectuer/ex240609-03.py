# 딕셔너리 관련 함수

# 1, 딕셔너리의 key를 리스트로 만들기 : keys()

a = { 
    'name' : 'pey',
    'phone': '010-9999-1233',
    'birth': '1121'
}

result = a.keys( ) #dict_keys(['name', 'phone', 'birth'])
print(result)

result = list(result)
print(result)

print(list(a.keys()))

# 2. 딕셔너리의 value를 리스트로 만들기 : values()

a = {
    'name' : 'pey',
    'phone' : '010-9999-1234',
    'birth' : '1113'
}
result = a.values()
print(result)

result = list(result)
print(result)

print(list(a.values()))



# 3. key,value 쌍으로 list로 만들기 : items()
a = {
    'name' : 'pey',
    'phone' : '010-9999-1234',
    'birth' : '1113'
}
print(list(a.items()))

# 4, key로 value 얻기 : get()
a = {
    'name' : 'pey',
    'phone' : '010-9999-1234',
    'birth' : '1113'
}
print(a.get('name'))
print(a['name'])

# 다른 점 : 
# print(a.get('age')) # key가 없으면, None을 반환한다.
# print(a['age']) # key가 없으면 error 발생

# 5. 딕셔너리에 key가 있는지 확인하는 방법 : in
a = {
    'name' : 'pey',
    'phone' : '010-9999-1234',
    'birth' : '1113'
}
print('name' in a) # true
print('age' in a) # false


