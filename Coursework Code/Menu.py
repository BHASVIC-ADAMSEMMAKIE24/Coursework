
### starting value for new player
player1Currency = 2000
player2Currency = 2000
player3Currency = 2000
player4Currency = 2000

import random
import time
import pygame
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
shuffledDeck =  ["AcS", "AcH", "AcD", "AcC"
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

#queue/shuffleDeck pointers
tail = 0
head = 51
def ShuffleDeck(STANDARDDECK):
    global shuffledDeck
    global head
    global tail
    head = 51
    tail = 0
    shuffledDeck = STANDARDDECK
    random.shuffle(shuffledDeck)
    return shuffledDeck



def CardIntegration(playerCards, nCards):
    global shuffledDeck
    global head
    for i in range(nCards):
        found = False
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
    if nCards > len(shuffledDeck) or nCards < 0:
        print("nCards out of range")
    else:
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
        total += int(CardValue(deck[i], "blackjack")) # adds the cards value on to the current total
    return total

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
                if int(CardTotal(players[i][_CARDS])) > 21:
                    players[i][_RESULT] = "Bust"
                    print(players[i][_RESULT])

            elif choice.lower() == "stand": # here to be edited when implementing the GUI
                print("")
        print(players[i][_USER] , " turn ended")
    print("All player turns have ended")
    return players


def BlackjackResult(players,dealer):
    dealerCardTotal = CardTotal(dealer[_CARDS])
    if dealerCardTotal > 21:
        dealer[_RESULT] = "Bust"
    for i in range(len(players)):
        if players[i][_RESULT] != "Bust":
            if dealer[_RESULT] == "Bust":
                players[i][_RESULT] = "Win"
            else:
                if CardTotal(players[i][_CARDS]) < dealerCardTotal:
                    players[i][_RESULT] = "Loss"
                elif CardTotal(players[i][_CARDS]) == dealerCardTotal:
                    players[i][_RESULT] = "Draw"
                else:
                    players[i][_RESULT] = "Win"
    return players, dealer

def BlackjackRound(players,dealer,isCardIntegration):
    # Reseting variables for start of new round
    dealer[_CARDS] = []
    dealer[_CURRENCY] = [0, 0, 0, 0]
    for i in range(len(players)):
        players[i][_CARDS] = []
    ShuffleDeck(STANDARDDECK)
    BlackjackAnte(players,dealersPot)
    if isCardIntegration:
        for i in range(len(players)):
            CardIntegration(players[i][_CARDS],2)
    elif not isCardIntegration:
        for i in range(len(players)):
            DealCards(players[i][_CARDS],2)
    DealCards(dealer[_CARDS], 2)
    ### Outputting players cards and one dealer card
    print(dealer[_USER] , "Cards:",dealer[_CARDS][0], "???")
    for i in range(len(players)):
        print(players[i][_USER],"Cards: ", players[i][_CARDS])
    BlackjackHitStandCycle(players)
    ### output dealer cards
    print(dealer[_USER], "Cards:",dealer[_CARDS])
    # Dealer hit stand cycle
    if CardTotal(dealer[_CARDS]) < 17:
        DealCards(dealer[_CARDS], 1)
        print(dealer[_USER], "Cards:", dealer[_CARDS])
        while CardTotal(dealer[_CARDS]) < 17:
            DealCards(dealer[_CARDS], 1)
            print(dealer[_USER], "Cards:", dealer[_CARDS])
    BlackjackResult(players, dealer)
    BJWinningsCalculation(players,dealersPot)
    ### Output players result and dealer result
    print(dealer[_USER], "Result:",dealer[_RESULT])
    for i in range(len(players)):
        print(players[i][_USER],"Result: ", players[i][_RESULT])
    ##    print("Fries: ", players[i][_CURRENCY])
    return player1Currency, player2Currency, player3Currency, player4Currency


########################################################################################################################

####################################################
## ############################################## ##
## ###                                        ### ##
## ###              Currency.py               ### ##
## ###                                        ### ##
## ############################################## ##
####################################################

def BJWinningsCalculation(players,dealersPot):
    for i in range (len(players)):
        if players[i][_RESULT] == "Win":
            players[i][_CURRENCY] += int((dealersPot[i]*2))
        elif players[i][_RESULT] == "Draw":
            players[i][_CURRENCY] += int(dealersPot[i])
    return players

def TotalPot(dealersPot):
    total = 0
    for i in range(len(dealersPot)):
        total += dealersPot[i]
    return total

def PKWinningsCalculation(players,dealersPot):
    nWinners = 0
    for i in range(len(players)):
        if players[i][_RESULT] == "Draw" or players[i][_RESULT] == "Win":
            nWinners += 1
    for j in range(len(players)):
        if players[j][_RESULT] == "Draw" or players[j][_RESULT] == "Win":
            players[j][_CURRENCY] += (int(TotalPot(dealersPot)) // nWinners)
    return players


########################################################################################################################

####################################################
## ############################################## ##
## ###                                        ### ##
## ###                Menu.py                 ### ##
## ###                                        ### ##
## ############################################## ##
####################################################
def PlayerSetup():
    global players
    nPlayers = 0
    nPlayers = int(input("Enter number of players 1-4: "))
    while nPlayers < 1 or nPlayers > 4:
        print("nPlayers outside of range.")
        nPlayers = int(input("Enter number of players 1-4: "))
    if nPlayers == 1:
        players = [player1]
    elif nPlayers == 2:
        players = [player1,player2]
    elif nPlayers == 3:
        players = [player1,player2,player3]
    elif nPlayers == 4:
        players = [player1,player2,player3,player4]
    for u in range(len(players)):
        username = input(players[u][_USER] + " Enter your username: ")
        players[u][_USER] = username

def StartBlackjack(players,dealer):
    choice = input("Card Integration?")
    if choice[0:1].lower() == "y":
        isCardIntegration = True
    else:
        isCardIntegration = False
    nRounds = int(input("Enter number of rounds: "))
    for r in range(nRounds):
        BlackjackRound(players,dealer,isCardIntegration)
    return players

def StartPoker(players,dealer):
    choice = input("Card Integration?")
    if choice[0:1].lower() == "y":
        isCardIntegration = True
    else:
        isCardIntegration = False
    nRounds = int(input("Enter number of rounds: "))
    #for i in range(nRounds):

        #PokerRound(players,dealer,isCardIntegration)
    return players

def Rules():
    ##output
    print("Blackjack Rules:\n blahblahblah\n")
    print("Poker Rules:\n blahblahblah\n")
    print("Poker hand rankings:\nRoyal Flush: Ac, Ki, Qu, Ja, and 10, all of the same suit.\nStraight Flush: Any straight of the same suit. For example, JaC, 10C, 09C, 08C, 07C.\nFour of a Kind: Any four cards of the same value, plus another random card. For example, 08C, 08D, 08H, 08S, JaH.\nFull House: Three cards of one value and two cards of another value. For example, JaC, JaH, JaS, 02C, 02D.\nFlush: All cards of the same suit. The value doesnt matter.\nStraight: 5 cards of consecutive value but of different suits.\nThree of a Kind: Any three cards of the same value and two random cards. For example, 05C, 05S, 05H, 03C, JaD\nTwo Pair: Two pairs of cards of equal value and one random card. For example, 08S, 08D, 04C, 04H, JaS.\nPair: One pair of cards of equal value and three random cards. For example, QuD, QuH, 08S, 05C, 03H.\nHigh Card: No cards interact with other cards in any way, so the highest value card.")

def Menu():
    PlayerSetup()
    choice = input("Enter your choice: (blackjack,rules,poker)\n)")
    if choice == "blackjack":
        StartBlackjack(players,dealer)
    elif choice == "rules":
        Rules()
    elif choice == "poker":
        StartPoker(players,dealer)









########################################################################################################################

####################################################
## ############################################## ##
## ###                                        ### ##
## ###                GUI.py                  ### ##
## ###                                        ### ##
## ############################################## ##
####################################################
#initialise the pygame
pygame.init()

# create the screen (width(X),height(Y))
screen = pygame.display.set_mode((1280,1024))


# Title and icon
pygame.display.set_caption('The Cards Collective')
# (32 pixel image from "flaticon.com") #"https://www.flaticon.com/free-icons/french-fries"
icon = pygame.image.load('icon.png')

# Background Image            # https://indonesian-recipes.com/download/2030-version.html
background = pygame.image.load("background.png")

running = True
while running:
    pygame.display.set_icon(icon)
    screen.blit(background, (0, 0))  # This displays the background to the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    pygame.display.update()


######################################################################
## Testing ###########################################################
######################################################################



######################################################################
## Testing ###########################################################
######################################################################
Menu()