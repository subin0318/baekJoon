a, b = map(int, input().split())

if a < b:
    print(1, 0, end=" ")
elif a == b:
    print(0, 1, end=" ")
else: # a > b 인 경우
    print(0, 0, end=" ") # 예시: 앞선 두 케이스와 구분되는 값 출력