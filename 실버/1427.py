# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

a=list(input())
c=""

a.sort()

for i in a:
    c+=i
  

print(c[::-1])