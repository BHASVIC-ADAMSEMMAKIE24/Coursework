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
dealersPot = [0, 0, 0, 0]
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
dealer = [dealerUser, dealersPot, dealerCards, dealerResult]

players = [player1, player2, player3, player4]


def ResetRound():
    global dealer
    global dealersPot
    global players
    for i in range(len(players)):
        players[i][_CARDS] = []
        players[i][_RESULT] = ""
    dealer[_CARDS] = []
    dealer[_RESULT] = ""
    dealersPot = [0, 0, 0, 0]
    dealer[_CURRENCY] = [0, 0, 0, 0]


########################################################################################################################
# Cards.py
########################################################################################################################

# Suits:   Spades Hearts Diamonds Clubs
# Index:     [0]    [1]    [2]    [3]     Index Value
ORDEREDDECK = [["AcS", "AcH", "AcD", "AcC"],  # [0]   Ace
               ["02S", "02H", "02D", "02C"],  # [1]   Two
               ["03S", "03H", "03D", "03C"],  # [2]   Three
               ["04S", "04H", "04D", "04C"],  # [3]   Four
               ["05S", "05H", "05D", "05C"],  # [4]   Five
               ["06S", "06H", "06D", "06C"],  # [5]   Six
               ["07S", "07H", "07D", "07C"],  # [6]   Seven
               ["08S", "08H", "08D", "08C"],  # [7]   Eight
               ["09S", "09H", "09D", "09C"],  # [8]   Nine
               ["10S", "10H", "10D", "10C"],  # [9]   Ten
               ["JaS", "JaH", "JaD", "JaC"],  # [10]  Jack
               ["QuS", "QuH", "QuD", "QuC"],  # [11]  Queen
               ["KiS", "KiH", "KiD", "KiC"]]  # [12]  King

STANDARDDECK = ["AcS", "AcH", "AcD", "AcC",
                "02S", "02H", "02D", "02C",
                "03S", "03H", "03D", "03C",
                "04S", "04H", "04D", "04C",
                "05S", "05H", "05D", "05C",
                "06S", "06H", "06D", "06C",
                "07S", "07H", "07D", "07C",
                "08S", "08H", "08D", "08C",
                "09S", "09H", "09D", "09C",
                "10S", "10H", "10D", "10C",
                "JaS", "JaH", "JaD", "JaC",
                "QuS", "QuH", "QuD", "QuC",
                "KiS", "KiH", "KiD", "KiC"]
shuffledDeck = list(STANDARDDECK)


def ShuffleDeck(STANDARDDECK):
    global shuffledDeck
    shuffledDeck = list(STANDARDDECK)
    random.shuffle(shuffledDeck)


# ==================== Card Integration (GUI grid) ==================================================

def card_code_to_filename(card_code):
    value = card_code[0:2]
    suit = card_code[2]

    if value == "Ac":
        value_name = "ace"
    elif value == "02":
        value_name = "two"
    elif value == "03":
        value_name = "three"
    elif value == "04":
        value_name = "four"
    elif value == "05":
        value_name = "five"
    elif value == "06":
        value_name = "six"
    elif value == "07":
        value_name = "seven"
    elif value == "08":
        value_name = "eight"
    elif value == "09":
        value_name = "nine"
    elif value == "10":
        value_name = "ten"
    elif value == "Ja":
        value_name = "jack"
    elif value == "Qu":
        value_name = "queen"
    elif value == "Ki":
        value_name = "king"
    else:
        value_name = value

    if suit == "S":
        suit_name = "spades"
    elif suit == "H":
        suit_name = "hearts"
    elif suit == "D":
        suit_name = "diamonds"
    elif suit == "C":
        suit_name = "clubs"
    else:
        suit_name = "unknown"

    filename = value_name + "-of-" + suit_name + ".png"
    return filename


def CardIntegration(playerCards, nCards):
    global shuffledDeck

    cell_w = 80
    cell_h = 120
    cols = 13
    hgap = 10
    vgap = 10
    start_x = 40
    start_y = 160

    card_image_cache = []
    for code in STANDARDDECK:
        filename = card_code_to_filename(code)
        surf = None
        try:
            img = pygame.image.load(filename).convert_alpha()
            img = pygame.transform.smoothscale(img, (cell_w, cell_h))
            surf = img
        except Exception:
            surf = None
        card_image_cache.append([code, surf])

    def get_cached_image(code):
        for pair in card_image_cache:
            if pair[0] == code:
                return pair[1]
        return None

    selected = 0
    selecting = True
    clock = pygame.time.Clock()

    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for idx, code in enumerate(shuffledDeck):
                    row = idx // cols
                    col = idx % cols
                    x = start_x + col * (cell_w + hgap)
                    y = start_y + row * (cell_h + vgap)
                    rect = pygame.Rect(x, y, cell_w, cell_h)

                    if rect.collidepoint(mx, my):
                        playerCards.append(code)
                        shuffledDeck.remove(code)
                        if "deal_effect" in globals():
                            deal_effect.play()
                        selected += 1
                        if selected >= nCards:
                            selecting = False
                        break

        screen.blit(background, (0, 0))

        overlay = pygame.Surface((1280, 1024))
        overlay.set_alpha(200)
        overlay.fill((0, 100, 0))
        screen.blit(overlay, (0, 0))

        header = "Card Integration - click cards to select"
        header_surf = FONT.render(header, True, (255, 255, 255))
        screen.blit(header_surf, (40, 40))

        sub = "Selected " + str(selected) + " / " + str(nCards)
        sub_surf = FONT.render(sub, True, (255, 255, 255))
        screen.blit(sub_surf, (40, 80))

        info = "Remaining cards in deck: " + str(len(shuffledDeck))
        info_surf = FONT.render(info, True, (255, 255, 255))
        screen.blit(info_surf, (40, 110))

        for idx, code in enumerate(shuffledDeck):
            row = idx // cols
            col = idx % cols
            x = start_x + col * (cell_w + hgap)
            y = start_y + row * (cell_h + vgap)
            rect = pygame.Rect(x, y, cell_w, cell_h)

            surf = get_cached_image(code)

            if surf is not None:
                screen.blit(surf, rect.topleft)
            else:
                pygame.draw.rect(screen, (230, 230, 230), rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)
                code_surf = FONT.render(code, True, (0, 0, 0))
                code_rect = code_surf.get_rect(center=rect.center)
                screen.blit(code_surf, code_rect)

        pygame.display.update()
        clock.tick(60)

    return playerCards


def DealCards(playerCards, nCards):
    global shuffledDeck
    if nCards > len(shuffledDeck) or nCards < 0:
        print("nCards out of range")
    else:
        for i in range(nCards):
            head = len(shuffledDeck)
            card = shuffledDeck[head - 1]
            shuffledDeck.pop(head - 1)
            playerCards.append(card)
    return playerCards


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
    total = 0
    for i in range(len(deck)):
        total += int(CardValue(deck[i], "blackjack"))
    return total


def CardSuit(card):
    suit = card[2:]
    return suit


########################################################################################################################
# Blackjack.py
########################################################################################################################

dealerCards = []
player1Cards = []
player2Cards = []
player3Cards = []
player4Cards = []


def BlackjackAnte(players, dealersPot):
    for i in range(len(players)):
        print("Your currency: " + str(players[i][_CURRENCY]))
        dealersPot[i] = int(input("Enter ante bet: "))
        while players[i][_CURRENCY] < dealersPot[i] or dealersPot[i] < 0:
            print("Invalid bet")
            dealersPot[i] = int(input("Enter ante bet: "))
        players[i][_CURRENCY] -= dealersPot[i]
    return players, dealersPot


def BlackjackHitStandCycle(players):
    for i in range(len(players)):
        print(players[i][_USER], " turn")
        choice = "hit"
        while players[i][_RESULT] != "Bust" and choice.lower() == "hit":
            choice = input("Hit or Stand: ")
            if choice.lower() == "hit":
                DealCards(players[i][_CARDS], 1)
                print(players[i][_CARDS])
                if int(CardTotal(players[i][_CARDS])) > 21:
                    players[i][_RESULT] = "Bust"
                    print(players[i][_RESULT])

            elif choice.lower() == "stand":
                print("")
        print(players[i][_USER], " turn ended")
    print("All player turns have ended")
    return players


def BlackjackResult(players, dealer):
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


def BlackjackRound(players, dealer, isCardIntegration):
    ShuffleDeck(STANDARDDECK)
    BlackjackAnte(players, dealersPot)
    if isCardIntegration:
        for i in range(len(players)):
            CardIntegration(players[i][_CARDS], 2)
    else:
        for i in range(len(players)):
            DealCards(players[i][_CARDS], 2)
    DealCards(dealer[_CARDS], 2)
    print(dealer[_USER], "Cards:", dealer[_CARDS][0], "???")
    for i in range(len(players)):
        print(players[i][_USER], "Cards: ", players[i][_CARDS])
    BlackjackHitStandCycle(players)
    print(dealer[_USER], "Cards:", dealer[_CARDS])
    if CardTotal(dealer[_CARDS]) < 17:
        DealCards(dealer[_CARDS], 1)
        print(dealer[_USER], "Cards:", dealer[_CARDS])
        while CardTotal(dealer[_CARDS]) < 17:
            DealCards(dealer[_CARDS], 1)
            print(dealer[_USER], "Cards:", dealer[_CARDS])
    BlackjackResult(players, dealer)
    BJWinningsCalculation(players, dealersPot)
    print(dealer[_USER], "Result:", dealer[_RESULT])
    for i in range(len(players)):
        print(players[i][_USER], "Result: ", players[i][_RESULT])
    return player1Currency, player2Currency, player3Currency, player4Currency


########################################################################################################################
# Currency.py
########################################################################################################################

def BJWinningsCalculation(players, dealersPot):
    for i in range(len(players)):
        if players[i][_RESULT] == "Win":
            players[i][_CURRENCY] += int((dealersPot[i] * 2))
        elif players[i][_RESULT] == "Draw":
            players[i][_CURRENCY] += int(dealersPot[i])
    return players


def TotalPot(dealersPot):
    total = 0
    for i in range(len(dealersPot)):
        total += dealersPot[i]
    return total


def PKWinningsCalculation(players, dealersPot):
    nWinners = 0
    for i in range(len(players)):
        if players[i][_RESULT] == "Draw" or players[i][_RESULT] == "Win":
            nWinners += 1
    for j in range(len(players)):
        if players[j][_RESULT] == "Draw" or players[j][_RESULT] == "Win":
            players[j][_CURRENCY] += (int(TotalPot(dealersPot)) // nWinners)
    return players


########################################################################################################################
# Menu.py (text version, still here but GUI is used)
########################################################################################################################

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
        players = [player1, player2]
    elif nPlayers == 3:
        players = [player1, player2, player3]
    elif nPlayers == 4:
        players = [player1, player2, player3, player4]
    for u in range(len(players)):
        username = input(players[u][_USER] + " Enter your username: ")
        players[u][_USER] = username


def StartBlackjack(players, dealer):
    choice = input("Card Integration?")
    if choice[0:1].lower() == "y":
        isCardIntegration = True
    else:
        isCardIntegration = False
    nRounds = int(input("Enter number of rounds: "))
    for r in range(nRounds):
        ResetRound()
        BlackjackRound(players, dealer, isCardIntegration)
    return players


def StartPoker(players, dealer):
    choice = input("Card Integration?")
    if choice[0:1].lower() == "y":
        isCardIntegration = True
    else:
        isCardIntegration = False
    nRounds = int(input("Enter number of rounds: "))
    return players


def Rules():
    print("Blackjack Rules:\nThe goal of Blackjack is to get a hand value closer to 21 than the dealer's hand without going over. To play, players place a bet, and receive two cards. The dealer also receives two cards, one face-up and one face-down. Number cards are worth their face value, face cards are worth 10, and an Ace can be 1 or 11. Players then hit to take more cards or stand to keep their current hand. The dealer must hit until their hand is at least 17. \n")
    print("Poker Rules:\nIn poker, you aim to make the best five-card hand from your two private hole cards and five community cards. After initial forced bets (blinds), you bet, call, raise, or fold your way through four betting rounds that follow the dealing of the flop (three community cards), the turn (fourth card), and the river (fifth and final card). The player with the highest-ranking hand at the showdown wins the pot, or the last remaining player who hasn't folded wins.\n")
    print("Poker hand rankings:\nRoyal Flush: Ac, Ki, Qu, Ja, and 10, all of the same suit.\nStraight Flush: Any straight of the same suit. For example, JaC, 10C, 09C, 08C, 07C.\nFour of a Kind: Any four cards of the same value, plus another random card. For example, 08C, 08D, 08H, 08S, JaH.\nFull House: Three cards of one value and two cards of another value. For example, JaC, JaH, JaS, 02C, 02D.\nFlush: All cards of the same suit. The value doesnt matter.\nStraight: 5 cards of consecutive value but of different suits.\nThree of a Kind: Any three cards of the same value and two random cards. For example, 05C, 05S, 05H, 03C, JaD\nTwo Pair: Two pairs of cards of equal value and one random card. For example, 08S, 08D, 04C, 04H, JaS.\nPair: One pair of cards of equal value and three random cards. For example, QuD, QuH, 08S, 05C, 03H.\nHigh Card: No cards interact with other cards in any way, so the highest value card.")


def Menu():
    PlayerSetup()
    choice = input("Enter your choice: (blackjack,rules,poker)\n)")
    if choice == "blackjack":
        StartBlackjack(players, dealer)
    elif choice == "rules":
        Rules()
    elif choice == "poker":
        StartPoker(players, dealer)


########################################################################################################################
# GUI.py
########################################################################################################################

pygame.init()

screen = pygame.display.set_mode((1280, 1024))

pygame.display.set_caption('The Cards Collective')
icon = pygame.image.load('icon.png')

background = pygame.image.load("background.png")

mixer.music.load("background-music.wav")
mixer.music.play(-1)

shuffle_effect = mixer.Sound("shuffle-sound.wav")
deal_effect = mixer.Sound("card-sound.wav")
stand_effect = mixer.Sound("stand-sound.wav")
click_effect = mixer.Sound("click-sound.wav")

FONT = pygame.font.SysFont(None, 32)
LARGE_FONT = pygame.font.SysFont(None, 72)

STATE_SETUP = "setup"
STATE_MENU = "menu"
STATE_BLACKJACK = "blackjack"
STATE_RULES = "rules"
STATE_POKER = "poker"

_OPT_RECT = 0
_OPT_TEXT = 1
_OPT_CLICKED = 2


def load_menu_images():
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

# --------- card images for actual cards ----------

card_image_list = []  # [code, surface]


def load_card_images():
    global card_image_list
    for code in STANDARDDECK:
        filename = card_code_to_filename(code)
        try:
            img = pygame.image.load(filename).convert_alpha()
            img = pygame.transform.smoothscale(img, (80, 120))
            card_image_list.append([code, img])
        except Exception:
            continue


def get_card_image(card_code):
    for pair in card_image_list:
        if pair[0] == card_code:
            return pair[1]
    return None


load_card_images()

# --------- fries currency images ----------

bucket_img_small = None
bag_img_small = None
stack_fries_img_small = None
handful_img_small = None

try:
    img = pygame.image.load("bucket-of-fries.png").convert_alpha()
    bucket_img_small = pygame.transform.smoothscale(img, (60, 60))
except Exception:
    bucket_img_small = None

try:
    img = pygame.image.load("bag-of-fries.png").convert_alpha()
    bag_img_small = pygame.transform.smoothscale(img, (60, 60))
except Exception:
    bag_img_small = None

try:
    img = pygame.image.load("stack-of-fries.png").convert_alpha()
    stack_fries_img_small = pygame.transform.smoothscale(img, (60, 60))
except Exception:
    stack_fries_img_small = None

try:
    img = pygame.image.load("handful-of-fries.png").convert_alpha()
    handful_img_small = pygame.transform.smoothscale(img, (60, 60))
except Exception:
    handful_img_small = None


def draw_fries_amount(surface, amount, base_x, base_y):
    """
    Draw fries icons representing 'amount' of currency.
    Uses:
      bucket  = 2000
      bag     = 1000
      stack   = 200
      handful = 50
    Rounds amount down to nearest 50.
    Draws rows: bucket row, bag row, stack row, handful row.
    """

    # round down to nearest 50
    if amount <= 0:
        return
    amount = (amount // 50) * 50
    if amount <= 0:
        return

    values = [2000, 1000, 200, 50]
    images = [bucket_img_small, bag_img_small, stack_fries_img_small, handful_img_small]
    row_gap = 50
    col_gap = 40

    for row in range(4):
        v = values[row]
        img = images[row]
        if img is None:
            # if image missing, skip this type
            continue
        count = amount // v
        amount -= count * v
        for c in range(count):
            x = base_x + c * col_gap
            y = base_y + row * row_gap
            surface.blit(img, (x, y))

# ===================== BLACKJACK GUI STATE & HELPERS =====================


def checkbox_is_clicked(checkbox, event):
    rect = checkbox[0]
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if rect.collidepoint(event.pos):
            checkbox[1] = not checkbox[1]
            if "click_effect" in globals():
                click_effect.play()
            return True
    return False


BJ_PHASE_ANTE = 1
BJ_PHASE_TABLE = 2

bj_phase = BJ_PHASE_ANTE

bj_slider_min_value = 0
bj_slider_max_value = 0
bj_slider_value = 0
bj_slider_dragging = False

bj_slider_track_rect = pygame.Rect(400, 380, 480, 8)
bj_slider_knob_rect = pygame.Rect(400, 370, 20, 28)

BJ_HIT_W = 140
BJ_HIT_H = 140
BJ_HIT_X = 190
BJ_HIT_Y = 100
bj_hit_rect = pygame.Rect(BJ_HIT_X, BJ_HIT_Y, BJ_HIT_W, BJ_HIT_H)
bj_hit_clicked = False

card_back_small = None
if singular_card_img is not None:
    card_back_small = pygame.transform.smoothscale(singular_card_img, (80, 120))

bj_ante_player_index = 0
bj_current_player_index = 0
bj_round_over = False
bj_dealer_done = False
bj_dealer_reveal = False


def gui_set_n_players(n):
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
    global bj_slider_min_value, bj_slider_max_value, bj_slider_value
    global bj_round_over, bj_dealer_done, bj_dealer_reveal

    ResetRound()
    ShuffleDeck(STANDARDDECK)

    bj_round_over = False
    bj_dealer_done = False
    bj_dealer_reveal = False

    if len(players) > 0:
        bj_slider_min_value = 0
        bj_slider_max_value = min([p[_CURRENCY] for p in players])
    else:
        bj_slider_min_value = 0
        bj_slider_max_value = 0

    bj_slider_value = bj_slider_min_value
    bj_slider_knob_rect.x = bj_slider_track_rect.left


def gui_prepare_ante_for_player(idx):
    global bj_slider_min_value, bj_slider_max_value, bj_slider_value, bj_ante_player_index
    bj_ante_player_index = idx
    if idx < len(players):
        bj_slider_min_value = 0
        bj_slider_max_value = players[idx][_CURRENCY]
    else:
        bj_slider_min_value = 0
        bj_slider_max_value = 0
    bj_slider_value = bj_slider_min_value
    slider_value_to_knob_x()


def slider_value_to_knob_x():
    if bj_slider_max_value == bj_slider_min_value:
        bj_slider_knob_rect.centerx = bj_slider_track_rect.left
        return
    frac = (bj_slider_value - bj_slider_min_value) / float(bj_slider_max_value - bj_slider_min_value)
    if frac < 0.0:
        frac = 0.0
    if frac > 1.0:
        frac = 1.0
    bj_slider_knob_rect.centerx = bj_slider_track_rect.left + int(frac * bj_slider_track_rect.w)


def knob_x_to_slider_value():
    global bj_slider_value
    if bj_slider_max_value == bj_slider_min_value:
        bj_slider_value = bj_slider_min_value
        return
    frac = (bj_slider_knob_rect.centerx - bj_slider_track_rect.left) / float(bj_slider_track_rect.w)
    if frac < 0.0:
        frac = 0.0
    if frac > 1.0:
        frac = 1.0
    value = bj_slider_min_value + frac * (bj_slider_max_value - bj_slider_min_value)
    bj_slider_value = int(value)


def draw_single_card(surface, card_code, center_x, center_y, angle_degrees):
    if card_back_small is None:
        return

    img = get_card_image(card_code)
    if img is None:
        img = card_back_small

    if angle_degrees != 0:
        img = pygame.transform.rotate(img, angle_degrees)

    rect = img.get_rect(center=(center_x, center_y))
    surface.blit(img, rect.topleft)


def draw_card_back(surface, center_x, center_y, angle_degrees):
    if card_back_small is None:
        return
    img = card_back_small
    if angle_degrees != 0:
        img = pygame.transform.rotate(img, angle_degrees)
    rect = img.get_rect(center=(center_x, center_y))
    surface.blit(img, rect.topleft)


def draw_hand_cards(surface, cards_list, center_x, center_y, spacing_x, base_angle):
    n = len(cards_list)
    if n == 0:
        return
    start_x = center_x - (n - 1) * spacing_x // 2
    for i in range(n):
        x = start_x + i * spacing_x
        y = center_y
        card_code = cards_list[i]
        draw_single_card(surface, card_code, x, y, base_angle)


def gui_start_table_round():
    global bj_current_player_index, bj_round_over, bj_dealer_done, bj_dealer_reveal
    bj_current_player_index = 0
    bj_round_over = False
    bj_dealer_done = False
    bj_dealer_reveal = False

    for i in range(len(players)):
        if players[i][_RESULT] not in ["Win", "Loss", "Draw", "Bust", "Stand"]:
            players[i][_RESULT] = ""
    dealer[_RESULT] = ""


def gui_advance_after_player_action():
    global bj_current_player_index, bj_round_over, bj_dealer_done, bj_dealer_reveal

    while bj_current_player_index < len(players) and players[bj_current_player_index][_RESULT] in ["Bust", "Stand"]:
        bj_current_player_index += 1

    if bj_current_player_index < len(players):
        return

    if not bj_dealer_done:
        while CardTotal(dealer[_CARDS]) < 17:
            DealCards(dealer[_CARDS], 1)
            deal_effect.play()

        if CardTotal(dealer[_CARDS]) > 21:
            dealer[_RESULT] = "Bust"

        BlackjackResult(players, dealer)
        BJWinningsCalculation(players, dealersPot)

        bj_dealer_done = True
        bj_round_over = True
        bj_dealer_reveal = True


# ---------- Menu option helpers ----------

def create_card_menu_option(center_x, center_y, width, height, text):
    rect = pygame.Rect(center_x - width // 2, center_y - height // 2, width, height)
    return [rect, text, False]


def draw_card_menu_option(surface, option, card_img):
    rect = option[_OPT_RECT]
    text = option[_OPT_TEXT]

    if card_img is not None:
        card_surface = pygame.transform.smoothscale(card_img, (rect.w, rect.h))
        surface.blit(card_surface, rect.topleft)
    else:
        pygame.draw.rect(surface, (230, 230, 230), rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2)

    t_surf = FONT.render(text, True, (0, 0, 0))
    t_rect = t_surf.get_rect(center=rect.center)
    surface.blit(t_surf, t_rect)


def card_menu_option_is_clicked(option, event):
    rect = option[_OPT_RECT]

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if rect.collidepoint(event.pos) and not option[_OPT_CLICKED]:
            option[_OPT_CLICKED] = True
            return True

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        option[_OPT_CLICKED] = False

    return False


# ---------- PLAYER SETUP ----------

SETUP_PHASE_NUM_PLAYERS = 0
SETUP_PHASE_USERNAMES = 1

setup_phase = SETUP_PHASE_NUM_PLAYERS
setup_n_players = 1
setup_current_index = 0
username_input_text = ""
username_input_rect = pygame.Rect(400, 420, 480, 40)

setup_players_1_option = create_card_menu_option(1280 // 2 - 150, 360, 80, 60, "1")
setup_players_2_option = create_card_menu_option(1280 // 2 - 50, 360, 80, 60, "2")
setup_players_3_option = create_card_menu_option(1280 // 2 + 50, 360, 80, 60, "3")
setup_players_4_option = create_card_menu_option(1280 // 2 + 150, 360, 80, 60, "4")

bj_cardint_checkbox = [pygame.Rect(400, 300, 28, 28), False]


def draw_setup_screen(surface):
    global setup_phase

    surface.blit(background, (0, 0))

    if setup_phase == SETUP_PHASE_NUM_PLAYERS:
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 1280, 1024))
        pygame.draw.rect(surface, (0, 100, 0), pygame.Rect(140, 160, 1000, 500))

        title_surf = LARGE_FONT.render("Welcome! How many players?", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(1280 // 2, 230))
        surface.blit(title_surf, title_rect)

        info_surf = FONT.render("Click 1, 2, 3 or 4 to select number of players.", True, (255, 255, 255))
        info_rect = info_surf.get_rect(center=(1280 // 2, 280))
        surface.blit(info_surf, info_rect)

        draw_card_menu_option(surface, setup_players_1_option, singular_card_img)
        draw_card_menu_option(surface, setup_players_2_option, singular_card_img)
        draw_card_menu_option(surface, setup_players_3_option, singular_card_img)
        draw_card_menu_option(surface, setup_players_4_option, singular_card_img)

    elif setup_phase == SETUP_PHASE_USERNAMES:
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 1280, 1024))
        pygame.draw.rect(surface, (0, 100, 0), pygame.Rect(140, 160, 1000, 500))

        player_number = setup_current_index + 1
        title_text = "Enter username for Player " + str(player_number)
        title_surf = LARGE_FONT.render(title_text, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(1280 // 2, 230))
        surface.blit(title_surf, title_rect)

        info_surf = FONT.render("Type a name and press Enter to confirm.", True, (255, 255, 255))
        info_rect = info_surf.get_rect(center=(1280 // 2, 280))
        surface.blit(info_surf, info_rect)

        pygame.draw.rect(surface, (255, 255, 255), username_input_rect)
        pygame.draw.rect(surface, (0, 0, 0), username_input_rect, 2)

        text_surf = FONT.render(username_input_text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(midleft=(username_input_rect.x + 10, username_input_rect.centery))
        surface.blit(text_surf, text_rect)

    label = FONT.render("Use Card Integration", True, (255, 255, 255))
    surface.blit(label, (450, 300))

    pygame.draw.rect(surface, (255, 255, 255), bj_cardint_checkbox[0], 2)
    if bj_cardint_checkbox[1]:
        inner = bj_cardint_checkbox[0].inflate(-6, -6)
        pygame.draw.rect(surface, (255, 255, 255), inner)


# ---------- Drawing functions for each main state ----------

def draw_menu_screen(surface):
    surface.blit(background, (0, 0))

    title_surf = LARGE_FONT.render("Menu", True, (0, 0, 0))
    title_rect = title_surf.get_rect(center=(1280 // 2, 120))
    surface.blit(title_surf, title_rect)

    if stack_of_cards_img is not None:
        scaled_stack = pygame.transform.smoothscale(stack_of_cards_img, (140, 140))
        surface.blit(scaled_stack, (190, 100))

    draw_card_menu_option(surface, blackjack_option, singular_card_img)
    draw_card_menu_option(surface, poker_option, singular_card_img)
    draw_card_menu_option(surface, rules_option, singular_card_img)

    # Currency guide using fries images
    guide_title = FONT.render("Currency (fries)", True, (0, 0, 0))
    guide_rect = guide_title.get_rect(center=(1280 // 2, 650))
    surface.blit(guide_title, guide_rect)

    y_row = 690
    x_start = 140
    x_gap = 260

    # bucket
    if bucket_img_small is not None:
        surface.blit(bucket_img_small, (x_start, y_row))
    text = FONT.render("Bucket = 2000", True, (0, 0, 0))
    surface.blit(text, (x_start + 70, y_row + 15))

    # bag
    if bag_img_small is not None:
        surface.blit(bag_img_small, (x_start + x_gap, y_row))
    text = FONT.render("Bag = 1000", True, (0, 0, 0))
    surface.blit(text, (x_start + x_gap + 70, y_row + 15))

    # stack
    if stack_fries_img_small is not None:
        surface.blit(stack_fries_img_small, (x_start + 2 * x_gap, y_row))
    text = FONT.render("Stack = 200", True, (0, 0, 0))
    surface.blit(text, (x_start + 2 * x_gap + 70, y_row + 15))

    # handful
    if handful_img_small is not None:
        surface.blit(handful_img_small, (x_start + 3 * x_gap, y_row))
    text = FONT.render("Handful = 50", True, (0, 0, 0))
    surface.blit(text, (x_start + 3 * x_gap + 70, y_row + 15))


def draw_blackjack_screen(surface):
    global bj_phase

    surface.blit(background, (0, 0))

    if bj_phase == BJ_PHASE_ANTE:
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 1280, 1024))
        pygame.draw.rect(surface, (0, 100, 0), pygame.Rect(140, 160, 1000, 500))

        if bj_ante_player_index < len(players):
            player_name = players[bj_ante_player_index][_USER]
        else:
            player_name = "Unknown"

        title_surf = LARGE_FONT.render("Ante for " + player_name, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(1280 // 2, 230))
        surface.blit(title_surf, title_rect)

        range_text = "Min: " + str(bj_slider_min_value) + "   Max: " + str(bj_slider_max_value) + "   Current: " + str(
            bj_slider_value)
        range_surf = FONT.render(range_text, True, (255, 255, 255))
        range_rect = range_surf.get_rect(center=(1280 // 2, 320))
        surface.blit(range_surf, range_rect)

        pygame.draw.rect(surface, (200, 200, 200), bj_slider_track_rect)
        pygame.draw.rect(surface, (255, 255, 0), bj_slider_knob_rect)

        draw_card_menu_option(surface, bj_confirm_ante_option, singular_card_img)

    elif bj_phase == BJ_PHASE_TABLE:
        dealer_label = FONT.render(str(dealer[_USER]), True, (0, 0, 0))
        dealer_label_rect = dealer_label.get_rect(center=(1280 // 2, 120))
        surface.blit(dealer_label, dealer_label_rect)

        dealer_hand = dealer[_CARDS]
        center_x = 1280 // 2
        center_y = 220

        if not bj_dealer_reveal:
            n = len(dealer_hand)
            if n == 1:
                draw_single_card(surface, dealer_hand[0], center_x, center_y, 0)
            elif n >= 2:
                offset = 45
                draw_single_card(surface, dealer_hand[0], center_x - offset, center_y, 0)
                draw_card_back(surface, center_x + offset, center_y, 0)
        else:
            draw_hand_cards(surface, dealer_hand, center_x, center_y, 90, 0)

        if bj_dealer_reveal:
            dealer_result_text = "Result: " + str(dealer[_RESULT])
        else:
            dealer_result_text = "Result: ?"
        dealer_result_surf = FONT.render(dealer_result_text, True, (0, 0, 0))
        dealer_result_rect = dealer_result_surf.get_rect(center=(1280 // 2, 280))
        surface.blit(dealer_result_surf, dealer_result_rect)

        player_seats = [
            (360, 700, -15),
            (530, 770, -5),
            (750, 770, 5),
            (920, 700, 15)
        ]

        n_players = len(players)
        for i in range(n_players):
            seat_x, seat_y, seat_angle = player_seats[i]

            name_text = str(players[i][_USER])
            name_surf = FONT.render(name_text, True, (0, 0, 0))
            name_rect = name_surf.get_rect(center=(seat_x, seat_y - 80))
            surface.blit(name_surf, name_rect)

            draw_hand_cards(surface, players[i][_CARDS], seat_x, seat_y, 40, seat_angle)

            currency_text = "Fries: " + str(players[i][_CURRENCY])
            result_text = "Result: " + str(players[i][_RESULT])

            currency_surf = FONT.render(currency_text, True, (0, 0, 0))
            result_surf = FONT.render(result_text, True, (0, 0, 0))

            currency_rect = currency_surf.get_rect(center=(seat_x, seat_y + 80))
            result_rect = result_surf.get_rect(center=(seat_x, seat_y + 110))

            surface.blit(currency_surf, currency_rect)
            surface.blit(result_surf, result_rect)

            # draw fries icons for this player's currency (rounded down to nearest 50)
            draw_fries_amount(surface, players[i][_CURRENCY], seat_x - 60, seat_y -170)

        if stack_of_cards_img is not None:
            stack_img_scaled = pygame.transform.smoothscale(stack_of_cards_img, (BJ_HIT_W, BJ_HIT_H))
            surface.blit(stack_img_scaled, (BJ_HIT_X, BJ_HIT_Y))
            hit_text = FONT.render("Hit", True, (0, 0, 0))
            surface.blit(hit_text, (BJ_HIT_X + 50, BJ_HIT_Y + BJ_HIT_H + 5))

        draw_card_menu_option(surface, bj_stand_option, singular_card_img)
        draw_card_menu_option(surface, bj_new_round_option, singular_card_img)

        if not bj_round_over and bj_current_player_index < len(players):
            turn_name = players[bj_current_player_index][_USER]
            turn_text = "Turn: " + turn_name
        else:
            turn_text = "Round over"

        turn_surf = FONT.render(turn_text, True, (0, 0, 0))
        turn_rect = turn_surf.get_rect(topleft=(20, 20))
        surface.blit(turn_surf, turn_rect)

        info_surf = FONT.render("Press M to return to Menu", True, (0, 0, 0))
        info_rect = info_surf.get_rect(topright=(1260, 20))
        surface.blit(info_surf, info_rect)


def draw_rules_screen(surface):
    surface.blit(background, (0, 0))

    title_surf = LARGE_FONT.render("Rules", True, (0, 0, 0))
    title_rect = title_surf.get_rect(center=(1280 // 2, 80))
    surface.blit(title_surf, title_rect)

    info_surf = FONT.render("Press M to return to Menu", True, (0, 0, 0))
    info_rect = info_surf.get_rect(topright=(1260, 20))
    surface.blit(info_surf, info_rect)

    blackjack_text = (
        "Blackjack Rules:\n"
        "The goal of Blackjack is to get a hand value closer to 21 than the dealer's hand "
        "without going over. To play, players place a bet, and receive two cards. The dealer "
        "also receives two cards, one face-up and one face-down. Number cards are worth their "
        "face value, face cards are worth 10, and an Ace can be 1 or 11. Players then hit to "
        "take more cards or stand to keep their current hand. The dealer must hit until their "
        "hand is at least 17."
    )

    poker_text = (
        "Poker Rules:\n"
        "In poker, you aim to make the best five-card hand from your two private hole cards "
        "and five community cards. After initial forced bets (blinds), you bet, call, raise, "
        "or fold your way through four betting rounds that follow the dealing of the flop "
        "(three community cards), the turn (fourth card), and the river (fifth and final card). "
        "The player with the highest-ranking hand at the showdown wins the pot, or the last "
        "remaining player who hasn't folded wins."
    )

    rankings_text = (
        "Poker hand rankings:\n"
        "Royal Flush: Ac, Ki, Qu, Ja, and 10, all of the same suit.\n"
        "Straight Flush: Any straight of the same suit. For example, JaC, 10C, 09C, 08C, 07C.\n"
        "Four of a Kind: Any four cards of the same value, plus another random card. For example, 08C, 08D, 08H, 08S, JaH.\n"
        "Full House: Three cards of one value and two cards of another value. For example, JaC, JaH, JaS, 02C, 02D.\n"
        "Flush: All cards of the same suit. The value doesnt matter.\n"
        "Straight: 5 cards of consecutive value but of different suits.\n"
        "Three of a Kind: Any three cards of the same value and two random cards. For example, 05C, 05S, 05H, 03C, JaD.\n"
        "Two Pair: Two pairs of cards of equal value and one random card. For example, 08S, 08D, 04C, 04H, JaS.\n"
        "Pair: One pair of cards of equal value and three random cards. For example, QuD, QuH, 08S, 05C, 03H.\n"
        "High Card: No cards interact with other cards in any way, so the highest value card."
    )

    def draw_multiline(text, start_x, start_y, line_spacing):
        y = start_y
        lines = text.split("\n")
        for line in lines:
            line_surf = FONT.render(line, True, (0, 0, 0))
            line_rect = line_surf.get_rect(topleft=(start_x, y))
            surface.blit(line_surf, line_rect)
            y += line_spacing
        return y

    left_x = 80
    y = 140
    y = draw_multiline(blackjack_text, left_x, y, 28)
    y += 20
    y = draw_multiline(poker_text, left_x, y, 28)
    y += 20
    draw_multiline(rankings_text, left_x, y, 24)


def draw_poker_wip_screen(surface):
    surface.blit(background, (0, 0))

    title_surf = LARGE_FONT.render("Poker", True, (0, 0, 0))
    title_rect = title_surf.get_rect(center=(1280 // 2, 120))
    surface.blit(title_surf, title_rect)

    lines = [
        "Poker is not available yet.",
        "Press M to return to the Menu."
    ]
    y = 260
    for line in lines:
        t_surf = FONT.render(line, True, (0, 0, 0))
        t_rect = t_surf.get_rect(center=(1280 // 2, y))
        surface.blit(t_surf, t_rect)
        y += 40


# ------------------------- MAIN -------------------------

card_width = 260
card_height = 90
center_x = 1280 // 2

blackjack_option = create_card_menu_option(center_x, 320, card_width, card_height, "Blackjack")
poker_option = create_card_menu_option(center_x, 450, card_width, card_height, "Poker (WIP)")
rules_option = create_card_menu_option(center_x, 580, card_width, card_height, "Rules")

bj_confirm_ante_option = create_card_menu_option(center_x, 460, 220, 80, "Confirm Ante")
bj_stand_option = create_card_menu_option(1120, 650, 200, 80, "Stand")
bj_new_round_option = create_card_menu_option(1120, 750, 200, 80, "New Round")

current_state = STATE_SETUP

clock = pygame.time.Clock()
running = True

while running:
    pygame.display.set_icon(icon)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # global 'back to menu'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m and current_state in (STATE_BLACKJACK, STATE_RULES, STATE_POKER):
                current_state = STATE_MENU

        # ---------- SETUP STATE ----------
        if current_state == STATE_SETUP:
            checkbox_is_clicked(bj_cardint_checkbox, event)

            if setup_phase == SETUP_PHASE_NUM_PLAYERS:
                if card_menu_option_is_clicked(setup_players_1_option, event):
                    click_effect.play()
                    setup_n_players = 1
                    gui_set_n_players(setup_n_players)
                    setup_phase = SETUP_PHASE_USERNAMES
                    setup_current_index = 0
                    username_input_text = ""

                if card_menu_option_is_clicked(setup_players_2_option, event):
                    click_effect.play()
                    setup_n_players = 2
                    gui_set_n_players(setup_n_players)
                    setup_phase = SETUP_PHASE_USERNAMES
                    setup_current_index = 0
                    username_input_text = ""

                if card_menu_option_is_clicked(setup_players_3_option, event):
                    click_effect.play()
                    setup_n_players = 3
                    gui_set_n_players(setup_n_players)
                    setup_phase = SETUP_PHASE_USERNAMES
                    setup_current_index = 0
                    username_input_text = ""

                if card_menu_option_is_clicked(setup_players_4_option, event):
                    click_effect.play()
                    setup_n_players = 4
                    gui_set_n_players(setup_n_players)
                    setup_phase = SETUP_PHASE_USERNAMES
                    setup_current_index = 0
                    username_input_text = ""

            elif setup_phase == SETUP_PHASE_USERNAMES:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        name = username_input_text.strip()
                        if name == "":
                            name = "Player " + str(setup_current_index + 1)
                        if setup_current_index < len(players):
                            players[setup_current_index][_USER] = name
                        setup_current_index += 1
                        if setup_current_index >= setup_n_players or setup_current_index >= len(players):
                            current_state = STATE_MENU
                        else:
                            username_input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        username_input_text = username_input_text[:-1]
                    else:
                        if len(username_input_text) < 20:
                            username_input_text += event.unicode

        # ---------- MENU STATE ----------
        if current_state == STATE_MENU:
            if card_menu_option_is_clicked(blackjack_option, event):
                click_effect.play()
                gui_reset_round_for_blackjack()
                if len(players) > 0:
                    gui_prepare_ante_for_player(0)
                bj_phase = BJ_PHASE_ANTE
                current_state = STATE_BLACKJACK

            if card_menu_option_is_clicked(poker_option, event):
                click_effect.play()
                current_state = STATE_POKER

            if card_menu_option_is_clicked(rules_option, event):
                click_effect.play()
                current_state = STATE_RULES

        # ---------- BLACKJACK STATE ----------
        if current_state == STATE_BLACKJACK:

            if bj_phase == BJ_PHASE_ANTE:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bj_slider_knob_rect.collidepoint(event.pos):
                        bj_slider_dragging = True

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    bj_slider_dragging = False

                if event.type == pygame.MOUSEMOTION and bj_slider_dragging:
                    new_x = event.pos[0]
                    left = bj_slider_track_rect.left
                    right = bj_slider_track_rect.right
                    if new_x < left:
                        new_x = left
                    if new_x > right:
                        new_x = right
                    bj_slider_knob_rect.centerx = new_x
                    knob_x_to_slider_value()

                if card_menu_option_is_clicked(bj_confirm_ante_option, event):
                    click_effect.play()
                    bj_use_card_integration = bj_cardint_checkbox[1]
                    i = bj_ante_player_index
                    if i < len(players):
                        bet = bj_slider_value
                        if bet > players[i][_CURRENCY]:
                            bet = players[i][_CURRENCY]
                        dealersPot[i] = bet
                        players[i][_CURRENCY] -= bet

                    next_idx = bj_ante_player_index + 1
                    if next_idx < len(players):
                        gui_prepare_ante_for_player(next_idx)
                    else:
                        ShuffleDeck(STANDARDDECK)
                        shuffle_effect.play()

                        for i in range(len(players)):
                            if bj_use_card_integration:
                                CardIntegration(players[i][_CARDS], 2)
                            else:
                                DealCards(players[i][_CARDS], 2)
                                deal_effect.play()

                        DealCards(dealer[_CARDS], 2)
                        deal_effect.play()

                        gui_start_table_round()
                        bj_phase = BJ_PHASE_TABLE

            elif bj_phase == BJ_PHASE_TABLE:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bj_hit_rect.collidepoint(event.pos) and not bj_hit_clicked:
                        bj_hit_clicked = True
                        click_effect.play()
                        if (not bj_round_over) and len(players) > 0 and bj_current_player_index < len(players):
                            p = players[bj_current_player_index]
                            DealCards(p[_CARDS], 1)
                            deal_effect.play()
                            total = CardTotal(p[_CARDS])
                            if total > 21:
                                p[_RESULT] = "Bust"
                                bj_current_player_index += 1
                                gui_advance_after_player_action()

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    bj_hit_clicked = False

                if card_menu_option_is_clicked(bj_stand_option, event):
                    click_effect.play()
                    stand_effect.play()
                    if (not bj_round_over) and len(players) > 0 and bj_current_player_index < len(players):
                        p = players[bj_current_player_index]
                        p[_RESULT] = "Stand"
                        bj_current_player_index += 1
                        gui_advance_after_player_action()

                if card_menu_option_is_clicked(bj_new_round_option, event):
                    click_effect.play()
                    gui_reset_round_for_blackjack()
                    if len(players) > 0:
                        gui_prepare_ante_for_player(0)
                        bj_phase = BJ_PHASE_ANTE
                    else:
                        current_state = STATE_SETUP
                        setup_phase = SETUP_PHASE_NUM_PLAYERS

    # ---------- DRAW BASED ON STATE ----------
    if current_state == STATE_SETUP:
        draw_setup_screen(screen)
    elif current_state == STATE_MENU:
        draw_menu_screen(screen)
    elif current_state == STATE_BLACKJACK:
        draw_blackjack_screen(screen)
    elif current_state == STATE_RULES:
        draw_rules_screen(screen)
    elif current_state == STATE_POKER:
        draw_poker_wip_screen(screen)

    pygame.display.update()
    clock.tick(60)
    # heello