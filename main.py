
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

#function to pick a random card
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

#function to return score
def calculate_score(card_list):
    score= sum(card_list)
    if 11 in card_list and score>21:
        score-=10
    if score==21:
        return 0
    else:
        return score


#picking 2 random cards each for the user and computer
user_cards=[deal_card(),deal_card()]
comp_cards=[deal_card(),deal_card()]

def check_blackjack():
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(comp_cards)
    if user_score>21 or comp_score==0:
        print (f'You lose!, your score exceeded 21.')
    elif user_score==0:
        print('You win! Blackjack!')
    else:
        check=input('Do you wish to draw another card?(y/n): ').lower()
        if check=='y':
            user_cards.append(deal_card())
            print(user_cards)
            check_blackjack()
        else:
            while comp_score < 17:
                comp_cards.append(deal_card())
                comp_score=calculate_score(comp_cards)
            compare(user_score,comp_score)

def compare(uscore,cscore):
    print(f'Your score is {uscore}')
    if uscore==cscore:
        print('It\'s a draw!')
    elif cscore==0 or uscore>21:
        print(f'You lose!, the dealer\'s score was {cscore}')
    elif uscore==0 or cscore>21:
        print(f'You win!, the dealer\'s score was {cscore}')
    else:
        if uscore>cscore:
            print(f'You win!, the dealer\'s score was {cscore}')
        else:
            print(f'You lose!, the dealer\'s score was {cscore}')



print('Your cards are:', user_cards)
print('The dealer has the card:', comp_cards[0])
check_blackjack()

