# 리스트 관련 함수

# 1. 리스트의 요소 추가하기 : append() 함수
# 리스트의 맨 마지막에 요소값을 추가한다.

a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 2, 3]
a.append([4, 5])
print(a)

# 2. 리스트의 정렬 : sort( ) 함수
# 리스트의 요소를 순서대로 정렬해 준다.

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'd', 'b']
a.sort()
print(a)

# 3. 리스트의 순서 뒤집기 : reverse()
# 리스트의 순서를 역순으로 바꾼다.
a = ['a', 'c', 'b']
a.reverse()
print(a)

a = ['a', 'c', 'b']
a.sort()
a.reverse()
print(a)

# 4. 리스트의 인덱스를 반환 : index() 함수
#  리스트의 어떤값의 인덱스를 찾을 때 사용

a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# print(a.index(5)) <- 오류

# 4. 리스트의 요소 삽임 : insert() 함수
# insert(인덱스,값)

a = [1, 2, 3]
a.insert(0,4)
print(a)

a.insert(3,5)
print(a)

# 5. 리스트 요소를 제거 : remove() 함수
# remove(x) -> 리스트에서 첫번째 만나는 값을 제거

a = ['a', 'b', 'c','b', 'e']
a.remove('b')
a.remove('b')
print(a)

# 6. 리스트의 요소를 끄집어 내기 : pop() 함수

a = [1, 2, 3]
b = a.pop()    # 맨 마지막 요소를 끄집어 낸다.
print(b)
print(a)

a = [1, 2, 3]
b = a.pop(1) # 1번째 인덱스 위치에 있는 값을 끄집어 낸다.
print(b)
print(a)

# 7. 리스트에 포함된 요소의 갯수 세기 : count() 함수

a = ['a', 'b', 'c' ,'b','e']
print(a.count('b'))

# 8. 리스트의 확장 : extend() 함수
# extend(x) => x는 리스트만 올수 있다.
# extend() 함수는 리스트의  + 연산자와 똑같다.

a = [1, 2, 3]
a.extend([4,5])
print(a)

b = [6,7]
a.extend(b)
print(a)
