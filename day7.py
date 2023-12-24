# Day 7: Camel Cards
# Make a function to interpret card, score the card type.

# Function to map the card with its respective letter used
def map_cards(hand):
    letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
    mapped_hand = []
    for card in hand:
        mapped_hand.append(letter_map.get(card, card))
    return mapped_hand

def classify_hand(hand):
    counts = [hand.count(card) for card in hand]
# Count from top to down since we care moreso about the highest value in the counts
    if 5 in counts:
        return 6
    elif 4 in counts:
        return 5
    elif 3 in counts:
        if 2 in counts:
            return 4
        else:
            return 3
    elif counts.count(2) == 4:
        return 2
    elif 2 in counts:
        return 1
    else:
        return 0
# Compute rank and plays here
def calculate_strength(hand):
    return classify_hand(hand), map_cards(hand)
plays, total = [], 0
# Read from the plays.
with open("input.txt", "r") as file:
    for line in file:
        hand, bid = line.split()
        plays.append((hand, int(bid)))
# Sort the plays with strongest first
plays.sort(key=calculate_strength)
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid
print(total)