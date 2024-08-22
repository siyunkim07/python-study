# 문자열의 함수들

# 1. 문자 갯수 세기 - count
 
a = "hobby"
result = a.count('b')
print(result,'개')

# 2. 문자 위치 알려 주기 - find
# 만약에 찾고자 하는 문자나 문자열이 없으면, -1을 반환한다.
# 찾고자 하는 문자나 문자열의 첫번재 위치만 찾는다.
a = "Python is the best choice"
result = a.find('b')
print(result)

result = a.find('z')
print(result)
# 3. 문자 위치 알려 주기 - index
# 찾고자 하는 문자나 문자열의 첫번재 위치만 찾는다.
# 만약에 찾고자 하는 문자나 문자열이 없으면, error가 발생함.

a = "Life is too short"
print(a.index('t'))

a = "Life is too short"
print(a.index('t'))

# 4. 문자열의 삽입 - join

print(",".join('abdf')) #문자열에 삽입
print(",".join(['a' , 'b' , 'c', 'd'])) #문자열에 삽입

# 5. 소문자를 대문자로 바꾸기 - upper
a = "hi"
result = a.upper()
print(result)

# 6. 대문자를 소문자로 바꾸기 - lower
a = "HI"
result = a.lower()
print(result)

# 7. 공백을 지우기 : 문자열의 왼쪽, 오른쪽의 공백을 지는 함수 - strip
a = "       hi       "
result = a.strip() # 왼쪽, 오른쪽 공백을 모두 제거
print(result)
result = a.lstrip() # 왼쪽 공백만 모두 제거
print(result)
result = a.rstrip() # 오른쪽 공백만 모두 제거
print(result)

# 8. 문자열 바꾸기 -replace
a = "Life is too short"
result = a.replace("Life", "Your leg")
print(result)
 
# 9. 문자열을 나누기 - split
# 결과가 리스트를 반환한다.

a = "Life is too short"
print(a.split(" "))
print(a.split())

a = "a:b:c:d"
result = a.split(":")
print(result)

# 10. 앞에서 배운 모든 함수는 원래 본래의 문자열은 절대로 변경하지 않는다.
# 함수를 실행하면, 항상 새로운 문자열을 반환함.
 
a = "LIFE"
result = a.lower()
print(result)
print(a)

# 문자열은 문자열의 일부를 절대로 변경할 수 없다.

a = "Life"
a = "LIFE"
print(a)


