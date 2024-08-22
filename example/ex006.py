# 화씨를 입력하면, 섭씨를 반환하는 함수


# def temp_trans(F):
#     return(F-32)/1.8

# result = temp_trans(float(input('화씨를 입력하세요 : ')))
# print(f'{result:0.1f}')


# 201


# def print_coin():
#     print('비트코인')

# for i in range(100): 
#   print_coin() 


# def print_coins():
#    for i in range(100):
#       print("비트코인")

# print_coins()


# 사칙연산 함수

# def calculator(a,b,c):
#     if a =='+':
#         print(b + c)
#     elif a == '-':
#         print(b - c)
#     elif a == '*':
#         print(b * c)
#     else:
#         print(b / c)
       

# calculator('+', 5, 10)
# calculator('-', 10, 5)
# calculator('*', 3, 5)
# calculator('/', 10, 5)

# 215

# def print_with_smile(문자열) :
#     print(문자열 + ':D')

# print_with_smile('안녕하세요')

# 217

# def print_upper_price(int) : 
#     print(int * 1.3)

# print_upper_price(100) 

# 218
# def print_sum(a,b):
#     print(a + b)

# print_sum(2,3)
# 219

# def print_arithemtic_opertation(a,b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)

# print_arithemtic_opertation(3,4)

# def print_max(a,b,c):
#     if a > b and a > c:
#      print(a)
#     elif b > a and b > c:
#      print(b)
#     else:
#      print(c)

# print_max(3,4,6)


# 221
# def print_reverse(string):
#    print(string[::-1])



# print_reverse('Python')

# 222
# def print_score(list):
#    print(sum(list)/len(list))

# print_score([1,2,3])


# 223

# def print_even(list):
#     for i in list:
#      if i % 2 == 0:
#         print(i)

# print_even([1,3,2,10,12,11,15])


# # 224

# # 딕셔너리를 for in, value(변수)에 key값이나온다.
# def print_keys(dictionary):
#    for i in dictionary:
#       print(i)

# print_keys({"이름":"김말똥","나이":30,"성별":"여자"})

# # 225

# my_dict = {"10/26" : [100, 130, 100, 100],
# "10/27" : [10, 12, 10, 11]}

# def print_value_by_key(my_dict,keys):
#    print(my_dict[keys])


# print_value_by_key  (my_dict, "10/26")


# 226

def print_5xn(string,num):
   lines = int(len(string) / num)
   for i in range(lines + 1):
      print(string[i * num:i* num + num])

print_5xn("아이엠어보이유",3)


# 228

def calc_monthly_salary(annual_salary):
   month_money = print(int(annual_salary / 12))
   return annual_salary


calc_monthly_salary(1200000)

# 232


def make_url(string):
   url = 'www.' + string +".com" 
   return url

result = make_url("naver")
print(result)


# 233

def make_list(string):
   return list(string)


print(make_list('abcd'))

def make_list(string):
   my_list = []
   for 변수 in string:
      my_list.append(변수)
   return my_list


# 234
def pickup_even(my_lsit):
   new_list = []
   for i in my_lsit:
      if i % 2 == 0:
         new_list.append(i)
   return new_list


print(pickup_even([3,4,5,6,7,8]))


# 235


def convert_int(str):
   return int(str.replace(',',''))

print(convert_int("1,234,567"))
      

# 236


   
   

