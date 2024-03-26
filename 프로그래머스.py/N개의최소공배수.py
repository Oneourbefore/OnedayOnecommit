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

def greet_and_select_category():
    # Greet the user and ask for their name
    name = input("1. 이름을 입력하세요: ")
    print(f"반갑습니다 {name}님, 카테고리를 골라주세요.")
    
    # List of categories
    categories = [
        "1. 음악", "2. 영화", "3. 스포츠", "4. 음식", "5. 여행",
        "6. 책", "7. 게임", "8. 패션", "9. 기술", "10. 예술
    # Get the user's choice
    choice = input("원하는 카테고리 번호를 선택하세요: ")
    return choice

# Call the function to run the program
category_choice = greet_and_select_category()
print(f"당신이 선택한 카테고리는 {category_choice}번 입니다.")
