# 반복문_for

# while문을(리스트 인덱스 필요할 때)
fruit = ["딸기", "포도", "복숭아", "수박", "귤"]

i = 0
while(i < len(fruit)):
    print(fruit[i])
    i += 1

# for문으로(리스트 인덱스 필요없을 때)(형식 암기)
fruit = ["딸기", "포도", "복숭아", "수박", "귤"]

for item in fruit:
    print(item)

 # 1, 3, 5, 7, 9 의 제곱 출력하기(간단히)
for num in [ 1, 3, 5, 7, 9 ]:
    print(num*num)

# range 함수(1부터 100 일일이 다 칠 수 없어서//리스트 대신//메모리 효율성 굿)

# 1부터 9까지
for i in range(1, 10):
    print(i)

# 항상 0부터 (9까지)**
for i in range(10):
    print(i)

# 세번째꺼는 간격
for i in range(3, 17, 3):
    print(i)




# numbers라는 리스트가 주어졌습니다. 
# for문과 range 함수를 사용하여 numbers의 인덱스와 원소를 출력해보세요.
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(0, 8):
    print(str(i)+ " " + str(numbers[i]))

# 이렇게도
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(len(numbers)):
    # 파이썬에서는 자동으로 띄어쓰기 된다 i랑 numbers[i](여러 값 쓰면 자동 띄어쓰기)
    print(i, numbers[i])





# 피타고라스 수 : 피타고라스의 정리(a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍 (a, b, c) 이다
# a < b < c일때, a + b + c = 1000을 만족하는 피타고라스 수 (a, b, c)는 단 하나
# 이 경우, a * b * c는 얼마인가

# -> 요약하면
#  1. a >= 1, b >= 1, c >= 1
#  2. a + b + c = 1000
#  3. a < b < c
#  4. a^2 + b^2 = c^2

for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - a - b

        # a < b < c이여야 하고, 피타고라스 정리를 만족해야 한다.
        if (a < b and b < c) and (a * a + b * b == c * c):
            print(a * b * c)





# Aliasing 

# 1. alias 맞는 경우
x = [2,3,5,7,11]
y = x
y[2] = 4
print(x)
print(y)

# 결과는 x, y 모두 [2,3,4,7,11]..!!
# -> y는 x의 별명alias이라서 같은 값 출력되는 것


# 2. alias 아닌 경우
# 그럼 x는 유지하고 y는 바꾸고 싶을 때-> 리스트 함수사용(리스트 x를 복사한 것//alias 아니다)
x = [2,3,5,7,11]
y = list(x)
y[2] = 4
print(x)
print(y)





# 리스트 안의 데이터 거꾸로 뒤집기**
# (for문 사용해서//새로운 리스트 만들지 말고//reverse, insert, append 함수사용말고)

# sol) 리스트를 가운데기점으로 반으로 나누면 대칭되는 두 인덱스!!의 합은 늘 6이다
# -> 왼쪽 인덱스 + 오른쪽인덱스 = 총 개수 - 1(인덱스니까 1빼는 것)
numbers = [2, 4, 6, 8, 10, 12, 14]

# left, right변수는 인덱스의미!!
for left in range(int(len(numbers)/ 2)):
    right = len(numbers) - left - 1
    
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp


print("뒤집어진 리스트: " + str(numbers))






# 리스트와 문자열은 비슷하다(대괄호 그런 건 말고)//차이: 문자열은 변경 불가
alphabets = "ABCDEFGHIJ"
print(alphabets[0])
print(alphabets[1])
print(alphabets[4])
print(alphabets[-1])


print(len("hello, world"))





# 자리수 합 구하기 문제
# for문을 사용해서 sum_digit(1)부터 sum_digit(1000)까지의 합 구하기

# 자리수 합 리턴
def sum_digit(num):
    # num을 문자열로 형변환시키기(**문자열은 리스트처럼 사용할 수 있어서)
    str2 = str(num)
    sum = 0
    
    for i in str2:	#for문은 인덱스 사용안하니까// for문에서 문자열이렇게 사용하는구나
        sum += int(i)
    return sum	
    

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
sum = 0
for i in range(1, 1001):
    sum += sum_digit(i)
print(sum)





# 주민등록번호 가리기 문제**
# 문자열은 변할 수 없어서 변할 수 있는 리스트로 만들어야

"""
# 내가 푼 방법..
def mask_security_number(security_number):
    num = list(security_number)
    # 문자열을 리스트로

    for i in num:
        if(num[6] == "-"):
            for j in range(10,14):
                num[j] = "*"
       
        else:
            for j in range(9,13):
                num[j] = "*"

    # 리스트를 다시 문자열로
    total_str = ""
    for i in range(len(num)):
        total_str += num[i]

    return  total_str


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
"""


# 모범답안

def mask_security_number(security_number):
    num = list(security_number)
    # 문자열을 리스트로

    # 마지막 네 값을 *로 대체**
    for i in range(len(num) - 4, len(num)):
        num[i] = "*"

    # 리스트를 다시 문자열로
    total_str = ""
    for i in range(len(num)):
        total_str += num[i]

    """
    # 리스트를 다시 문자열로 더 쉬운 방법

    total_str = "".join(num)


    """



    return  total_str


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


"""

# 더 쉬운 방법 wow
def mask_security_number(security_number):
    return security_number[:len(security_number) - 4] + "****"

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

"""






# 팔린드롬(palindrom) 문제 : 거꾸로 읽어도 똑같은 단어
def is_palindrome(word):
    half_count = int(len(word)/2)
    
    return (word[:half_count] == word[len(word)-1:half_count:-1])
    


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))