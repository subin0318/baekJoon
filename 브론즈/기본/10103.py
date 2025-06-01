# 게임은 여섯 면 주사위를 사용하며, 라운드로 진행된다. 매 라운드마다, 각 사람은 주사위를 던진다. 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게 된다. 
# 두 사람의 주사위가 같은 숫자가 나온 경우에는 아무도 점수를 잃지 않는다.

# 조건
# 1. 주사위 눈에서 눈 크기만큼 승패를 결정한다
# 2. 예를 들어  4 5 가 나오면 5가 나온 사람이 승리하면서  상대는 이기사람의 눈의 수 만큼 점수를 잃게 된다
# 3. 비기면 점수를 둘다 잃지 않는다
# 4. 둘은 점수 100점으로 시작한다


player1,player2 = 100 , 100

execution = int(input()) # 실행 횟수

for _ in range (execution) :
   
   result1, result12 = map(int, input().split()) # result1 은 player1 , result2 은 player2 결과값에 반영됨
   
   if result1 > result12 : # 게임 조건
      
      player2 -= result1
      
   elif result1 < result12 :
       
        player1 -= result12
    
   else: pass # 승패가 안날때는 pass 
    
print(player1,player2,sep="\n")




