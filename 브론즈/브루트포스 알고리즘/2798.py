# 블랙잭

# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며,
# 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.


# 예제 입력
# 5 21(블랙잭 수)
# 5 6 7 8 9 (숫자카드 3장 합이 21을 넘어서는 안되거나 같아야한다)

# 21


# N , M = map(int,input().split())

# cards = list(map(int,input().split()))

# result = 0

# number_list=[]
# result_list= []

# for i in range (len(cards)) :
#     for j in range (i+1,len(cards)) :
#          for k in range (j+1,len(cards)) :
#              result = cards[i] + cards[j] + cards[k]
#              number_list.append(result)
             

# for x in number_list:
#     if x <= M:
#         result_list.append(x)
        
# print(max(result_list))


# cards= [3,4,5,6,7,8,9]

# for i in range (len(cards)) : 
#     for j in range (i+1,len(cards)) : # 첫번째 카드와 다른 카드를 선택 해야 하므로 i+1 부터 시작
#          for k in range (j+1,len(cards)) :

# 5중 3장을 뽑는다고 가정하자 한장을 뽑으면 중복이 안되기에 -1 을 해야 한다 N , N-1 , N-2 가 된다 그걸
#  파아썬으로 구현한다면 3중 for문을 쓸수 있다


