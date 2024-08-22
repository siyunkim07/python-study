 # Python의 기본 연산자 (사직연산)

num_1 = 3
num_2 = 4

result = num_1 + num_2  # 더하기
print(result)

result = num_1 - num_2  # 빼기
print(result)

result = num_1 * num_2  # 곱하기
print(result)

result = num_1 / num_2  # 나누기 : 나누기 결과값은 항상 실수가 됨.
print(result)

# 제곱을 나타내는 ** 연산자

a = 3
b = 4
result = a ** b # 3 * 3 * 3 * 3
print(result)

# % : 어떤수를 어떤수로 나누었을 때, 나머지를 구함.

a = 7 
b = 3
result = a % b
print(result)

result = b % a
print(result)

# 어떤 수가 짝수인지 홀수인지 구분하는 방법

# 어떤 수를 2로 나누어서 나머지가 0이면 : 짝수 
# 어떤 수를 2로 나누어서 나머지가 1이면 : 홀수 

a = 13
result = a % 2
print(result)

a = 8
result = a % 2
print(result)

# // : 어떤 수를 어떤 수로 나누었을 때, 몫을 구하는 연산자

a = 7
b = 4

result = a//b
print(result)