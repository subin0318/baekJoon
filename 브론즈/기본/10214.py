# 입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스는 9줄에 걸쳐서 입력되며, 매 줄마다 해당 회의 연세대 득점 Y와 고려대 득점 K가 공백으로 구분되어 주어진다. 
# 이 두 수는 0이상 9이하이다.

T=int(input())

for i in range (T):
    Yonsei=0
    Korea=0

    for _ in range ((9)):
        Y,K=map(int,input().split())
        Yonsei+=Y
        Korea+=K

    if Yonsei > Korea : print("Yonsei")
    elif Yonsei < Korea : print("Korea")
    else: print("Draw")