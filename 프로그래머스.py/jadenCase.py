def solution(s):
    list_main = s.split()
    for i in range(len(list_main)):
        if list_main[i][0].isalpha():
            list_main[i] = list_main[i].lower()
            list_main[i] = list_main[i][0].upper() + list_main[i][1:]
    answer = ' '.join(list_main)
    return answer

print(solution("eople3 unFollowed me"))