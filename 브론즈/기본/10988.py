# a=input()

# if a[0] == a[::-1] :print(1)
# else: print(0)

# print(a[0])
# print(a[::-1])

a=input()
if a == a[::-1] : print(1) 
# 파이썬에서는 문자열도 일종의 시퀀스 자료형으로 취급하여 리스트와 비슷하게 쓸수있어 a[::-1] 을 쓸수있는거다
else: print(0)

