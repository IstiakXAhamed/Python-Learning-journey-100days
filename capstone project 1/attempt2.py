import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of the given cards."""
    score = sum(cards)
    ace_count = cards.count(11)
    
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    
    return score

playContinue = True

while playContinue:
    moreBlkjk = input("Do you want to have another game of Blackjack?, y or n? ")
    
    if moreBlkjk == "y":
        myCards = [deal_card(), deal_card()]
        pcCards = [deal_card(), deal_card()]

        takeCard = True

        while takeCard:
            myScore = calculate_score(myCards)
            pcScore = calculate_score(pcCards)

            print(f"Your Cards: {myCards}, current score: {myScore}")
            print(f"Computer's first card: {pcCards[0]}")

            if myScore == 21 or myScore > 21:
                takeCard = False
            else:
                morePlay = input("y for getting more card, n for stop! ")
                if morePlay == "y":
                    myCards.append(deal_card())
                else:
                    takeCard = False

        myScore = calculate_score(myCards)  # Recalculate after player's turn

        # Computer's turn
        while pcScore < 17 and myScore <= 21:  # Computer keeps drawing until it reaches 17 or higher
            pcCards.append(deal_card())
            pcScore = calculate_score(pcCards)

        print(f"Your final hand: {myCards}, final score: {myScore}")
        print(f"Computer's final hand: {pcCards}, final score: {pcScore}")

        if myScore > 21:
            print("You went over 21. You lose!")
        elif pcScore > 21:
            print("Computer went over 21. You win!")
        elif myScore > pcScore:
            print("You win!")
        elif myScore < pcScore:
            print("You lose!")
        else:
            print("It's a draw!")

    elif moreBlkjk == "n":
        playContinue = False
