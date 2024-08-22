# while 문 : 반복문

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print('나무를 %d번 찍었습니다.' % treeHit)
#     if treeHit ==10:
#         print('나무 넘어갑니다.')

# prompt = """  
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# ... Enter number: """ 
# number = 0
# while number != 4: 
#     print(prompt)
#     number = int(input())
# 초기값
# coffee = 10

# while True:
#     money = int(input('돈을 넣어 주세요: '))
#     if money == 300:
#         print('커피를 줍니다.')
#         coffee = coffee -1
#     elif money > 300:
#         print('거스름돈 %d를 주고 커피를 줍니다.' % (money - 300))
#         coffee = coffee -1
#     else:
#         print('돈을 다시 돌려주고 커피를 주지 않습니다.')
#         print('남은 커피의 양은 %d개 입니다.' % coffee)

#     if coffee == 0:
#         print('커피가 다 떨어졌습니다. 판매를 중지 합니다.')
#         break

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 1:
#         continue
#     print(a)


# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")



# for문

# test_list = ['one',  'two', 'three']

# for i in test_list:
#     print(i)

# my_list = [1, 2, 3, 4 , 5, 6, 7, 8 ,9, 10]
# for i in my_list[1::2]:
#     print(i) 

# # for문의 사용
# a = [(1,2), (3,4), (5,6)]

# # 언팩킹 : (first, last) = (1, 2)

# for (first, last) in a:
#     print(first, last)


# for문의 응용

# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks: # 리스트, 튜플, 문자열, 딕셔너리
#     number = number + 1
#     if mark >= 60:
#       print('%d번 학생은 합격입니다.' % number)
#     else:
#       print('%d번 학생은 불합격입니다.' % number)

# for문에서의 continue
# for문에서 continue문을 만나면, continue문 이하의 명령문은 실행하지 않고,
# 바로 다음 Loop를 진행한다.

# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60:
#         continue
#     print("%d번 학생은 합격입니다.")

#  for문과 함께 사용되는 range() 함수

# range(시작값, 종료값, step) 함수 :  
# 시작값 : 시작하는 값
# 종료값 : 종료하는 값 , 종료값은 포함하지 않는다. 바로 앞까지 포함.
# step : 증감 혹은 건너뜀을 의미.

# a = range(0, 10)
# print(tuple(a))    

# a = range(0, 10, 2)
# print(tuple(a))    

# step을 음수로 주면 뒤에서 부터 시작을 한다.
# a = range(10, 0, -1)
# print(list(a))

# a = range(10) # 앞 시작값이 0이 생략되었다.


# add = 0

# for i in range(1, 11) :
#     add = add + i # add += 1 


# print(add)

# for와 range를 사용하여 구구단의 결과값 출력하기

# for i in range(2,10):
#     for j in range(1,10):
#         print(i * j, end = " ")
#     print()

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} x {j} = {i * j}')
#     print()
      
# 리스트 컴프리헨션 

# a = [1, 2, 3, 4]

# result = []
# for num in a:
#     result.append(num * 3)
# print(result)

# result = [num * 3 for num in a ]
# print(result)

# a = [1, 2, 3, 4]

# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)