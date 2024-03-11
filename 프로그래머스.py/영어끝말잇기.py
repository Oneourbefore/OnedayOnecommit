# def solution(n, words):
#     start=words[0][-1]
#     # 첫번쨰 단어의 끝 알파벳 지정
#     words=words[1:]
#     # 두번째 부터 시작
#     # kick , know 
#     selfnum=1
#     firstnum=0
#     for word in words:
#         # 두번째 단어가 들어옴
#         if word in words: 
#         elif start==word[0]:
#         # 첫번쨰 끝과 두번째 처음을 비교함 -> 만약에 같으면 
#         # 첫번째 끝을 두번째 끝으로 대치해줌
#             start=word[-1]
#             selfnum=selfnum+1
#             print(selfnum)
#         else:
#             return [selfnum//n,selfnum%n]
#             break
#     if selfnum==len(words):
#         return [0,0]
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print(solution(3,["tank", "kick", "cnow", "wheel", "land", "dream", "mother", "robot", "tank"]))


def solution(n, words):
    answer = []
    cnt=1
    answer.append(words[0])
    words=words[1:]
    for word in words:
        if word in answer:
            return [1+cnt%n,1+cnt//n]
        
        elif answer[-1][-1]==word[0]:
            answer.append(word)
            cnt=cnt+1
        else:
            return [1+cnt%n,1+cnt//n]
    return [0,0]
print(solution(3,["tank", "cick", "know", "wheel", "land", "dream", "mother", "robot", "tank","korea","able"]))
# 5 번째 