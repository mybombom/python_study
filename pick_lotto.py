import random

# 1부터 45까지 담겨있는 배열
numbers = list(range(1, 46))

# 숫자 6개 뽑기
lucky_numbers = random.sample(numbers, 6)

print(lucky_numbers)
