# 자기소개 

# 1. User 클래스에 introduce와 introduce_twice 메소드 코딩


# sns의 유저
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일출력하기)
    def introduce(self):
        print("My name is %s" % (self.name))
        print("My email address is %s" % (self.email))

    # 자기 소개 두번(print 쓰지 말고)
    def introduce_twice(self):
        self.introduce() 
        self.introduce()            # wow    User.introduce_twice(user1)와 같다// user1 = self라서//user1.introduce()는 self.introduce()와 같다
            
        

# 테스트
user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
user1.introduce_twice()     # wow    User.introduce_twice(user1)와 같다// user1 = self라서//user1.introduce()는 self.introduce()와 같다