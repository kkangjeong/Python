# 함수
#1
def hello():
    print("hello world")
#들여쓰기 주의(들여쓰기로 구분)
hello()

def hello(name):
    print("hello %s" % (name))

hello("유재석")


#optional parameter : 마지막 파라미터 쓰지 않으면 기본값 갖는//optional parameter는 마지막에 있어야
def myself(name, age, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)

myself("코드잇", 1)            # 기본값이 설정된 파라미터를 바꾸지 않을 때
myself("코드잇", 1, "미국")     # 기본값이 설정된 파라미터를 바꾸었을 때


#2
def sum2(a,b):
    print(a+b)

sum2(2,4)


def f(x):
    print("f 시작")
    return x+1
    print("f 끝")   #리턴 했으니 이건 dead code네

def g(x):
    print("g 시작")
    return x*x-1
    print("g 끝")

print(f(2))         #(밑이랑 헷갈리지 말 것이) print를 해서!! 리턴값이 출력되는 것
print(g(3))
print(f(2)+g(3))



#return 과 print 차이
def print_square(x):
    print(x*x)

def get_square(x):
    return x*x

print_square(3)  # 9 출력
get_square(3)    # 아무것도 안뜬다-> print를 한 적이 없어서 get_square(3) 값은 9이긴 하지//출력만 안되는 것

print(print_square(3))   # 9출력하고// 다음 줄에 none 출력(print_square(3)의 리턴이 없어서 (파이썬에서는 리턴 없으면 none출력//없으니까))
print(get_square(3))      # 이 때 9출력



# global변수와 local변수
"""
#1
def x_is_one():
     x = 1

x_is_one()
print(x)
# x가 지역변수라 오류메시지
"""

#2
def x_is_one():
    global x    #로컬 아니고 글로벌이다(글로벌은 자주 바꾸지 말아야)
    x = 1

x = 5
x_is_one()
print(x)

#답은 1이다

#3
def multiply_by_three():
    y = 2
    y = y * 3

y = 2
multiply_by_three()
print(y)

#답은 2이다



#상수는 대문자가 굿//global변수 가장 좋은 예가 상수//상수: 프로그램 내내 바뀌지 않는 값
#파이썬에서는 상수바꿔도 오류 안나지만 상수(PI) 바꾸지 않는 게 약속//바꾸려면 변수(radius)를 썼겠지
PI = 3.14

def calculate_area(r):
    return PI * r * r

radius = 6
print("반지름이 %f면 원 넓이는 %f" %(radius, calculate_area(radius)))

radius = 12
print("반지름이 %f면 원 넓이는 %f" %(radius, calculate_area(radius)))

