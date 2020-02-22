# 맞팔해요

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트


    # 팔로우 : self의 following_list에 another_user를 추가하고, another_user의 followers_list에 self를 추가하기**
    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)
        

    # 몇명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)
        

    # 팔로워가 몇명인지 리턴
    def num_followers(self):
        return len(self.followers_list)
        
        

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")



# 테스트
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())





# 출력결과
# Young 2 2
# Yoonsoo 1 3
# Taeho 2 0
# Lisa 1 1