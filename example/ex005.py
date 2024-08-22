# 131
# fruits = ["사과", "귤", "수박"]
# for fruit in fruits:
#     print(fruit)

# 133
변수 = 'A'
변수 = 변수.lower()
print("변환:", 변수)
변수 = 'C'
변수 = 변수.lower()
변수 = 'C'
변수 = 변수.lower()

# 136

리스트 = [10, 20, 30]
for 변수 in 리스트 :
  print(변수)

# 138
리스트 = [10, 20, 30]
for 변수 in 리스트:
  print("-------")

# 139
print("++++")
for 변수 in [10, 20, 30] :
  print(변수)

  # 140
for 변수 in [1, 2, 3, 4]:
  print('-------')

# 141
리스트 = [100, 200, 300]
for 변수 in 리스트:
  print(변수 + 10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for 변수 in 리스트:
  print("오늘의 메뉴:",변수)

# 143
length = len(변수)
리스트 = ['sk하이닉스', '삼성전자', 'LG전자']
for  변수 in 리스트:
  print(length)

# 144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
  print(i, len(i))

# 145
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
  print(i[0])

# 146
리스트 = [1, 2, 3]
for i in 리스트:
  print(f"3 x {i}")

# 147
리스트 = [1, 2, 3]
for i in 리스트:
 print(f"3 x {i} = {3 * i}")

 # 148
 리스트 = ['가', '나', '다', '라']
 for i in 리스트[1:]:
   print(i)
   
   # 149
 리스트 = ['가', '나', '다', '라']



 # 150
리스트 = ['가', '나', '다', '라']
for i in 리스트[::-1]:
  print(i)

# 151
리스트 = [3, -20, -3, 44]
for i in 리스트:
  if  i < 0:
    print(i)
else:
  pass

# 152
리스트 = [3, 100, 23, 44]
for i in 리스트:
  if i % 3 == 0:
    print(i)


# 153.

리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
  if i < 20 and i % 3 == 0:
    print(i)


# 154
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
  if len(i) > 3 :
    print(i)

# 155
리스트 = ["A", "b", "c", "D"]
for  i in 리스트:
  if i.isupper() == True:
    print(i)

# 156
리스트 = ["A", "b", "c", "D"]
for  i in 리스트:
  if i.islower() == True:
    print(i)

# 157
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
  print(i[0].upper() +i[1:])

# for i in 리스트:
#   print(i.capitalize())

# 158

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
  print(i.split(".")[0])

# 159

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  if i.split(".")[1] == 'h':
    print(i)

# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  if i.split(".") == "h" or i.split(".") == "c":
     print(i)

# for 문에서의 range() 
# range(시작값, 종료값, step)
# range(값) : 시작값(0)과 step(1)이 생략된 것임

value = range(10)
print(list(value))

for i in range(10) :
  
# step이 음수가 될 수 있다. 
# step이 음수가 되면, 시작값이 종료값보다 크야 한다.

 for i in range(0, 10, -1):
  print(i)





# 161
for i in range(100):
  print(i)

# 162
for i in range(2002,2051,4):
 print(i)

# 163
for i in range(3,31,3):
  print(i)

# 164
for i in range(99,0,-1):
  print(i)

# 165
for i in range(10):
  print(i / 10)

# 166
for i in range(1,10):
  print(f"3 x {i} = {i * 3}")

# 167
for  i in range(1,10,2):
  print(f"3 X {i} = {3 * i}")

  # 168
  total = 1
for i in range(1,11):
  total = total * i

print(total)
  
# 171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(i, price_list[i])


# 172

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print('ㅇ')


# 174
price_list = [32100, 32150, 32000, 32500]
for i in range(1,len(price_list)):
  print(90 + 10 * i, price_list[i])


# 175
my_list = ["가", "나", "다", "라"]
# print(my_list[0] , my_list[1])
# print(my_list[1] , my_list[2])
# print(my_list[2] , my_list[3])

# for i in range(len(my_list)-1):
#   print(my_list[i] , my_list[i + 1])



# 176
my_list = ["가", "나", "다", "라", "마"]
# print(my_list[0], my_list[1], my_list[2])
# print(my_list[1], my_list[2], my_list[3])
# print(my_list[2], my_list[3], my_list[4])

# for i in range(len(my_list)-2):
#   print(my_list[i], my_list[i + 1], my_list[i + 2])

# 177
my_list = ["가", "나", "다", "라"]
# print(my_list[3], my_list[2])
# print(my_list[2], my_list[1])
# print(my_list[1], my_list[3])

for i in range(len(my_list)-1, 0, -1):
 print(my_list[i], my_list[i - 1])


# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
  print(my_list[i + 1] - my_list[i])

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
  print((my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3)

# 180
low_prices  = [100, 200, 400, 800, 1000] 
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
  print(volatility.append(high_prices[i]- low_prices[i]))
print(volatility)


# 181
apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]


# 182
stock = [['시가', 100, 200, 300], ['종가', 80, 210, 330]]

# 183
stock = {
  '시가' : [100, 200, 300],
  '종가' : [80, 210, 330]
}

# 184

stock = {
  '10/10' : [80, 110, 70, 90],
  '10/11' : [230, 190, 200]
}

# 185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j,'호')

# 186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
  for j in i:
    print(j,'호')
  

# 187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
  for j in i[::-1]:
    print(j,'호')


# 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j)
    print('-----')
# 189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j)
  print('-----')
# 190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
  for j in i:
    print(j)
print('-----')


# 191
data = [
  [2000, 3050, 2050, 1980],
  [7500, 2050, 2050, 1980],
  [15450, 15050, 15550, 14900]
]
# 192
for i in data:
  for j in i:
    print(j * 1.00014)
  print('----')
# 193
result = []
for i in data:
  for j in i:
    result.append(j)
print(result)

# 194
result = []
for i in data:
  result1 = []
  for j in i:
    result1.append(j)
  result.append(result1)
print(result)

# 195
ohlc = [["open", "high", "low", "close"], 
[100, 110, 70, 100],
[200, 210, 180, 190], 
[300, 310, 300, 310]]

for i in ohlc[1:]:
  print(i[-1])

# 196
ohlc = [["open", "high", "low", "close"], 
[100, 110, 70, 100],
[200, 210, 180, 190], 
[300, 310, 300, 310]]
for i in ohlc[1:]:
  if i[-1] > 150:
    print(i[-1])


# 197
ohlc = [["open", "high", "low", "close"], 
[100, 110, 70, 100],
[200, 210, 180, 190], 
[300, 310, 300, 310]]
for i in ohlc[1:]:
  if i[-1] >= i[0]:
    print(i[-1])


# 198
ohlc = [["open", "high", "low", "close"], 
[100, 110, 70, 100],
[200, 210, 180, 190], 
[300, 310, 300, 310]]
volatility =[]
for i in ohlc[1:]:
  volatility.append(i[1] - i[2])
print(volatility)  
   

# 199
ohlc = [["open", "high", "low", "close"], 
[100, 110, 70, 100],
[200, 210, 180, 190], 
[300, 310, 300, 310]]
for i in ohlc[1:]:
  if i[-1] > i[0]:
    print(i[1]-i[2])


# 200
ohlc = [["open", "high", "low", "close"], 
[100, 110, 70, 100],
[200, 210, 180, 190], 
[300, 310, 300, 310]]
profit = 0
for i in ohlc[1:]:
  profit = profit + (i[-1] - i[0])
print(profit) 