import random

print("추첨해라")

for i in range(5) :
    lotto = random.sample(range(1,45),6)
    print(lotto)

