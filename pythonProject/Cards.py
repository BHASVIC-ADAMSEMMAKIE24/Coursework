import random

# This improves code reusability as the values inside the array change instead making a whole new array
# when cards are being delt they will be stored as a queue (FIFO)
# #def bjValues():
# one = 1
# two = 2
# three = 3
# four = 4
# five = 5
# six = 6
# seven = 7
# eight = 8
# nine = 9
# ten = 10
# j = 11
# q = 11
# k = 11
# a = 11


ordered_Deck = [["AcS", "AcH", "AcD", "AcC"]
    , ["02S", "02H", "02D", "02C"]
    , ["03S", "03H", "03D", "03C"]
    , ["04S", "04H", "04D", "04C"]
    , ["05S", "05H", "05D", "05C"]
    , ["06S", "06H", "06D", "06C"]
    , ["07S", "07H", "07D", "07C"]
    , ["08S", "08H", "08D", "08C"]
    , ["09S", "09H", "09D", "09C"]
    , ["10S", "10H", "10D", "10C"]
    , ["JaS", "JaH", "JaD", "JaC"]
    , ["QuS", "QuH", "QuD", "QuC"]
    , ["KiS", "KiH", "KiD", "KiC"]]
# Value
ace = 0
two = 1
three = 2
four = 3
five = 4
six = 5
seven = 6
eight = 7
nine = 8
ten = 9
jack = 10
queen = 11
king = 12
# Suit
spades = 0
hearts = 1
diamond = 2
clubs = 3
#ordered_Deck[value][suit]
#print(ordered_Deck[ace][spades])
standard_Deck = ["AcS", "AcH", "AcD", "AcC"
    , "02S", "02H", "02D", "02C"
    , "03S", "03H", "03D", "03C"
    , "04S", "04H", "04D", "04C"
    , "05S", "05H", "05D", "05C"
    , "06S", "06H", "06D", "06C"
    , "07S", "07H", "07D", "07C"
    , "08S", "08H", "08D", "08C"
    , "09S", "09H", "09D", "09C"
    , "10S", "10H", "10D", "10C"
    , "JaS", "JaH", "JaD", "JaC"
    , "QuS", "QuH", "QuD", "QuC"
    , "KiS", "KiH", "KiD", "KiC"
                 ]
tail = 0
head = 51
player1 = []
player2 = []
player3 = []
player4 = []
dealer = []


#queue pointers

def ShuffleDeck(standard_Deck):
    global shuffled_Deck
    global head
    global tail
    head = 51
    tail = 0
    shuffled_Deck = standard_Deck
    random.shuffle(shuffled_Deck)


def CardIntegration(player, nCards):
    global shuffled_Deck
    global head
    for i in range(nCards):
        card = input("Input card")
        shuffled_Deck.remove(card)
        player.append(card)
    head -= nCards
    return player


def DealCards(player, nCards):
    global shuffled_Deck
    global head
    for i in range(nCards):
        card = shuffled_Deck[head]
        shuffled_Deck.pop(head)
        head -= 1
        player.append(card)
    return player


#gamemode is either poker or blackjack
gamemode = "blackjack"


def CardValue(card, gamemode):
    value = card[0:2]
    if int(value) <= 10:
        value = int(value)
    elif gamemode == "blackjack":
        if value == "Ac":
            value = 11
        else:
            value = 10
    elif gamemode == "poker":
        if value == "Ac":
            value = 14
        elif value == "Ki":
            value = 13
        elif value == "Qu":
            value = 12
        elif value == "Ja":
            value = 11
        else:
            print("card value error")
    else:
        print("gamemode error")

    suit = card[2:]
    return value, suit


#print(standard_Deck[ace][spades])

# print(shuffled_Deck)
# ShuffleDeck(standard_Deck)
# print(shuffled_Deck[0])
#print(str(cards[0][1]) , str(cards[1][0]))

# ShuffleDeck(standard_Deck)
# DealCards(player1,1)
# # DealCards(player2,2)
# # DealCards(player3,2)
# # DealCards(player4,2)
# # print(player1)
# # print(player2)
# # print(player3)
# # print(player4)
# # print(shuffled_Deck)
# # print(len(shuffled_Deck))
# card = player1[0]
# print(card)
# print(card[0:2])
# print(card[2:])

print(CardValue("AcS","poker"))
