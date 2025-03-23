# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.


number = {
    
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}





# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

# 변수만들기

# grade_point_sum += 모든 (학점 * 등급) 
# credit_sum = 학점 총합
# gpa = 모든 (학점 * 등급)  % 학점 총합
# b 는 학점 c는 등급이다


grade_point_sum=0
credit_sum=0



for _ in range (20):
    
    a,b,c= input().split()
    
    if c != "P":
        grade_point_sum += float(b) * number[c]
        credit_sum += float(b)

gpa = grade_point_sum / credit_sum
   
print(gpa)