# 최단 경로 알고리즘

# 그래프(정점: vertex//변:edge)
# (undirected graph: 페이스북처럼 친구 맺기, 방향성 없는 그래프//directed graph: 인스타처럼 팔로우기능있는, 방향성 있는 그래프)
# (unweighted graph: 변의 크기 개념이 없는 그래프//weighted graph: 변의 크기 개념이 있는 그래프)






# Queue(대기 행렬)
"""
BFS 알고리즘을 구현하기 위해서는 'queue'라는 것을 사용해야 합니다.


Queue는 직역을 하면 '(무엇을 기다리는 사람, 자동차 등의) 줄', 또는 '대기 행렬'입니다.


컴퓨터 프로그래밍에서 queue는 리스트처럼 여러 값을 보관하는데요. Queue에 값을 추가하면 순서대로 대기를 하고, queue에서 값을 빼면 들어간 순서대로 나오게 됩니다.


#deque

파이썬에서 queue를 사용하기 위해서는 'deque (double-ended queue)'라는 것을 사용해야 하는데요. 예시를 통해 알아보겠습니다.



from collections import deque

# 새로운 queue 생성
numbers = deque()

# queue에 값 추가
numbers.append(2)
numbers.append(3)
numbers.append(5)
numbers.append(7)

print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))



출력결과
deque([2, 3, 5, 7])
4
2
deque([3, 5, 7])
3
3
deque([5, 7])
2

"""








# 지하철 최단 경로 찾기
"""
두 지하철역 사이의 최단 거리 경로를 찾는 프로그램을 써보겠습니다. 'BFS(Breadth-First Search)' 알고리즘을 사용하게 될텐데요. 
알고리즘을 구현하기 전에 필요한 것들을 먼저 준비하겠습니다.


# 준비 과정

Station 클래스

지하철역을 표현하는 Station 클래스를 만들어야 합니다. Station 클래스의 구성 요소는 이렇습니다:


(1) 인스턴스 변수 name: 역 이름


(2) 인스턴스 변수 neighbors: 이웃 역들을 담고 있는 리스트. 즉, Station 인스턴스들을 담고 있는 리스트입니다.


(3) 메소드 __init__: 인스턴스 변수들을 초기값으로 설정해줍니다.

def __init__(self, name):
    # 인스턴스 변수들을 초기값으로 설정

(4) 메소드 add_connection: 두 지하철역을 서로 이웃으로 설정해줍니다.


def add_connection(self, another_station):
    # self의 neighbors에 another_station을 담고,
    # another_station의 neighbors에 self를 담는다.





# 파일 읽기


+) station.txt 다운로드 받기



stations.txt 파일의 각 줄에 서울의 각 지하철 호선이 나와있습니다. 
전에 배웠던 방법들을 응용해서 각 역에 해당하는 Station 인스턴스를 만들고, add_connection 메소드를 이용해서 이웃 역들을 연결시켜봅시다.


또, stations라는 사전을 만들어서 key로는 역 이름을, value로는 Station 인스턴스를 넣어 보관합시다. 
그러면 나중에 원하는 역 이름을 사전의 key로 넣어서 인스턴스를 쉽게 찾을 수 있겠죠?



stations = {}
in_file = open('stations.txt')

# 파일의 데이터를 정리하여 각 역에 해당하는 Station 인스턴스를 만들고,
# add_connection 메소드로 이웃 역들을 연결시킨다.
#
# 후에 각 역을 쉽게 찾아서 쓸 수 있도록 stations 사전의 
# key로 역 이름을 넣고, value로 해당 Station 인스턴스를 넣는다.

in_file.close()





# 테스트
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)



# BFS 알고리즘

파라미터로 시작점 start와 목표 지점 goal을 파라미터로 받고 최단 거리 경로를 리턴하는 bfs 함수를 쓰겠습니다. 
start와 goal은 Station 인스턴스이고, 리턴값은 Station 인스턴스들이 담긴 리스트입니다.


다음은 BFS 알고리즘의 pseudocode(가짜 코드)입니다.


def bfs(start, goal):
    # 변수 정의
    previous 사전 생성
    queue 생성
    current = None

    # 초기 설정
    start의 previous를 None로 설정
    queue에 start 추가

    아직 보지 않은 역이 있고, 도착역을 찾지 않았을 경우 반복:
        queue의 앞에 있는 역 빼서 current에 지정

        current의 neighbor를 순서대로 본다:
            neighbor가 아직 안 본 역이면:
                queue에 추가한다
                previous 사전에 추가한다

    만약 current가 goal이면:
        경로를 만들어서 리턴

    current가 goal이 아니면 None을 리턴



+) 4 인강듣기

Pseudocode와 영상을 보고 알고리즘이 왜 올바른 답을 내는지 생각해보세요. 
시작점 start에서부터 거리가 1인 정점들을 모두 보고, 거리가 2인 정점들을 모두 보고... 
이런식으로 하다가 goal을 찾으면 당연히 최단거리가 맞겠죠?





# 템플릿

from collections import deque

# 지하철역 클래스
class Station:
    # 코드를 입력하세요.


# Breadth-First Search 알고리즘
def bfs(start, goal):
    # 코드를 입력하세요.


# 파일 읽기
stations = {}
in_file = open('stations.txt')

# 코드를 입력하세요

in_file.close()


# 테스트
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)





출력결과

잠원
신사
압구정
옥수
금호
약수
버티고개
한강진
이태원





