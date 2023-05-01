import random

n = int(input('숫자를 선택하세요'))

for i in range(n):
    numbers = random.sample(range(1, 46), 6)
    print(numbers)

