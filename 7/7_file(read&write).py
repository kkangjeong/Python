# 파이썬으로 파일 읽고, 쓰기, 파일의 내용으로 작업하기

# 1
# r : 파일 읽기
in_file = open("C:/Users/user/Desktop/Python/7/file1.txt", "r", encoding='UTF8')

# print(type(in_file))

# 한줄씩 모두 읽기
for line in in_file:
    print(line)

# for문 쓰면 in_file파일의 정보들 리스트와 비슷하게 사용가능

in_file.close()
# 파일 읽고나면 꼭 닫아주기-> 메모리 낭비



# 2
# strip 익히기(맨 앞/맨 뒤 화이트스페이스(띄어쓰기, 엔터, 탭) 없애서 출력)
# print("     abc     def     ".strip())
# print("    \n   abc  def  \n\n   ".strip())


# 1을 \n 없애서 출력하려고
in_file = open("C:/Users/user/Desktop/Python/7/file1.txt", "r", encoding='UTF8')

for line in in_file:
    print(line.strip())

in_file.close()




# 3
# split 익히기(파라미터 값 기준으로 문자열 분리시키고, 분리된 값들이 정리되어 있는 리스트 리턴)
numbers = "1. 2. 3. 4. 5. 6"
print(numbers.split("."))

print(numbers.split(". "))





full_name = "Kang, Joengin"
name_data = full_name.split(", ") 
last_name = name_data[0]
first_name = name_data[1]

print(last_name, first_name)        # 콤마 나열하면 공백 자동 추가 wow
# 출력값 : Kang Joengin




# 파라미터 없으면 -> 디폴트 값 : ""(화이트 스페이스(띄어쓰기, 엔터, 탭)기준으로)
print("1 2 3 4 5 6".split())
# ['1', '2', '3', '4', '5', '6']



some_string = "   abc    def   \n   gh   lmnop   q r \n s  "
print(some_string.split())
# ['abc', 'def', 'gh', 'lmnop', 'q', 'r', 's']


print("   \n   1 \t\n     2     \t\t\n\n   3       4   5 \n 6  \t".split())







# /file1.txt 파일에는 치킨집의 12월 매출이 있다
# :의 왼쪽에는 며칠인지, 그리고 오른쪽에는 그 날의 매출//

# file1.txt를 읽어 들이고, 
# strip과 split을 써서 12월의 치킨 하루 평균 매출을 계산하라
# 만약 한 달이 28일이거나 30일이면 그에 맞게 평균 매출을 구할 수 있도록 코드 짜기

# 내가 푼 방법
in_file = open("C:/Users/user/Desktop/Python/7/file1.txt", 'r', encoding='UTF8')
sum = 0
avg = 0
for i in in_file:
    b = (i.strip()).split("일: ")
    sum += int(b[1])
    
    if(int(b[0])==28):
        avg = sum/int(b[0])
    
    elif(int(b[0]) == 29):
        avg = sum/int(b[0])

    elif(int(b[0]) == 30):
        avg = sum/int(b[0])
    
    elif(int(b[0]) == 31):
        avg = sum/int(b[0])
           
print(avg)

in_file.close()

"""
# 모범 답안
in_file = open("C:/Users/user/Desktop/Python/7/file1.txt", 'r', encoding='UTF8')

sum = 0

line_count = 0

for line in in_file:
    data = line.strip().split(": ") 
    amount = int(data[1])
    sum += amount
    line_count += 1

print(sum/line_count)

in_file.close()
"""









# 파일 쓰기
out_file = open("7/new_file.txt" ,"w")

out_file.write("Hello World\n")
out_file.write("My name is Jeong In Kang")

out_file.close()












# 1. 단어장 만들기

# 영어 단어와 한국어 뜻을 받고 vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리한다
# 프로그램을 끝내려면 q 입력하기

out_file = open("7/vocabulary.txt", "w", encoding='UTF8')


while(1):
    f_input = input("영어 단어를 입력하세요: ")
    if(f_input == "q"):
        break

    f2_input = input("한국어 뜻을 입력하세요: ")

    out_file.write(f_input + ": ")
    out_file.write(f2_input + "\n")
    
out_file.close()





# 2. 만든 단어장으로 퀴즈하기
# vocabulary.txt 파일에 있는 단어 수 달라져도 코드 잘 작동하는 법-> 그냥 하면된다
# for문 끝날 때까지 파일문장 다 읽는 거라서

in_file = open("7/vocabulary.txt", "r", encoding='UTF8')

for word in in_file:
    data = word.strip().split(": ")
    # print(data[1] + ":")
    # 띄어쓰기 안하도록** -> print하지말고 input뒤에서 하는 방법밖에 없구나

    #input이 answer가 아니라ㅋㅋ input할 때 출력문장이라고 생각
    answer = input("%s: "% (data[1]))
    if(data[0] == answer):
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % (data[0]))


in_file.close()
