"""
# dictionary : 딕셔너리(사전)
# 순서 없는 key - value 쌍의 집합

dict1 = {}

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)
# {2: 4, 3: 9, 5: 25}
# 리스트와 달리 딕셔너리는 순서 x

print(dict1[3])
# 9





# 리스트와 달리 딕셔너리는 키(리스트의 인덱스)를 정수말고도 문자열로 가능

family = {}
family['mom'] = "grace"
family['dad'] = "chris"
family['son'] = 'young'
family['daughter'] = 'kay'

print(family)
print(family['dad'])







# family 딕셔너리의 key 모두 받아오기 : keys 메소드 사용
print(family.keys())


# family 딕셔너리에 어떤 key들 있는지 확인하기
print('son' in family.keys())
print('uncle' in family.keys())


#  family 딕셔너리의 key들 리스트로 쓰기 : list 함수로 형 변환
family_keys = list(family.keys())
print(family_keys)








# family 딕셔너리의 value 모두 받아오기 : values 메소드 사용
print(family.values())


# family 딕셔너리에 어떤 value가 있는지 확인하기
print('grace' in family.values())
print('yoonsoo' in family.values())


# family 딕셔너리의 value들 리스트로 쓰기 : list 함수로 형 변환
family_values = list(family.values())
print(family_values)






"""










# 저번 단어장 발전시키기
# 저번 단어장 퀴즈는 순서가 같았지만 
# 이번에는 randint 함수와 사전(dictionary) 이용해서 
# vocabulary.txt의 단어들 랜덤한 순서로 테스트하는 프로그램을 만들기
# 알파벳 q를 입력할 때까지


from random import randint

in_file = open("7_2/vocabulary.txt", "r", encoding='UTF8')

# 딕셔너리 만든 후 -> 랜덤으로 출력
dict1 = {}
for line in in_file:
    dict1_key_value = line.strip().split(": ")
    dict1[dict1_key_value[1]] = dict1_key_value[0]

while(1):
    list_keys = list(dict1.keys())
    a = randint(0, len(list_keys)- 1)  

    list_values = list(dict1.values())

    answer = input("%s: " % (list_keys[a]))


    # if랑 elif 관계 주의 : if문 참이면 첫번째elif문 참거짓 판단 x //if문 거짓이면 첫번째elif문 참거짓 판단 o(이 내용은 당연)
    #                      첫번째elif 참이면 두번째elif 판단 x // 첫번째elif 거짓이면 두번째elif 판단 o (wow)
    # 그래서 if/else   if로 함  //근데 두그룹의 순서도 주의해야 wow

    if(answer == "q"):
            break


    if((list_values[a]) == answer):
        print("맞았습니다!")

    else:
        print("틀렸습니다. 정답은 %s입니다." % (list_values[a]))




in_file.close()