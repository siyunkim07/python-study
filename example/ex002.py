# 51.

movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 52.

movie_rank.append('배트맨')

# 53.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 54.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
del movie_rank[2]
print(movie_rank)

# 55.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

# 56.
lang1 = ["C", "C++", "JAVA"] 
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 57.
nums = [1, 2, 3, 4, 5, 6, 7]

print("max :", max(nums))
print("min :", min(nums))

# 58.
nums = [1, 2, 3 ,4 ,5]
print(sum(nums))

# 59.

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소 시지", "라면", "팥빙수", "김치전"]
print(len(cook))


# 60.
nums = [1, 2, 3, 4, 5, 6, 7]
a = sum(nums)
b = len(nums)
print(a / b)

# 61.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 64.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65. 
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 66. # joi() 함수는 리스트를 문자열로 변환한다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = " ".join(interest)
print(result,type(result))

# 67.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 68.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 69. split(구분자_문자열) : 문자열을 리스트로 변환하는 함수
string = "삼성전자/LG전자/Naver"
result = string.split("/")
print(result)

# 70.  
data = [2, 4, 3, 1, 5 ,10, 9]

# sort() 메서드는 본래의 리스트를 정렬해서 변경한다.
data.sort()
print(data)

# 다른 방법으로는 sorted() 내장함수 사용 - 본래의 data를 변경하지 않고 정렬된 새로운 리스트를 생성한다.

data = [2, 4, 3, 1, 5 ,10, 9]
sorted_data = sorted(data)
print(sorted_data)
print(data)







