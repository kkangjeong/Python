# 코멘트
print("hi")
print("hello" + "world")
print('2' + "3")
print(7 % 3)
print(2 ** 3)  #거듭제곱
# +,-,*(나눗셈 아닌) 정수형 소수형 연산은 (소수형 있으면 무조건 소수형이라고 생각)결과가 소수형(나눗셈 예외 밑에)
#나눗셈 예제(정수정수/정수소수/소수소수/소수정수 4가지 모두 소수형)


#문자열(string)
print("강정인")
print('강정인')

print("I'm happy")
print('steve says, "learn cs"')

#문자열 연산 
print("hello" * 3)

#형 변환(type conversion/type casting)
print(int(3.8))
print(int("2") + int("5"))
print(str(2) + str(5))
print("제 나이는 " + str(7) + "살입니다.")



# 답이 8.0 인 이유 : 정수형과 소수형 간의 연산이라서
print(2 ** 3.0)

print("오늘은 " + str(2020) +"년 " + str(2)+"월 " + str(2) + "일 일요일입니다." )

# 위에꺼 (문자열 더하기 정수형) 안되니까 바보
더하기 할 때 같은 타입인지 생각하자*
print("오늘은 " + int(2020.0) +"년" + int(2.0)+"월 " + int(2.0) + "일 일요일입니다." )


#문자열 포맷팅
year = 2016
month = 1
day = 16
day_of_week = "일"

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + day_of_week + "요일입니다.")
#대신에

print("오늘은 %d년 %d월 %d일 %s요일입니다." % (year, month, day, day_of_week))

print("1 나누기 3은 %.4f" % (1.0 / 3))   #답은 0.3333(소수점 넷째자리까지)
print("1 나누기 3은 %d" % (1.0 / 3))   #답은 0


#Boolen
#True , False , and , or, not
# and일 때 모두 true면 T(나머지 3개 F) , or일 때 모두 false면 F(나머지 3개 T)
print(2>1)
print("Hello" == "Hello")

#type 함수 : 타입(자료형) 알고 싶을 때
print(type(1.0))
print(type(True))
print(type(print))


# 자료형( + 알파)
    # 1. floor division : 소수부분 버리고 정수부분만
            print(7 / 4)

            # 요약하면 두 개가 같은 것
            print(int(7 / 4))
            print(7 // 4)

            #주의 : 소수형있으면 결과 소수형
            print(5.0 // 2)
            print(5 // 2.0)
            print(5.0 // 2.0)

    # 2. 반올림(round : 소수형 반올림)
    print(round(3.141592, 4))   # 3.141592를 소수점 4째 자리로 반올림
    print(round(4.34))          # 4.34를 소수점 0번째 자리로 반올림

    #3. 줄바꿈 기호(\n)
    print("안녕하세요\n코드잇입니다\n여러분 모두를\n환영합니다")

