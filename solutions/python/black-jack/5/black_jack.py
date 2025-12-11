def value_of_card(card):
    face = "JQK"
    ace = "A"
    
    if card in face:
        return 10
    elif card == ace:
        return 1
    return int(card)

def higher_card(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
                                                 
    if valu1 > valu2:
        return card1
    elif valu1 < valu2:
        return card2
    return card1, card2

def value_of_ace(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
    total = valu1 + valu2
    
    if card1 == "A" or card2 == "A":
        return 1
    elif total <= 10:
        return 11
    return 1

def is_blackjack(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
    
    has_ace = "A" in (card1, card2)
    has_ten = 10 in (valu1, valu2)
    return has_ace and has_ten  
        
def can_split_pairs(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
    
    if valu1 == valu2 == 10:
        return True
    elif card1 == card2:
        return True
    return False

def can_double_down(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
    total = valu1 + valu2

    if 9 <= total <= 11:
        return True
    return False 
    
    