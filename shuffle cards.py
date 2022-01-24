import itertools , random
#Form a deck of cards
deck= list(itertools.product(range(1,14),["Spade","Heart","Dimond","Club"]))
# shuffle the cards
random.shuffle(deck)
#Draw five cards
print("Your combination of card is :")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
