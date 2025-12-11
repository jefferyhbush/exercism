def value_of_card(card):
    face = "JQK"
    ace = "A"
    
    if card in face:
        return 10
    if card == ace:
        return 1
    return int(card)

def higher_card(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
                                                 
    if valu1 > valu2:
        return card1
    if valu1 < valu2:
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
    
    return "A" in (card1, card2) and 10 in (valu1, valu2)
        
def can_split_pairs(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)

    return valu1 == valu2 == 10 or card1 == card2

def can_double_down(card1, card2):
    valu1, valu2 = value_of_card(card1), value_of_card(card2)
    total = valu1 + valu2

    return 9 <= total <= 11 
    
    