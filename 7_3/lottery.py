# 로또 시뮬레이션 프로그램 만들기

# lottery_driver.py를 실행하면 lotto 모듈에 있는 함수들 사용해서 로또 100장 시뮬레이션 후, lottery.html 파일 만들어주도록 
# 웹 브라우저로 html 파일을 열면 시뮬레이트 되도록

# 참가자는 한 번 할 때마다 1과 45 사이 서로 다른 번호 여섯개 뽑는다
# 당첨번호는 여섯개와 보너스번호 하나
# 당첨액수는 5 경우
# 내가 뽑은 번호 6개와 일반 번호 6개 모두 일치 (10억원)
# 내가 뽑은 번호 5개와 일반 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만원)
# 내가 뽑은 번호 5개와 일반 번호 5개 일치 (100만원)
# 내가 뽑은 번호 4개와 일반 번호 4개 일치 (5만원)
# 내가 뽑은 번호 3개와 일반 번호 3개 일치 (5천원)

# lottery_driver.py를 실행하면 lottery 모듈에 있는 함수들을 사용하여 로또 100장 시뮬레이션을 한 후, lottery.html 파일 만든다.
# 웹 브라우저로 html 파일을 열면 예쁘게 시뮬레이션의 결과 나온다.



from random import randint

# 무작위로 오름차순된 1 - 45 사이의 서로 다른 숫자 여섯개 뽑기


def generate_numbers():
    list1 = []
    new_list1 = []
    
    while(1):
        numbers = randint(1, 45)
        list1.append(numbers)
        if(len(set(list1)) != 6):
            continue
        else:
            break

    new_list1 = sorted(list1)

    return new_list1

     
    





# generate_numbers 함수 이용해서 정렬된 6개에 보너스번호 더한 리스트 리턴
# 일곱개 번호 서로 달라야하고, 첫 여섯개만 정렬하기


def draw_winning_numbers():
    list1 = generate_numbers()
    a = randint(1, 45)
    list1.append(a)

    while(1):
        if(len(set(list1)) == 6):
            continue
        else:
            return list1
            break


    # 관련없지만 set은 list순서 유지x

    





# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0

    for j in range(0, len(list1)):
        for i in range(0, len(list2)):
            if(list1[j] == list2[i]):
                count += 1
            else:
                count += 0
            i += 1
        j += 1
    return count


    




# 로또 등수 확인하기
# 참가자 번호 6개 있는 리스트 numbers와 당첨 여섯개와 보너스 한 개 있는 리스트 winning_numbers받아서
# 당첨 금액 리턴

def check(numbers, winning_numbers):
    

    if(count_matching_numbers(numbers, winning_numbers[:6]) == 6):
        reward = 100000000
        
    elif(count_matching_numbers(numbers, winning_numbers[:6]) == 5):
        reward = 1000000
        
    elif(count_matching_numbers(numbers, winning_numbers[:6]) == 4):
        reward = 50000
        
    elif(count_matching_numbers(numbers, winning_numbers[:6]) == 3):
        reward = 5000
        
    elif(count_matching_numbers(numbers, winning_numbers[:6]) == 5) and (count_matching_numbers(numbers, winning_numbers[6]) == 1):
        reward = 50000000
        
    return reward
    
    
    