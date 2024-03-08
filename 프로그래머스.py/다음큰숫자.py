# 1111 8 + 4 + 2 + 1 = 15
# 10111 16 + 4 + 2 + 1 = 23
# 11011 16 + 8 + 2 + 1 = 27
# 11101 16 + 8 + 4 + 1 = 29
# 11110 16 + 8 + 4 + 2 = 30
# 100111 32 + 
# 조합을 사용하여 
def convert2binary(num):
    temp = []

    while True:
        remainder = num % 2
        num = num // 2
        temp.append(remainder)
        
        if num < 2:
            temp.append(num)
            break

    temp.reverse()
    result = "".join(map(str, temp))
    return result

num = 25
binary_num = convert2binary(num)
print(binary_num)