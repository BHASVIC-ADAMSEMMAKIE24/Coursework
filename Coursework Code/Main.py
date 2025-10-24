import random



###########################
#   pointers
##########################
#queue pointers
tail = 0
head = 51





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
#            _USER         _CURRENCY        _CARDS       _RESULT
player1 = [player1User, player1Currency, player1Cards, player1Result]
player2 = [player2User, player2Currency, player2Cards, player2Result]
player3 = [player3User, player3Currency, player3Cards, player3Result]
player4 = [player4User, player4Currency, player4Cards, player4Result]
dealer  = [dealerUser,       dealersPot,  dealerCards,  dealerResult]

players = [player1, player2, player3, player4]

