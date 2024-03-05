# # a='110010101001'
# # print(int(a,2))
# def convert2binary(num):
#     temp = []
#     while True:
#         if num == 1:
#             temp.append(1)
#             break
#         remainder = num % 2
#         num = num // 2
#         temp.append(remainder)
#         if num < 2:
#             temp.append(num)
#             break
#     temp.reverse()
#     result = "".join(map(str, temp))
#     return result
# def solution(s):
#     counts=0
#     # input s = '01110' 입력이 들어왔을 때 일단 제거할 0의 개수를 저장해야겠지
#     iteration=0
#     while s!='1':
#         counts=counts+s.count('0')
#         s=s.replace('0','')
#         lens=len(s)
#         s=convert2binary(lens)
#         iteration=iteration+1
#     answer = []
#     answer.append(iteration)
#     answer.append(counts)
#     return answer
# print(solution("01110"))
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
print(solution("01110"))