def value_of_card(card):
    face = "JQK"
    ace = "A"
    
    if card in face:
        return 10
    elif card == ace:
        return 1
    return int(card)

def higher_card(card_one, card_two):
    w, z = value_of_card(card_one), value_of_card(card_two)
                                                 
    if w > z:
        return card_one
    elif w < z:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    w, z = value_of_card(card_one), value_of_card(card_two)
    total = w + z
    
    if card_one == "A" or card_two == "A":
        return 1
    elif total <= 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    w, z = value_of_card(card_one), value_of_card(card_two)
    
    if card_one == "A" and z == 10:
        return True
    elif w == 10 and card_two == "A":
        return True
    return False    
        
def can_split_pairs(card_one, card_two):
    w, z = value_of_card(card_one), value_of_card(card_two)
    
    if w == z == 10:
        return True
    elif card_one == card_two:
        return True
    return False

def can_double_down(card_one, card_two):
    w, z = value_of_card(card_one), value_of_card(card_two)
    total = w + z

    if 9 <= total <= 11:
        return True
    return False
    