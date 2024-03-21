def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_array(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    return result