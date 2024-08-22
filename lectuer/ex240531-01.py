# 문자열은 인덱싱이나 슬라이싱을 통해서  직접 변경할 수 없다.

a = "Pithon"

# a[1] = 'y' # error
# print(a)

a = a[0:1] + "y" + a[2:]
print(a)


