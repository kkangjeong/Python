# class : 내가 자료형을 만들어 쓰는 것(문자열 하나로도, 리스트 하나로도 표현할 수 없을 때)

class User:
    pass
    # 아예 비워놓으면 오류떠서 다른 내용 쓰지 않겠다는 명령어

user1 = User()
user2 = User()

print(type(user1))
#  출력결과  :  <class '__main__.User'>
#   __main__  : 실행 파일 이름
#    .User : 클래스 이름






# 인스턴스
class User:
    pass

user1 = User()
user2 = User()
print(user1 == user2)

# false 나온다 ->  (list aliasing 개념 생각해보면)두 개는 다른 인스턴스(=값)이다



"""
        list aliasing 개념
        x = [2, 3, 5, 7]
        y == x
        y[2] = 4
        print(x == y)
        # true 이다


        x = [2, 3, 5, 7]
        y = [2, 3, 5, 7]
        y[2] = 4
        print(x == y)
        # false 이다
"""



class User:
    pass

user1 = User()
user2 = user1
print(user1 == user2)

# true 이다









# 인스턴스 변수 : 처음부터 초기값 설정 이렇게 해야
class User:
    pass

user1 = User()
user2 = User()

user1.name = "Kang"                         # 인스턴스 변수
user1.email = "wjddls0626@naver.com"
user1.password = "123456"

print(user1.name, user1.email, user1.password)








# 메소드 : 클래스 내에 정의된 함수(변수 뿐만 아니라)

class User:
    def say_my_name(self):                                  # self 쓰는 게 커뮤니티 약속
        print("My name is " + self.name)

user1 = User()
user2 = User()

user1.name = "Kang"                        
user1.email = "wjddls0626@naver.com"
user1.password = "123456"

user2.name = "JeongIn"                        
user2.email = "wjddls5212@gmail.com"
user2.password = "654321"


User.say_my_name(user1)

# 바로 윗줄을 파이썬에서는 이렇게도 가능
user1.say_my_name()







# 파라미터가 여러개인 경우
class User:
    def introduce(self, n):
        for i in range(n):
            print("%s is %d years old." % (self.name, self.age))


# 이 두 줄은 같음
User.introduce(user1, 3)
user1.introduce(3)

# 이 두 줄은 같음
User.introduce(user2, 2)
user2.introduce(2)





# ex1요약하면)  모든 인스턴스 변수 초기값 설정할 때(항상 해야) __init__ 메소드 사용하자!!
# 이렇게
class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user1 = User("Young", "young@codeit.kr", "123456")     

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")