# 대표 정렬 3 가지만 : 리스트의 원소들을 특정 순서로 정리하는 것(오름차순, 내림차순, 알파벳 순 etc..)
# 1. Selection Sort(선택 정렬) : 오름차순

def selection_sort(my_list):
    # selection_sort는 새로운 리스트를 만들어서 리턴해주는 것이 아니고, 파라미터로 넘어온 리스트를 변형시켜주는 것
    
   


    # 다시
    for i in range(1, len(my_list)):
        for j in range(0, len(my_list)-1):
            if(int(my_list[j]) <= int(my_list[i])):
                my_list[j] = my_list[j]
            else:
                my_list[j] = my_list[i]
            j += 1
        i += 1
        

some_list = [7,11,6,4,2,8,9]
selection_sort(some_list)
print(some_list)















# 2. Insertion Sort(삽입 정렬)

def insertion_sort(my_list):
    # 코드를 입력하세요.

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)

[1, 2, 3, 4, 6, 11, 12]
















# 3. Merge Sort(합병 정렬)

# 분할 정복(Divide and Conquer) 방식으로 merge_sort 함수 사용하기
# merge_sort는 파라미터로 리스트 하나를 받고, 정렬된 새로운 리스트를 리턴
# merge_sort 함수에서는 재귀(recursion)의 개념을 활용해야 합니다. 

# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)

[1, 2, 3, 4, 6, 11, 12]
