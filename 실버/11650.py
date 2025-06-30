# 좌표 정렬하기

# 조건
# 1. 입력할 좌표의 갯수를 입력한다
# 2. 입력된 자표들 끼리 작은순부터 큰 수로 정렬한다

# 5 (좌표 입력 갯수)
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

# 결과
# 1 -1 
# 1 1  
# 2 2  
# 3 3   
# 3 4    

# 여기서 알수 있는거 x 좌표를 기준으로 본다 비교할 x 좌표가 같다면 다음은 y좌표를 본다 y 좌표까지 비교한 후 ㅈ정렬한다



# data = [[1,2], [2,2], [5,1], [0,0], [3,1]]

# sorted_data = sorted(data, key=sum)

# print(sorted_data)
    


# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

# 결과
# 1 -1 
# 1 1  
# 2 2  
# 3 3   
# 3 4  

N = int(input())


coordinate = []

for i in range (N):
    
    x,y = map(int,input().split())
    
    coordinate.append([x,y])
    

sorted_coordinate = sorted(coordinate)

for k in sorted_coordinate:
    print(k[0],k[1])
    


    
