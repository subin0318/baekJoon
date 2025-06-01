# 조건
# 두개의 값을 받는다 (성적 , 몇번째 순위)

grade , rank = map(int,input().split())
grade = list(map(int, input().split()))
grade.sort(reverse=True)
print(grade[rank-1])

