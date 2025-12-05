import random
import time
import pygame
from pygame import mixer

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
def ResetRound():
    # # _USER
    #  # (None)
    # # _CURRENCY
    # global dealersPot
    # dealersPot = [0,0,0,0]
    # # _CARDS
    # global dealerCards
    # global player1Cards
    # global player2Cards
    # global player3Cards
    # global player4Cards
    # dealerCards = []
    # player1Cards = []
    # player2Cards = []
    # player3Cards = []
    # player4Cards = []
    # # _RESULT
    # global dealerResult
    # global player1Result
    # global player2Result
    # global player3Result
    # global player4Result
    # dealerResult = ""
    # player1Result = ""
    # player2Result = ""
    # player3Result = ""
    # player4Result = ""
    global dealer
    global dealersPot
    global players
    for i in range(len(players)):
        players[i][_CARDS] = []
        players[i][_RESULT] = ""
    dealer[_CARDS] = []
    dealer[_RESULT] = ""
    dealersPot = [0,0,0,0]
    dealer[_CURRENCY] = [0,0,0,0]




    #return dealersPot, dealerCards, player1Cards, player2Cards, player3Cards, player4Cards, dealerResult, player1Result, player2Result, player3Result, player4Result

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

def ShuffleDeck(STANDARDDECK):
    global shuffledDeck
    shuffledDeck = STANDARDDECK
    random.shuffle(shuffledDeck)




def CardIntegration(playerCards, nCards):
    global shuffledDeck
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
    return playerCards


def DealCards(playerCards, nCards):
    global shuffledDeck
    if nCards > len(shuffledDeck) or nCards < 0:
        print("nCards out of range")
    else:
        for i in range(nCards):
            head = len(shuffledDeck)
            card = shuffledDeck[head-1]
            shuffledDeck.pop(head-1)
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
        ResetRound()
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

# Background Music   # ES_Silver over Sirmione - Wendy Marcini   # https://www.epidemicsound.com/music/tracks/db2394b6-2af0-430c-b72c-3c5df6ce4c59/
mixer.music.load("background-music.wav")
mixer.music.play(-1) ## infinite

# ==== Sound effects ====
shuffle_effect = mixer.Sound("shuffle-sound.wav")   ## loads sound effects
deal_effect = mixer.Sound("card-sound.wav") # plays every time a card is delt
stand_effect = mixer.Sound("stand-sound.wav") # plays when a player stands
click_effect = mixer.Sound("click-sound.wav") # plays when a player clicks a button
## sound_effect.play() to play sound                     ##    plays loaded audio
# ===================== MENU GUI HELPERS (FUNCTION-BASED, NO CLASSES) =====================

# Fonts for GUI
FONT = pygame.font.SysFont(None, 32)
LARGE_FONT = pygame.font.SysFont(None, 72)

# State names
STATE_MENU      = "menu"
STATE_BLACKJACK = "blackjack"
STATE_RULES     = "rules"

# Indexes for menu option list structure
# menu_option = [rect, text, clicked_flag]
_OPT_RECT    = 0
_OPT_TEXT    = 1
_OPT_CLICKED = 2


def load_menu_images():
    """
    Loads stack-of-cards and singular-card images.
    If files are missing, returns None in their place.
    """
    stack_img = None
    single_card_img = None
    try:
        stack_img = pygame.image.load("stack-of-cards.png").convert_alpha()
    except Exception:
        stack_img = None
    try:
        single_card_img = pygame.image.load("singular-card.png").convert_alpha()
    except Exception:
        single_card_img = None
    return stack_img, single_card_img


stack_of_cards_img, singular_card_img = load_menu_images()

# ===================== BLACKJACK GUI STATE & HELPERS (LIST-BASED) =====================

# Phases inside STATE_BLACKJACK
BJ_PHASE_SELECT_PLAYERS = 0   # ask: how many players?
BJ_PHASE_ANTE           = 1   # ante slider
BJ_PHASE_TABLE          = 2   # table with cards + hit/stand

bj_phase = BJ_PHASE_SELECT_PLAYERS

# Slider state for ante (one slider, same ante for all players for now)
bj_slider_min_value = 0
bj_slider_max_value = 0
bj_slider_value     = 0
bj_slider_dragging  = False

# Slider geometry
bj_slider_track_rect = pygame.Rect(400, 380, 480, 8)   # bar
bj_slider_knob_rect  = pygame.Rect(400, 370, 20, 28)   # knob (x updated based on value)

# Hit area (stack-of-cards) on blackjack table
BJ_HIT_W = 140
BJ_HIT_H = 140
BJ_HIT_X = 190
BJ_HIT_Y = 100
bj_hit_rect     = pygame.Rect(BJ_HIT_X, BJ_HIT_Y, BJ_HIT_W, BJ_HIT_H)
bj_hit_clicked  = False  # debounce

# Small card back image for drawing cards (uses singular-card.png)
card_back_small = None
if singular_card_img is not None:
    card_back_small = pygame.transform.smoothscale(singular_card_img, (80, 120))


def gui_set_n_players(n):
    """
    GUI version of 'how many players' – sets the global 'players' list.
    (Usernames stay as default for now.)
    """
    global players
    if n == 1:
        players = [player1]
    elif n == 2:
        players = [player1, player2]
    elif n == 3:
        players = [player1, player2, player3]
    elif n == 4:
        players = [player1, player2, player3, player4]
    else:
        players = [player1]


def gui_reset_round_for_blackjack():
    """
    Wrapper to start a fresh GUI round:
    - uses your ResetRound()
    - also resets ante slider values
    """
    global bj_slider_min_value, bj_slider_max_value, bj_slider_value
    ResetRound()
    # after players are set, ante max is min of their currency
    if len(players) > 0:
        bj_slider_min_value = 0
        bj_slider_max_value = min([p[_CURRENCY] for p in players])
    else:
        bj_slider_min_value = 0
        bj_slider_max_value = 0
    bj_slider_value = 0
    # reset knob to left
    bj_slider_knob_rect.x = bj_slider_track_rect.left


def slider_value_to_knob_x():
    """
    Updates bj_slider_knob_rect.x based on bj_slider_value.
    """
    if bj_slider_max_value == bj_slider_min_value:
        bj_slider_knob_rect.centerx = bj_slider_track_rect.left
        return
    frac = (bj_slider_value - bj_slider_min_value) / float(bj_slider_max_value - bj_slider_min_value)
    frac = max(0.0, min(1.0, frac))
    bj_slider_knob_rect.centerx = bj_slider_track_rect.left + int(frac * bj_slider_track_rect.w)


def knob_x_to_slider_value():
    """
    Updates bj_slider_value based on bj_slider_knob_rect.x.
    """
    if bj_slider_max_value == bj_slider_min_value:
        bj_slider_value = bj_slider_min_value
        return
    frac = (bj_slider_knob_rect.centerx - bj_slider_track_rect.left) / float(bj_slider_track_rect.w)
    frac = max(0.0, min(1.0, frac))
    # round to nearest integer
    value = bj_slider_min_value + frac * (bj_slider_max_value - bj_slider_min_value)
    # assign to global
    globals()['bj_slider_value'] = int(value)


def draw_single_card(surface, card_code, center_x, center_y, angle_degrees):
    """
    Draws one card back with card code text on top.
    """
    if card_back_small is None:
        return

    img = card_back_small
    if angle_degrees != 0:
        img = pygame.transform.rotate(card_back_small, angle_degrees)

    rect = img.get_rect(center=(center_x, center_y))
    surface.blit(img, rect.topleft)

    label = FONT.render(card_code, True, (0, 0, 0))
    label_rect = label.get_rect(center=rect.center)
    surface.blit(label, label_rect)


def draw_hand_cards(surface, cards_list, center_x, center_y, spacing_x, base_angle):
    """
    Draws one player's hand as a row of cards.
    """
    n = len(cards_list)
    if n == 0:
        return

    start_x = center_x - (n - 1) * spacing_x // 2

    for i in range(n):
        x = start_x + i * spacing_x
        y = center_y
        card_code = cards_list[i]
        draw_single_card(surface, card_code, x, y, base_angle)



# ---------- Menu option helpers (LISTS, not dicts) ----------

def create_card_menu_option(center_x, center_y, width, height, text):
    """
    Creates a list-based menu option:
    [ pygame.Rect, text_string, clicked_flag ]
    """
    rect = pygame.Rect(center_x - width // 2, center_y - height // 2, width, height)
    return [rect, text, False]


def draw_card_menu_option(surface, option, card_img):
    """
    Draws a card-shaped menu option:
    - card image scaled to rect
    - text centered on top
    """
    rect = option[_OPT_RECT]
    text = option[_OPT_TEXT]

    # Card background
    if card_img is not None:
        card_surface = pygame.transform.smoothscale(card_img, (rect.w, rect.h))
        surface.blit(card_surface, rect.topleft)
    else:
        # fallback rectangle if image missing
        pygame.draw.rect(surface, (230, 230, 230), rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2)

    # Text centered on card
    t_surf = FONT.render(text, True, (0, 0, 0))
    t_rect = t_surf.get_rect(center=rect.center)
    surface.blit(t_surf, t_rect)


def card_menu_option_is_clicked(option, event):
    """
    One-shot click for a menu option (list-based).
    Uses MOUSEBUTTONDOWN + MOUSEBUTTONUP with a clicked flag.
    """
    rect = option[_OPT_RECT]

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if rect.collidepoint(event.pos) and not option[_OPT_CLICKED]:
            option[_OPT_CLICKED] = True
            return True

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        option[_OPT_CLICKED] = False

    return False


# ---------- Drawing functions for each state ----------

def draw_menu_screen(surface):
    # """
    # Draws the main Menu screen:
    # - background table
    # - 'Menu' title
    # - static stack-of-cards image in top-left
    # - three sideways card options in the center column
    # """
    # background table
    surface.blit(background, (0, 0))

    # Title
    title_surf = LARGE_FONT.render("Menu", True, (0, 0, 0))
    title_rect = title_surf.get_rect(center=(1280 // 2, 120))
    surface.blit(title_surf, title_rect)

    # Stack-of-cards image (non-interactive on the menu)
    if stack_of_cards_img is not None:
        scaled_stack = pygame.transform.smoothscale(stack_of_cards_img, (140, 140))
        surface.blit(scaled_stack, (190, 100))   # changed from (80, 160) as it was not on the table done via trail and error

    # Card-based menu options
    draw_card_menu_option(surface, blackjack_option, singular_card_img)
    draw_card_menu_option(surface, poker_option, singular_card_img)
    draw_card_menu_option(surface, rules_option, singular_card_img)


def draw_blackjack_placeholder(surface):
    """
    Blackjack GUI screen with 3 phases:
    - BJ_PHASE_SELECT_PLAYERS: popup asking 1–4 players
    - BJ_PHASE_ANTE: ante slider + confirm
    - BJ_PHASE_TABLE: full table + hit/stand controls
    """
    global bj_phase

    # background table
    surface.blit(background, (0, 0))

    if bj_phase == BJ_PHASE_SELECT_PLAYERS:
        # Darkened overlay
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 1280, 1024))
        pygame.draw.rect(surface, (0, 100, 0), pygame.Rect(140, 160, 1000, 500))

        title_surf = LARGE_FONT.render("How many players?", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(1280 // 2, 230))
        surface.blit(title_surf, title_rect)

        info_surf = FONT.render("Click 1, 2, 3 or 4 to select number of players.", True, (255, 255, 255))
        info_rect = info_surf.get_rect(center=(1280 // 2, 280))
        surface.blit(info_surf, info_rect)

        # 4 card options (created in Main)
        draw_card_menu_option(surface, bj_players_1_option, singular_card_img)
        draw_card_menu_option(surface, bj_players_2_option, singular_card_img)
        draw_card_menu_option(surface, bj_players_3_option, singular_card_img)
        draw_card_menu_option(surface, bj_players_4_option, singular_card_img)

    elif bj_phase == BJ_PHASE_ANTE:
        # Ante selection overlay
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 1280, 1024))
        pygame.draw.rect(surface, (0, 100, 0), pygame.Rect(140, 160, 1000, 500))

        title_surf = LARGE_FONT.render("Ante (bet) selection", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(1280 // 2, 230))
        surface.blit(title_surf, title_rect)

        # Show min/max and current value
        range_text = f"Min: {bj_slider_min_value}   Max: {bj_slider_max_value}   Current: {bj_slider_value}"
        range_surf = FONT.render(range_text, True, (255, 255, 255))
        range_rect = range_surf.get_rect(center=(1280 // 2, 320))
        surface.blit(range_surf, range_rect)

        # Draw slider track
        pygame.draw.rect(surface, (200, 200, 200), bj_slider_track_rect)
        # Draw slider knob
        pygame.draw.rect(surface, (255, 255, 0), bj_slider_knob_rect)

        # Confirm button
        draw_card_menu_option(surface, bj_confirm_ante_option, singular_card_img)

    elif bj_phase == BJ_PHASE_TABLE:
        # ---------------- Dealer ----------------
        dealer_label = FONT.render(str(dealer[_USER]), True, (0, 0, 0))
        dealer_label_rect = dealer_label.get_rect(center=(1280 // 2, 120))
        surface.blit(dealer_label, dealer_label_rect)

        draw_hand_cards(
            surface,
            dealer[_CARDS],
            center_x=1280 // 2,
            center_y=220,
            spacing_x=90,
            base_angle=0
        )

        dealer_result_text = f"Result: {dealer[_RESULT]}"
        dealer_result_surf = FONT.render(dealer_result_text, True, (0, 0, 0))
        dealer_result_rect = dealer_result_surf.get_rect(center=(1280 // 2, 280))
        surface.blit(dealer_result_surf, dealer_result_rect)

        # ---------------- Players ----------------
        player_seats = [
            (360, 700, -15),  # P1 bottom-left
            (530, 770, -5),   # P2
            (750, 770, 5),    # P3
            (920, 700, 15)    # P4 bottom-right
        ]

        n_players = len(players)
        for i in range(n_players):
            seat_x, seat_y, seat_angle = player_seats[i]

            name_text = str(players[i][_USER])
            name_surf = FONT.render(name_text, True, (0, 0, 0))
            name_rect = name_surf.get_rect(center=(seat_x, seat_y - 80))
            surface.blit(name_surf, name_rect)

            draw_hand_cards(
                surface,
                players[i][_CARDS],
                center_x=seat_x,
                center_y=seat_y,
                spacing_x=40,
                base_angle=seat_angle
            )

            currency_text = f"Fries: {players[i][_CURRENCY]}"
            result_text   = f"Result: {players[i][_RESULT]}"

            currency_surf = FONT.render(currency_text, True, (0, 0, 0))
            result_surf   = FONT.render(result_text,   True, (0, 0, 0))

            currency_rect = currency_surf.get_rect(center=(seat_x, seat_y + 80))
            result_rect   = result_surf.get_rect(center=(seat_x, seat_y + 110))

            surface.blit(currency_surf, currency_rect)
            surface.blit(result_surf, result_rect)

        # Hit area (stack-of-cards)
        if stack_of_cards_img is not None:
            stack_img_scaled = pygame.transform.smoothscale(stack_of_cards_img, (BJ_HIT_W, BJ_HIT_H))
            surface.blit(stack_img_scaled, (BJ_HIT_X, BJ_HIT_Y))
            hit_text = FONT.render("Hit", True, (0, 0, 0))
            surface.blit(hit_text, (BJ_HIT_X + 50, BJ_HIT_Y + BJ_HIT_H + 5))

        # Stand button (card-style)
        draw_card_menu_option(surface, bj_stand_option, singular_card_img)

        info_surf = FONT.render("Press M to return to Menu", True, (0, 0, 0))
        info_rect = info_surf.get_rect(topright=(1260, 20))
        surface.blit(info_surf, info_rect)


def draw_rules_placeholder(surface):

    # Placeholder Rules screen

    surface.blit(background, (0, 0))

    lines = [
        "Rules Screen (placeholder)",
        "Press M to return to the Menu."
    ]

    y = 260
    for line in lines:
        t_surf = FONT.render(line, True, (0, 0, 0))
        t_rect = t_surf.get_rect(center=(1280 // 2, y))
        surface.blit(t_surf, t_rect)
        y += 50





















######################################################################
##  Main   ###########################################################
######################################################################

# Create menu options (list-based, no dicts)
card_width  = 260
card_height = 90
center_x    = 1280 // 2

blackjack_option = create_card_menu_option(center_x, 320, card_width, card_height, "Blackjack")
poker_option     = create_card_menu_option(center_x, 450, card_width, card_height, "Poker (WIP)")
rules_option     = create_card_menu_option(center_x, 580, card_width, card_height, "Rules")

# Blackjack: popup options for number of players (1–4)
bj_players_1_option = create_card_menu_option(center_x - 150, 360, 80, 60, "1")
bj_players_2_option = create_card_menu_option(center_x - 50,  360, 80, 60, "2")
bj_players_3_option = create_card_menu_option(center_x + 50,  360, 80, 60, "3")
bj_players_4_option = create_card_menu_option(center_x + 150, 360, 80, 60, "4")

# Blackjack: confirm ante button
bj_confirm_ante_option = create_card_menu_option(center_x, 460, 220, 80, "Confirm Ante")

# Blackjack: stand button on table
bj_stand_option = create_card_menu_option(1120, 650, 200, 80, "Stand")

current_state = STATE_MENU

clock = pygame.time.Clock()
running = True

while running:
    pygame.display.set_icon(icon)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press M to return to menu (from future screens)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m and current_state != STATE_MENU:
                current_state = STATE_MENU

        if current_state == STATE_MENU:
            if current_state == STATE_BLACKJACK and bj_phase == BJ_PHASE_SELECT_PLAYERS:

                if card_menu_option_is_clicked(bj_players_1_option, event):
                    click_effect.play()
                    gui_set_n_players(1)
                    bj_phase = BJ_PHASE_TABLE

                if card_menu_option_is_clicked(bj_players_2_option, event):
                    click_effect.play()
                    gui_set_n_players(2)
                    bj_phase = BJ_PHASE_TABLE

                if card_menu_option_is_clicked(bj_players_3_option, event):
                    click_effect.play()
                    gui_set_n_players(3)
                    bj_phase = BJ_PHASE_TABLE

                if card_menu_option_is_clicked(bj_players_4_option, event):
                    click_effect.play()
                    gui_set_n_players(4)
                    bj_phase = BJ_PHASE_TABLE


            if card_menu_option_is_clicked(blackjack_option, event):
                click_effect.play()  # click sound when clicking an option
                bj_phase = BJ_PHASE_SELECT_PLAYERS  # start by asking how many players
                current_state = STATE_BLACKJACK

            if card_menu_option_is_clicked(poker_option, event):
                click_effect.play()
                current_state = STATE_BLACKJACK  # placeholder for poker

            if card_menu_option_is_clicked(rules_option, event):
                click_effect.play()
                current_state = STATE_RULES
            # ===================== BLACKJACK EVENTS =====================
        if current_state == STATE_BLACKJACK:

            # Phase 1: select number of players
            if bj_phase == BJ_PHASE_SELECT_PLAYERS:

                if card_menu_option_is_clicked(bj_players_1_option, event):
                    click_effect.play()
                    gui_set_n_players(1)
                    gui_reset_round_for_blackjack()
                    slider_value_to_knob_x()
                    bj_phase = BJ_PHASE_ANTE

                if card_menu_option_is_clicked(bj_players_2_option, event):
                    click_effect.play()
                    gui_set_n_players(2)
                    gui_reset_round_for_blackjack()
                    slider_value_to_knob_x()
                    bj_phase = BJ_PHASE_ANTE

                if card_menu_option_is_clicked(bj_players_3_option, event):
                    click_effect.play()
                    gui_set_n_players(3)
                    gui_reset_round_for_blackjack()
                    slider_value_to_knob_x()
                    bj_phase = BJ_PHASE_ANTE

                if card_menu_option_is_clicked(bj_players_4_option, event):
                    click_effect.play()
                    gui_set_n_players(4)
                    gui_reset_round_for_blackjack()
                    slider_value_to_knob_x()
                    bj_phase = BJ_PHASE_ANTE

            # Phase 2: ante slider
            elif bj_phase == BJ_PHASE_ANTE:

                # slider drag start
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bj_slider_knob_rect.collidepoint(event.pos):
                        bj_slider_dragging = True

                # slider drag end
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    bj_slider_dragging = False

                # slider drag motion
                if event.type == pygame.MOUSEMOTION and bj_slider_dragging:
                    # move knob horizontally within track
                    new_x = event.pos[0]
                    left = bj_slider_track_rect.left
                    right = bj_slider_track_rect.right
                    new_x = max(left, min(right, new_x))
                    bj_slider_knob_rect.centerx = new_x
                    knob_x_to_slider_value()

                # confirm ante button
                if card_menu_option_is_clicked(bj_confirm_ante_option, event):
                    click_effect.play()
                    # apply same ante to all players, respecting currency
                    for i in range(len(players)):
                        bet = bj_slider_value
                        if bet > players[i][_CURRENCY]:
                            bet = players[i][_CURRENCY]
                        dealersPot[i] = bet
                        players[i][_CURRENCY] -= bet

                    # shuffle deck and deal initial cards (2 per player + 2 for dealer)
                    ShuffleDeck(STANDARDDECK)
                    shuffle_effect.play()
                    for i in range(len(players)):
                        DealCards(players[i][_CARDS], 2)
                        deal_effect.play()
                    DealCards(dealer[_CARDS], 2)
                    deal_effect.play()

                    bj_phase = BJ_PHASE_TABLE  # move to main table view

            # Phase 3: table (hit/stand controls)
            elif bj_phase == BJ_PHASE_TABLE:

                # Hit: click stack-of-cards image (for now, always hits Player 1 / players[0])
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bj_hit_rect.collidepoint(event.pos) and not bj_hit_clicked:
                        bj_hit_clicked = True
                        click_effect.play()
                        if len(players) > 0:
                            DealCards(players[0][_CARDS], 1)
                            deal_effect.play()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    bj_hit_clicked = False

                # Stand: stand button
                if card_menu_option_is_clicked(bj_stand_option, event):
                    click_effect.play()
                    stand_effect.play()
                    # At this stage we are only triggering the sound and
                    # letting your existing logic decide what to do with stands later.

    # Draw based on state
    if current_state == STATE_MENU:
        draw_menu_screen(screen)
    elif current_state == STATE_BLACKJACK:
        draw_blackjack_placeholder(screen)
    elif current_state == STATE_RULES:
        draw_rules_placeholder(screen)

    pygame.display.update()
    clock.tick(60)









