import random



########################################################################################################################

####################################################
## ############################################## ##
## ###                                        ### ##
## ###               Cards.py                 ### ##
## ###                                        ### ##
## ############################################## ##
####################################################

        #Suits:   Spades Hearts Diamonds Clubs
        #Index:     [0]    [1]    [2]    [3]     Index Value
ORDEREDDECK =   [["AcS", "AcH", "AcD", "AcC"]  # [0]   Ace
                , ["02S", "02H", "02D", "02C"]  # [1]   Two
                , ["03S", "03H", "03D", "03C"]  # [2]   Three
                , ["04S", "04H", "04D", "04C"]  # [3]   Four
                , ["05S", "05H", "05D", "05C"]  # [4]   Five
                , ["06S", "06H", "06D", "06C"]  # [5]   Six
                , ["07S", "07H", "07D", "07C"]  # [6]   Seven
                , ["08S", "08H", "08D", "08C"]  # [7]   Eight
                , ["09S", "09H", "09D", "09C"]  # [8]   Nine
                , ["10S", "10H", "10D", "10C"]  # [9]   Ten
                , ["JaS", "JaH", "JaD", "JaC"]  # [10]  Jack
                , ["QuS", "QuH", "QuD", "QuC"]  # [11]  Queen
                , ["KiS", "KiH", "KiD", "KiC"]] # [12]  King

#ordered_Deck[value][suit]
#print(ordered_Deck[ace][spades])
STANDARDDECK =  ["AcS", "AcH", "AcD", "AcC"
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







# _USER
dealerUser = "Dealer"
player1User = "Player 1"
player2User = "Player 2"
player3User = "Player 3"
player4User = "Player 4"
# _CURRENCY
dealersPot = [0,0,0,0]
player1Currency = 2000
player2Currency = 2000
player3Currency = 2000
player4Currency = 2000
# _CARDS
dealerCards = []
player1Cards = []
player2Cards = []
player3Cards = []
player4Cards = []
# _RESULT
dealerResult = ""
player1Result = ""
player2Result = ""
player3Result = ""
player4Result = ""

# player constants
_USER = 0
_CURRENCY = 1
_CARDS = 2
_RESULT = 3
#            _USER         _CURRENCY        _CARDS       _RESULT
player1 = [player1User, player1Currency, player1Cards, player1Result]
player2 = [player2User, player2Currency, player2Cards, player2Result]
player3 = [player3User, player3Currency, player3Cards, player3Result]
player4 = [player4User, player4Currency, player4Cards, player4Result]
dealer  = [dealerUser,       dealersPot,  dealerCards,  dealerResult]

players = [player1, player2, player3, player4]

def ShuffleDeck(STANDARDDECK):
    global shuffledDeck
    global head
    global tail
    head = 51
    tail = 0
    shuffledDeck = STANDARDDECK
    random.shuffle(shuffledDeck)



def CardIntegration(playerCards, nCards):
    global shuffledDeck
    global head
    found = False
    for i in range(nCards):
        while not found:
            card = str(input("Input card: "))
            if shuffledDeck.count(card) == 1:
                found = True
            else:
                print("Card does not exist in deck")
        shuffledDeck.remove(card)
        playerCards.append(card)
    head -= nCards
    return playerCards


def DealCards(playerCards, nCards):
    global shuffledDeck
    global head
    for i in range(nCards):
        card = shuffledDeck[head]
        shuffledDeck.pop(head)
        head -= 1
        playerCards.append(card)
    return playerCards


#gamemode is either poker or blackjack
gamemode = "blackjack"

def CardValue(card, gamemode):
    value = card[0:2]
    if gamemode == "blackjack":
        if value == "Ac":
            value = 11
        elif value in ["Ki", "Qu", "Ja"]:
            value = 10
        else:
            value = int(value)
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
            value = int(value)
    else:
        print("gamemode error")

    return value

def CardTotal(deck):
    total = 0 # initialises total
    for i in range(len(deck)): # cycles through each card in the players deck
        total += CardValue(deck[i], "blackjack") # adds the cards value on to the current total
    return total

CardTotal(players[0][_CARDS])
def CardSuit(card):
    suit = card[2:]
    return suit

########################################################################################################################

####################################################
## ############################################## ##
## ###                                        ### ##
## ###             Blackjack.py               ### ##
## ###                                        ### ##
## ############################################## ##
####################################################


### Resetting Variables
dealerCards = []
player1Cards = []
player2Cards = []
player3Cards = []
player4Cards = []


def BlackjackAnte(players,dealersPot):
    for i in range(len(players)): # loops through each player
        print("Your currency: " + str(players[i][_CURRENCY])) # displays currency to user
        dealersPot[i] = int(input("Enter ante bet: ")) # takes integer value of players ante bet
        while players[i][_CURRENCY] < dealersPot[i] or dealersPot[i] < 0:
            print("Invalid bet") # while loop prevents negative bets and bets above the players available currency
            dealersPot[i] = int(input("Enter ante bet: ")) # forced to enter a valid bet
        players[i][_CURRENCY] -= dealersPot[i] # subtracts ante from players currency after bet is validated
    return players, dealersPot

# test
# for i in range(len(players)): # displaying each players currency before ante changes
#     print(players[i][_CURRENCY])
# BlackjackAnte(players,dealersPot) # calling upon subroutine
# for i in range(len(players)): # displaying each players currency after ante changes
#     print(players[i][_CURRENCY])

def BlackjackHitStandCycle(players):
    for i in range(len(players)):  # loops through each player
        print(players[i][_USER], " turn") # outputs which players current turn
        choice = "hit"
        while players[i][_RESULT] != "Bust" and choice.lower() == "hit":
            choice = input("Hit or Stand: ")
            if choice.lower() == "hit":
                DealCards(players[i][_CARDS],1) # deals the player a card
                print(players[i][_CARDS])   # outputs the new deck
                if int(CardTotal(players[i][_CARDS], "blackjack")) > 21:
                    players[i][_RESULT] = "Bust"
                    print(players[i][_RESULT])

            elif choice.lower() == "stand": # here to be edited when implementing the GUI
                print("")
        print(players[i][_USER] , " turn ended")
    print("All player turns have ended")
    return players








