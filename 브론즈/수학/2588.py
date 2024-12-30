# 세자리수 곱하기 

a=int(input())
b = list(input())

print(a*int(b[2]),a*int(b[1]),a*int(b[0]),a*(int(b[0])*100 + int(b[1])*10 + int(b[2])),sep="\n")

