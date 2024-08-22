 # 문자열(string)

# 1. 큰 따옴표

a = "hello world"

# 2. 작은 따옴표

a = 'hello world'

# 3. 큰 따옴표 3개

a = """hello world"""

# 4. 작은 따옴표 3개

a = '''hello world'''

# 문자열을 만들때 주의 사항 

# 1. 큰 따옴표 문자열 안에 따옴표를 사용하는 경우 : 작은 따옴표 사용

a = "'Hello World'"

# 2. 작은 따옴표 문자열 안에 따옴표를 사용하는 경우 : 큰 따옴표 사용

a = '"Hello World"'

# 3. 큰 따옴표 문자열 안에 큰 따옴표를 사용하거나, 
# 작은 따옴표 문자열 안에 작은 따옴표를 사용하고자 하는 경우

a = "\"Hello\"World"
print(a)

a = '\'Hello\'World'
print(a)

# 문자열을 여러줄로 표현할 때,
 
a = "Hello \nWorld!"
print(a)

a = """Hello
World!"""

print(a)

a = """
Hello
World!
"""

print(a) 

# 이스케이프 문자열 

# \", \', \n, \t

print("Hello\t\tWorld")

