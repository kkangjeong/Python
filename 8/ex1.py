# 요약하면) 맨 밑 __init__ 메소드 사용하자!!
# 모든 인스턴스 변수 초기값 설정할 때(항상 해야)
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












# initialize 메소드 : 한 번만 써서 모든 인스턴스 변수 초기값 설정하기 위해 


# 정의되어 있지 않은 인스턴스 변수 쓰려고 하면 오류 나와서 꼭 모든 인스턴스 변수를 정의해야 한다.
# User 인스턴스를 네개 만들고 초기값들을 설정해주려면 아래처럼

class User:
    pass

user1 = User()
user1.name = "Young"
user1.email = "young@codeit.kr"
user1.password = "123456"

user2 = User()
user2.name = "Yoonsoo"
user2.email = "yoonsoo@codeit.kr"
user2.password = "abcdef"

user3 = User()
user3.name = "Taeho"
user3.email = "taeho@codeit.kr"
user3.password = "123abc"

user4 = User()
user4.name = "Lisa"
user4.email = "lisa@codeit.kr"
user4.password = "abc123"


# but, 길어보이고 반복적 -> initialize 메소드 사용




# 이렇게

class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)                  # young@codeit.kr
print(user2.name)                   # Yoonsoo
print(user3.password)               # 123abc
print(user4.email)                  # lisa@codeit.kr






# 항상 초기화 설정해줘야 하니까 위에꺼(initialize 메소드) 말고 __init__ 메소드 사용!

# __init__ 메소드 : 한번에 인스턴스 만들어서! 인스턴스 변수 초기화 설정하도록


class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user1 = User("Young", "young@codeit.kr", "123456")      # 위랑 이게 다른 것

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")

