def value_of_card(card):
    
    if card in "JQK":
        return 10
    return 1 if card == "A" else int(card)

def higher_card(card1, card2):
    is_pair = can_split_pairs(card1, card2)
    value1, value2 = value_of_card(card1), value_of_card(card2)
                                                 
    if is_pair:
         return card1, card2
    return card1 if value1 > value2 else card2

def value_of_ace(card1, card2):
    value1, value2 = value_of_card(card1), value_of_card(card2)
    total = value1 + value2
    
    if card1 == "A" or card2 == "A":
        return 1
    return 11 if total <= 10 else 1

def is_blackjack(card1, card2):
    value1, value2 = value_of_card(card1), value_of_card(card2)
    
    return "A" in (card1, card2) and 10 in (value1, value2)
        
def can_split_pairs(card1, card2):
    value1, value2 = value_of_card(card1), value_of_card(card2)

    return value1 == value2

def can_double_down(card1, card2):
    value1, value2 = value_of_card(card1), value_of_card(card2)
    total = value1 + value2

    return 9 <= total <= 11 