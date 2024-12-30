# 첫 줄에는 
# A, B, C를 수로 생각했을 때, 
# A+B-C를 출력하세요.

# 둘째 줄에는 
# A, B, C를 문자열로 생각했을 때, 
# A+B-C를 출력하세요.

a=[]

for i in range (3):
    i=input()
    a.append(i)

print(( int(a[0]) + int(a[1] )) - int(a[2]))
print(int(a[0]+a[1])-int(a[2]))

