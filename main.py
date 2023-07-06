import random

print("로또 번호 5개 추첨하겠습니다!")

for i in range(5) :
    lotto = random.sample(range(1,45),6)
    print(lotto)

