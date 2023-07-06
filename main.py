import random

print("추첨해라")

for i in range(5) :
    lotto = random.sample(range(1,45),6)
    print(lotto)

y = input("한번 더 추첨하려면 y를 입력하세요:")

if y == "y" :
    lotto = random.sample(range(1,45),6)
    print(lotto)


