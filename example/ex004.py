# 101.

# True, False 값을 갖는 data type : bool

# 111
# user_input = input("입력 : ")
# print(user_input * 2)

#112.

# user_input = int(input('숫자를 입력하세요 : '))
# print(user_input + 10)

# 113.

# user_input = int(input('숫자를 입력하세요 : '))
# if user_input % 2 == 0: 
#     print('짝수')
# else:
#     print('홀수')

# 114.
# user_input = int(input('입력값 : '))
# result = user_input + 20 
# if result  > 255:
#     print(255)
# else:
#     print(result)


# 115.

# user_input = int(input('입력값 : '))
# result = user_input - 20
# if result < 0:
#     print(0)
# elif result > 255:
#     print(255)
# else:
#     print(result)

# 116.

# time = input('현재 시간 : ')

# if time[-2:] == "00":
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')

# 117.
# user_input = input('좋아하는 과일은?')
# fruit = ['사과', '포도', '홍시']
# if user_input in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')

# 118. for문에서의 in : 리스트, 튜플 -> 값
# it_company_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input('회사명 : ')
# if user in  it_company_list:
#     print('입사 희망 회사 입니다.')
# else:
#     print('입사 희망 회사가 아닙니다.')


# 119. 딕셔너리에서 기본적으로 for ~ in 문을 사용하면,
# 변수값에는 key값이 검색이 된다.
# fruit = {
#     "봄" : "딸기",
#     "여름" : "토마토",
#     "가을" : "사과"
# }
# favor = input('제가좋아하는 계절은 :')
# if favor in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')

# 120.
# fruit = {
#     "봄" : "딸기",
#     "여름" : "토마토",
#     "가을" : "사과"
# }
# favor = input('제가 좋아하는 과일은 :')
# if favor in fruit.values() : 
#     print('정답입니다.')
# else:
#     print('오답입니다.')

# 121.
# user = input('문자를 입력하세요:')
# letters = user.islower()
# if letters == True:
#     print(user.upper())
# else:
#     print(user.lower())

# 122.
# score = input("학점을 적으세요:")
# score = int(score)
# if score >= 0 and score <= 20:
#     print('E')
# elif score >= 21 and score <= 40 :
#     print('D')
# elif score >= 41 and score <=60 :
#     print('C')
# elif score >=61 and score <=80 :
#     print('B')
# elif score >= 81 and score <= 100:
#     print('A')
# else: 
#     pass

# 123. split() 함수와 언패킹 사용
# 환율 = { '달러' : 1167, '엔' : 1.096, '유로' : 1268, '위안' : 171}
# user = (input('금액 통화 :'))
# num, currency = user.split()
# print(f'{float(num) * 환율[currency]} 원')

# 124.
# user1 = int(input('input number1 :'))
# user2 = int(input('input number2 :'))
# user3 = int(input('input number3 :'))
# if user1 > user2 and user1 > user3:
#     print(user1)
# elif user2 > user1 and user2 > user3:
#     print(user2)
# else:
#     print(user3)


# 125.
# number = (input('휴대전화 번호 입력 : '))
# num = number.split('-')
# num = num[0]
# if num == '011':
#     print(f'당신은 {num.values} 사용자입니다.')
# elif num == '016':
#     print(f'당신은 {num.values} 사용자입니다.')
# elif num == '019':
#     print(f'당신은 {num.values} 사용자입니다.')
# else:
#     print('당신은 알수없음 사용자입니다')


# 126.
# num = input('우편번호 : ')
# num = num[2]
# if num in [0,1,2]:
#     print('강북구')
# elif num in [3,4,5]:
#     print('도봉구')
# else:
#     print('노원구')

# 127.

# id = input('주민등록번호 : ')
# id = id.split("-")[1]
# if id[0] in['1', '3']:
#     print('남자')
# elif id[0] in ['2', '4']:
#     print('여자')
# else:
#     print('잘못된 주민번호')

# 128.
# local_code = input('주민등록번호 : ')
# local_code = local_code.split('-')[1]
# local_code = int(local_code[1:3])

# if 0 <= local_code <= 8:
#     print('서울입니다.')
# else:
#     print('서울이 아닙니다.')



# # 129.
# id = input('주민등록번호 : ')
# 계산1 = int(id[0]) * 2 + \
#         int(id[1]) * 3 + \
#         int(id[2]) * 4 + \
#         int(id[3]) * 5 + \
#         int(id[4]) * 6 + \
#         int(id[5]) * 7 + \
#         int(id[7]) * 8 + \
#         int(id[8]) * 9 + \
#         int(id[9]) * 2 + \
#         int(id[10]) * 3 + \
#         int(id[11]) * 4 + \
#         int(id[12]) * 5 
         
        

# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)

# if id[-1] == 계산3[-1]:
#     print('유효한 주민등록번호입니다.')
# else:
#     print('유효하지 않은 주민등록입니다.')


# 130.

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])
# if (시가 + 변동폭) > 최고가 :
#     print('상승장')
# else:
#     print('하락장')




