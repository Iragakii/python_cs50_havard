
import random 
#50 %
coin = random.choice(["heads","tails"])
#10 %
number = random.randint(1,10)
#swap location
cards = ["jack","queen","king"]
card = random.shuffle(cards)
for card in cards:
    print(card)

print(number)
print(coin)