# 리스트 []
numbers = [1, 2, 3, 4, 5, 6]
names = ["정인", "강정", "강인", "인정"]

print(numbers)      #결과 : [1, 2, 3, 4, 5, 6]
print(names)



# 리스트_인덱싱(파이썬에는 *마이나스 인덱스 있다)
print(numbers[1] + numbers[-6])


# 리스트_슬라이싱
print(numbers[0:4])  #0부터 3까지*
print(numbers[2:])  #2부터 끝까지
print(numbers[:3])  #0부터 2까지

print(numbers[0:-3])    #주의 [1, 2, 3]


# 리스트 +로 연결하기 가능
a = ["a","b","c"]
b = ["d","e","f"]
c = a + b
print(c)



# 리스트 함수
# 1. len
# 2. append  (메소드)
numbers = []
print(len(numbers))
numbers.append(5)       #끝*에 추가
print(numbers)
numbers.append(8)       
print(numbers)


# 3. del
numbers = [1, 2, 3, 4, 5, 6, 7 , 8]

del numbers[3]          
print(numbers)


# 4. insert
numbers.insert(5, 0)        #인덱스 5에!! 삽입되어서 뒤에 것들 밀려남//[1,2,3,5,6,7,8]에서 [1,2,3,5,6,0,7,8]
print(numbers)


# 5. sorted (함수 : 새로운 리스트 생성해서 리턴)
print(sorted(numbers))      # 오름차순 정렬


# 6. sort(메소드 : 새로운 리스트 생성 x )
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)



# 7. in함수** :  어떤 값이 리스트에 있는지 확인하는 함수(너무 자주 있는 일이라서 함수로// 결과는 True or False)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 not in primes)




# ( in함수 없었으면 이렇게 코딩
#  value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False


# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))


#  )





# 8. reverse 
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)


# 9. index
# 해당하는 인덱스 리턴
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


# 10. remove
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)





# 리스트 안의 리스트(Nested List)

# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)











# 화씨 온도를 섭씨 온도로 바꿔주는 프로그램(len()함수 조건문에 자주 사용)

def fahrenheit_to_celsius(fahrenheit):
    i = 0
    while(i < len(sample_temperature_list)):
        sample_temperature_list[i] = round((sample_temperature_list[i]-32)*5/9, 2)
        i += 1

sample_temperature_list = [40, 15, 32, 64, -4, 11]

print("화씨 온도 리스트: " + str(sample_temperature_list))

fahrenheit_to_celsius(sample_temperature_list)

print("섭씨 온도 리스트: " + str(sample_temperature_list))







# 리스트 함수 활용 문제

numbers = []

# numbers에 자연수 1부터 10까지 추가
i = 1
while(i <= 10):
    numbers.append(i)
    i += 1
print(numbers)

# numbers에서 홀수 제거**(9부터 0 순서로 가는 게 좋다 -> (지우는 거라서)하나지우면 한칸씩 앞으로 오니까)
i = len(numbers) - 1
while(i >= 0):
    if(numbers[i] % 2 == 1):
        del numbers[i]
    i -= 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0,20)
print(numbers)

# numbers를 정렬해서 출력
print(sorted(numbers))







# 0 ~ 9 다른 세 개 랜덤 뽑기 (아예 다시 풀기)
# 컴퓨터는 0과 9 사이의 서로 다른 세 숫자를 임의의 순서로 뽑습니다. 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추려고 합니다.

# 컴퓨터는 사용자가 입력한 세 숫자에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.

# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
# 예를 들어 컴퓨터가 1, 2, 3을 생성하였는데, 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
# 기회는 무제한입니다. 하지만 몇번의 시도 끝에 맞췄는지 기록됩니다.

# 3S(세 숫자의 값과 위치를 모두 맞춘 경우)일 때 게임이 끝납니다.



# 모범 답안        
from random import randint

# 번호 뽑기
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers

# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0        # 시도 횟수
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수

# 3S 될 때까지 반복이니까
while strike_count < 3:
    # 번호 3개 입력 받기
    guess = []
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우에만 추가
        new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

        # 범위를 벗어나면 설명 메시지 출력
        if new_number < 0 or new_number > 9:
            print("0에서 9까지의 수를 입력해주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif new_number in guess:
            print("새로운 수를 입력해주세요!")
        # 타당한 값이면 guess에 추가
        else:
            guess.append(new_number)

    # 스트라이크, 볼 개수 세기
    strike_count = 0 # 스트라이크 개수
    ball_count = 0   # 볼 개수
    i = 0            # 인덱싱 변수

    while i < 3:
        if guess[i] == ANSWER[i]:
            strike_count = strike_count + 1
        elif guess[i] in ANSWER:
            ball_count = ball_count + 1
        i = i + 1

    print("%dS %dB" % (strike_count, ball_count))

    # 시도 횟수 추가
    tries = tries + 1

# 축하 메시지
print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))
