# 첫째 줄에 입력으로 주어진 16진수 수를 10진수로 변환해 출력한다.

# 16진수 A는 10부터 F 15이다 1
# 0 ~ 9 의 16진수 출력a

# 10 11 12 13 14 15


# 1
# result = {
#     'A' : 10 ,
#     'B' : 11 ,
#     'C' : 12,
#     'D' : 13,
#     'E' : 14,
#     'F' : 15
# }

# a= input()

# k=a.upper()

# print(result[k])

#2

# int() 함수로 바꿔주면 된다

a=input()

b= int(a,16)

print(b)