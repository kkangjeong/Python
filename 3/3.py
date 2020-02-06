#반복문

#               while 조건부분: ('조건'이 결과가 boolen이 나오는 식 의미했구나):
# (들여쓰기 유의)    수행부분

#1. 3번 출력하기
i = 1
while(i <= 3):
    i = i + 1
    print("i can")


#2. 1 이상 100이하 짝수 출력하기(while문 이용)

i = 0
while(i % 2 ==0):
    i += 2
    print(i)


# 3.(다시ㅋㅋ) 100이상 자연수 중 가장 작은 23의 배수 출력하기(while문 이용)


i = 100

while(i % 23 != 0):
    i += 1
print(i)


# 3. 다른방법(break 이용)
i = 100
while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)




# 조건문
# if문
# else if(= elif 문)

def print_grade(midterm, final):
    total = midterm + final
    if(total >= 90):
        print("You get a A")
    elif(total >= 80):
    	print("You get a B")
    elif(total >= 70):
    	print("You get a C")
    elif(total >= 60):
    	print("You get a D")
    else:
    	print("You fail")
    

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)



#4. 100이하 자연수 중 8의 배수, 12배수 아닌 것
i = 1
while(i <= 100):
    if(i % 12 == 0):
        i += 1
    elif(i % 8 ==0):
        print(i)
    i += 1



#5. 1000보다 작은 자연수 중 2 또는 3의 배수 합 출력하라

# 작은 수부터 해보기**(ex. 10보다 작은 수로)

# 작은 수부터 해보기 tip
i = 2
sum = 0
while(i < 1000):
    if(i % 2 == 0 or i % 3 == 0):
        sum += i
    i += 1    
print(sum)

# (와우 1000 주의 while문 두 실행문장 두 개 순서 때문에 )


# 6. 자연수 중 120의 약수 출력하고, 약수의 개수 출력하라

# 정수 n의 약수 : n을 나누었을 때 나누어 떨어지는 수**
# 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야


i = 1
count = 0
while(i <= 120):
    if(120 % i == 0):
        print(i)
        count = count + 1
        i += 1
	else:
        i += 1

print("120의 약수는 총 %d개입니다." % (count))


# 7. # 우승상금 : 5000만원(1988에 수령받음)
# 1) 동일 아저씨 : 은행에 돈 맡겨서 매년 이자 12%받기
# 2) 미란 아주머니 : 5000만원 짜리 아파트사기(2016년 현재 아파트 매매가 : 11억원)
# 1988년 은행에 5000만원 넣었을 경우 2016년에 얼마나 있을지 계산해서
# 2016년 은행에 저축해 둔 금액이 크면 동일아저씨말씀 맞다고 출력하고
# 아파트 가격이 더 크면 미란아주머니말씀 맞다고 출력하기

money = 50000000
apart_money = 1100000000
i = 1
while(i <= 28):
    money = money + money * 0.12
    i += 1

if(money < apart_money):
    print("%d원 차이로 미란 아주머니의 말씀이 맞습니다." % (apart_money-money))
else:
    print("%d원 차이로 동일 아저씨의 말씀이 맞습니다." % (money-apart_money))


# (다시)8. 피보나치 수열( : 첫째 항, 둘째 항이 1이고, 세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열)
# 피보나치 수열의 첫 20개 항 출력하기 

# 1 1 2 3 5 8 ...
front = 0  # previous 값
back = 1	# current 값

i = 0

while(i < 20):
    print(back)
    
    # 개념은 이건데
    # front = back
    # back = back + front
    
    # 이렇게 해야한다 -> temp 사용해야(원래 front에 있던 값 일시 보관(안 없어지게))
    temp = front
    front = back
    back = back + temp
    
    i += 1


# 9. 구구단 1단에서 9단까지(내가 짠건데 진짜 이상하네..;;)
a = 1
b = 1
while(b <= 9):
    while(a <= 8):
        print("%d * %d = %d" % (b, a, a * b))
        a += 1
    print("%d * %d = %d" % (b, a, a * b))
    a = 1
    b += 1


# 9번 답

a = 1
b = 1

while(a <= 9):
    b = 1
    while(b <= 9):
        print("%d * %d = %d" % (a, b, a * b))
        b += 1
    a += 1



# 10. break, continue문

# while문 나오고 싶으면 break문

# continue문 예제
i = 0
while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안하고 바로 조건부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)