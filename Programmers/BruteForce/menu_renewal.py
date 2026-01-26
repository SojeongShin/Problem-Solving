from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    list_ = []
    
    for order in orders:
        order = sorted(order)  # 조합 통일을 위해 정렬
        for i in range(2, len(order)+1):
            for com in combinations(order, i):
                list_.append(com)

    list_counter = Counter(list_)
    
    # 길이별로 "최대 빈도 조합들"을 담을 리스트
    best_menu = [[] for _ in range(max(course)+1)]
    course_list = [0] * (max(course)+1)

    for key in list_counter.keys():
        for cou in course:
            if len(key) == cou and list_counter[key] >= 2:   # 2회 이상만
                if list_counter[key] > course_list[cou]:
                    course_list[cou] = list_counter[key]
                    best_menu[cou] = [key]                    # 교체(새로 시작)
                elif list_counter[key] == course_list[cou]:
                    best_menu[cou].append(key)                # 동률 추가

    # answer 구성(코스 길이들만)
    for cou in course:
        for comb in best_menu[cou]:
            answer.append(''.join(comb))

    return sorted(answer)
