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


# family 딕셔너리에 어떤 key 있는지 확인하기
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

















# 저번 단어장 발전시키기
# 저번 단어장 퀴즈는 순서가 같았지만 
# 이번에는 randint 함수와 사전(dictionary) 이용해서 vocabulary.txt의 단어들 랜덤한 순서로 테스트하는 프로그램을 만들기

