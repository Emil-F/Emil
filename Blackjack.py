import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    hand = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards), random.choice(cards)]
    total_hand = sum(hand)
    total_dealer = sum(dealer)
    print(f"    You cards: {hand}, current score: {total_hand}")
    print(f"    Computer's first card: {dealer[0]}")
    done = False
    if total_hand > 21:
        print("You lose.")
    else:
        while not done:
            end = False
            while not end:
                another = input("Type 'y' to hit, type 'n' to stand: ").lower()
                if another == "y":
                    hand += [random.choice(cards)]
                    total_hand = sum(hand)
                    if total_hand > 21:
                        print(f"    Your final hand: {hand}, final score: {total_hand}")
                        print(f"    Computer's final hand: {dealer}, final score: {total_dealer}")
                        print("\n    Bust. You lose.")
                        done = True
                        end = True
                    else:
                        print(f"    You cards: {hand}, current score: {total_hand}")
                        print(f"    Computer's first card: {dealer[0]}")
                else:
                    if total_dealer == total_hand:
                        done = True
                        end = True
                    else:
                        while total_dealer < total_hand:
                            dealer += [random.choice(cards)]
                            total_dealer = sum(dealer)
                        print(f"    Your final hand: {hand}, final score: {total_hand}")
                        print(f"    Computer's final hand: {dealer}, final score: {total_dealer}")
                        done = True
                        end = True
        if total_dealer > total_hand and not total_dealer > 21:
            print("\n    Computer wins.")
        elif total_dealer > 21:
            print("\n    Dealer busts. You win.")
        elif total_dealer == total_hand:
            print("\n    Its a draw.")
    
def blackjack():
    end = False
    while not end:
        blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if blackjack == "y":
            deal_cards()
        else:
            end = True

blackjack()