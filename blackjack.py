"""
HW 6 blackjack.

From class.

Author: Frankie Benedetto
Version: 10/19/22
"""


cards = ('0', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10')
face_cards = ('J', 'Q', 'K')


def get_value(card):
    """Gets a card.

    Finds the value .
    
    Args:
        card (int): its the card.
        
    Returns:
        value (int): just returns the value of the card. 
    """
    if card in face_cards:
        value = 10
        
    elif card in cards:
        value = cards.index(card)
        
    return value


def dealer_hits(c1, c2):
    """Gives the dealer his two cards.

    Determines to hit or not.
    
    Args:
        c1 (str): card 1.
        c2 (str): card 2.
        
    Returns:
        hit (str): to hit or to not hit?.
        false (bool): true or false
        true (bool): true or false
    """
    if c1 == 'A' or c2 == 'A':
        if c1 in face_cards:
            return False
        if c2 in face_cards:
            return False
        
    if get_value(c1) + get_value(c2) >= 17:
        hit = False
        
    elif get_value(c1) + get_value(c2) < 17:
        hit = True
        
    return hit
