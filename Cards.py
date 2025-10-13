
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

#cards = [[one, two, three, four, five, six, seven, eight, nine, ten, "jack", "queen", "king", "ace"], ["Spades", "Hearts",
 #                                                                                             "Diamonds", "Clubs"]]

standard_Deck =  (["AcS","AcH","AcD","AcC"]
        , ["01S","01H","01D","01C"]
        , ["02S","02H","02D","02C"]
        , ["03S","03H","03D","03C"]
        , ["04S","04H","04D","04C"]
        , ["05S","05H","05D","05C"]
        , ["06S","06H","06D","06C"]
        , ["07S","07H","07D","07C"]
        , ["08S","08H","08D","08C"]
        , ["09S","09H","09D","09C"]
        , ["10S","10H","10D","10C"]
        , ["JaS","JaH","JaD","JaC"]
        , ["QuS","QuH","QuD","QuC"]
        , ["KiS","KiH","KiD","KiC"]
        )
shuffled_Deck = standard_Deck
#queue pointers
start = 0
end = 0

def ShuffleDeck(standard_Deck):
        function = random.seed()
        global shuffled_Deck
        shuffled_Deck = standard_Deck
        shuffled_deck = random.shuffle(shuffled_Deck,function)


def DealCards():
        global shuffled_deck



ace = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
jack = 11
queen = 12
king = 13
spades = 0
hearts = 1
diamond = 2
clubs = 3

print(standard_Deck[ace][spades])



#print(str(cards[0][1]) , str(cards[1][0]))