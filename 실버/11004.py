#A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.

import sys

N, K = map(int, sys.stdin.readline().split())
M=list(map(int, sys.stdin.readline().split()))
M.sort()
print(M[K-1])