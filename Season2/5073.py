def triangle_type(a, b, c):
    # 삼각형의 조건을 확인
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    # Equilateral: 세 변의 길이가 모두 같은 경우
    elif a == b == c:
        return "Equilateral"
    # Isosceles: 두 변의 길이만 같은 경우
    elif a == b or b == c or a == c:
        return "Isosceles"
    # Scalene: 세 변의 길이가 모두 다른 경우
    else:
        return "Scalene"

# 입력을 받고 결과를 출력하는 부분
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print(triangle_type(a, b, c))
