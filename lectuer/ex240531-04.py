# f 포매팅

name = "홍길동"
age = 18
print(f"나의 이름은 {name}입니다. 나이는 {age + 10}살 입니다.")

d = {
    "name" : "홍길동",
    "age" : 18
}
print(f"나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}살 입니다.")

# 정렬

print(f"{"hi":<10}") #왼쪽 정렬
print(f"{"hi":>10}") #오른쪽 정렬
print(f"{"hi":^10}") #가운데 정렬

# 채우기

print(f"{"hi":!<10}") #왼쪽 정렬
print(f"{"hi":*>10}") #오른쪽 정렬
print(f"{"hi":=^10}") #가운데 정렬

# 소수점 표현

y =3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{y:<10.4f}')

# { } 표현하기

print(f"{{ }}")