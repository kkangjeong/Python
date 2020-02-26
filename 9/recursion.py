# 재귀함수 : 자기 자신을 호출하는 함수(base case랑 recursive case가 있어야)

# 1
# 정수 n부터 1까지 출력하기

def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)

countdown(4)







# 2
# 1 ~ n 까지 곱 구하기
# 반복문 써서 풀 수 있는 문제는 재귀함수를 써서 풀 수 있고, 그 반대도 가능

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(4))




# 3 
# 삼각수 구하기 : 정삼각형 모양 이루는 점의 개수//n번째 삼각수 : 자연수1부터 n까지 합이구나//n은 1이상 자연수라고 가정

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:
        return 1
    return n + triangle_number(n - 1)


for i in range(1, 11):
    print(triangle_number(i))




# 4
# 피보나치 수열 : 첫째, 둘째 항이 1이고, 셋째 항부터는 바로 앞의 두항의 합으로 정의된 수열
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ..


# n번째 피보나치 수를 리턴
def fib(n):
    if n == 2 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)
     

for i in range(1, 11):
    print(fib(i))




# 5
# 자릿수 합 구하기

# n의 각 자릿수의 합을 리턴

# 22541이면 2 + 2541로 한 것
def sum_digits(n):
    su = str(n)
    if len(su) == 1:
        return int(su[0])
    return int(su[0]) + sum_digits(int(su[1:]))


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))



# 22541이면 2254 + 1로 한 것(내가 생각한 건데 위가 더 코드 짧네//숫자 일의 자리부터 시작되니까 이렇게 생각한 것)
def sum_digits(n):
    su = str(n)
    if len(su) == 1:
        return int(su[0])
    return sum_digits(int(su[0:len(su)-1])) + int(su[len(su) - 1])


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))




# 6
# 리스트 뒤집기

# some_list[:1]는 리스트 형태로 나오지만
# some_list[0]은 원소 형태로 나오는구나 wow    

# 답 여기에





some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)


# 안되지만 여기까지 생각함

def flip(some_list):
    if len(some_list) == 1:
        return some_list
    return some_list[len(some_list)-1:] + flip(some_list[len(some_list)-2::-1])


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)






# insert로 하는 방법 해보기??????????????????????

    return flip(some_list[0:len(some_list)-1]).insert(0, some_list[len(some_list)-1])
    



# 7
# 하노이의 탑 : 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것

# 한 번에 하나의 원판만 옮길 수 있다//큰 원판이 작은 원판 위에 있어서는 안 된다
# 가장 작은 원판의 번호는 1번이고 가장 큰 원판의 번호는 num_disks번
# 그리고 왼쪽 기둥이 1번, 가운데 기둥이 2번, 오른쪽 기둥이 3번


def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        return move_disk(1,1,3)
    hanoi(num_disks-1, 1, 2)
    move_disk(num_disks, 1, 3)
    return hanoi(num_disks-1, 2, 3)
    

hanoi(3, 1, 3)


# 즉) 원판이 n개 있었을 때

# 1 기둥에 있는 n-1 번째 원판을 2 기둥으로 이동한다.
# 1 기둥에 있는 n 번째 원판을 3 기둥으로 이동한다.
# 2 기둥에 있는 n-1 번째 원판을 3 기둥으로 이동한다.





# 원판 1개인 경우
# hanoi(1, 1, 3) #1번 원판을 1번 기둥에서 3번 기둥으로 이동


# 원판 2개인 경우
# hanoi(2, 1, 3)

# 1번 원판을 1번 기둥에서 2번 기둥으로 이동
# 2번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 3번 기둥으로 이동


# 원판 3개인 경우
# hanoi(3, 1, 3)

# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 2번 원판을 1번 기둥에서 2번 기둥으로 이동
# 1번 원판을 3번 기둥에서 2번 기둥으로 이동
# 3번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 1번 기둥으로 이동
# 2번 원판을 2번 기둥에서 3번 기둥으로 이동
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
