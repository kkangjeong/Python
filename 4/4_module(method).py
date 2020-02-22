# 1. 모듈 : 함수, 변수, 클래스 정의해놓은 파이썬 파일
# 새로운 파일에서 함수, 변수, 클래스들 불러오는 것
# test.py 에서 sum함수 쓰는 것
# * 이거쓰면 모든 함수 다겠지

# 모듈 사용법
# from 모듈파일이름 import 불러올 변수/함수/클래스
from test import sum, square
# 이렇게 꼭 써야


print(sum(2,5))
print(square(3))


# random모듈 사용법(파이썬 설치하면 제공하는 기본함수들)
from random import randint, uniform

print(randint(1, 10))   # 두 정수 사이 정수(1이상 10이하) 랜덤으로 리턴
print(uniform(0, 1))   # 두 소수 사이 수 랜덤으로



# 2. input 함수(변수 처리해야 의미있게 사용)

# input함수 리턴값은 항상 문자열// 바꿀 수 있는 방법은 형변환
name = input("이름을 입력하세요: ")
print("hello" + name)


# 3. 1과 20사이 숫자 맞추기 게임
# 4번 기회
from random import randint
i = 4
b = (randint(1, 20))
count = 0
while(i <= 4 and i >= 1):
    a = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (i)))
    i -= 1
    count += 1

    if(a == b):
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (count) )
        break
    elif(a < b):
        print("Up")
        continue
    else:
        print("Down")
        continue
if(i == 0):
    print("아쉽습니다. 정답은 %d였습니다." %(b))


