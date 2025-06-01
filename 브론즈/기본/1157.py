# 입학 OT때 누구보다도 남다르게 놀았던 당신은 자연스럽게 1학년 과대를 역임하게 되었다.
# 타교와의 조인트 엠티를 기획하려는 당신은 근처에 있는 학교 중 어느 학교가 술을 가장 많이 먹는지 궁금해졌다.
# 학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력하여라.


# execution = int(input()) # 실행 회수

# universities = {
#     "Yonsei": 10,
#     "Korea": 10000000,
#     "Ewha": 20
# }


# universities["수빈"] = 100000000000

# max_value = max(universities.values())

# for key, value in universities.items():
#     if value == max_value:
#         max_value_key = key
#         break 

# print(max_value_key)

# print(universities)


universities= {} # 대학교 이름과 알코올 소비량을 담는 딕셔너리

execution = int(input()) # 실행 횟수


for _ in range (execution):
    
    # 입력이 끝날떼 초기화
    universities= {}
    
    # 대학교 수 입력 
    universities_data= int(input())
    
    # 각 대학별 이름과 알코올 수 입력
    for _ in range (universities_data):
        universitie,alcohol=input().split()
        universities[universitie] = int(alcohol)

    max_alcohol = max(universities.values())
    
    for key, value in universities.items():
        if value == max_alcohol:
            max_universitie_alcohol = key
            break 
    
    # 가장 알코올 소비가 큰 대학교 
    print(max_universitie_alcohol)
