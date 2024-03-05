def convert2binary(num):
    temp = []
    while True:
        if num == 1:
            temp.append(1)
            break
        remainder = num % 2
        num = num // 2
        temp.append(remainder)
        if num < 2:
            temp.append(num)
            break
    temp.reverse()
    result = "".join(map(str, temp))
    return result
print(convert2binary(2))