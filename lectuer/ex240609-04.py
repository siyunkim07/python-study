# set은 집합과 관련된 자료형

# set을 생성하는 방법
# 1. set(list) 사용

s1 = set([1, 2, 3]) #튜플로도 사용가능 set((1, 2, 3))
print(s1)

# 2. 리터럴 방식
s1 = {1, 2, 3}
print(s1)

# set의 특징

# 중복허용 X
# 순서가 없다.(인덱싱과 슬라이싱 사용x)

s1 = set([1, 2, 3])
# s1[0] <- error

# set가 값을 참조하는 방법 :list나 튜플로 변환하여 참조

s1 =list(s1)
print(s1)

# set의 가장 대표적인 활용법
# 리스트나 튜플의 중복 data를 없앨 때

lst = [1, 2, 3 , 1, 2, 3, 4, 5, 6, 4, 5 , 7 ,8 ,9]
s1 = set(lst)
l1 = list(s1)
print(l1)

# 2. 차집합, 합집합, 교집합을 구할 때     #전역함수 매서드 함수 차이

s1 = set([1, 2, 3, 4, 5, 6]) 
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 : &, intersection()

lst = list(s1 & s2)
print(lst)

lst = s1.intersection(s2)
print(lst)

lst = s2.intersection(s1)
print(lst)

# 합집합 '|'사용
s1 = set([1, 2, 3, 4, 5, 6]) 
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 | s2)
print(s1.union(s2))

print(s2 | s1)
print(s2.union(s1))

# 차집합 '-' 사용

s1 = set([1, 2, 3, 4, 5, 6]) 
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 - s2) 
print(s1.difference(s2))

print(s2 - s1) 
print(s2.difference(s1))



# 집합 자료형 (Set) 관련 함수

# 1. 값을 1개 추가하기 - add() 함수

s1 = set([1, 2, 3])
s1.add(4)
print(s1) # set은 순서가 없기 때문에, 경우에 따라 매번 달라보인다.

# 2. 값을 여러개 추가하기 - update() 함수

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)


# 3. set에서 특정한 값을 삭제하는 경우 - remove() 사용

s1 = set([1, 2, 3])
s1.remove(2)  # 삭제하려는 값
print(s1)

