from collections import Counter

class Card(object):
    FACE_CARD_RANK = {'A': 14,
                      'K': 13,
                      'Q': 12,
                      'J': 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @classmethod
    def from_txt(cls, name):
        suit = name[1]
        try:
            rank = int(name[0])
        except ValueError:
            rank = Card.FACE_CARD_RANK[name[0]]

        return Card(suit, rank)

    def __str__(self):
        return "".join([str(self.rank), self.suit])

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.rank < other.rank

class PokerHand(object):
    def __init__(self, cards):
        self.cards = cards

    @property
    def high_card(self):
        # return max([card.rank for card in self.cards])
        return max(self.cards)

    def n_of_a_kinds(self, n):
        ranks = [c.rank for c in self.cards]
        return [r for r, m in Counter(ranks).items() if m == n]

    def is_straight(self):
        s = self.sorted_hand()
        for i, card in enumerate(s):
            if i == 0:
                continue
            if not card.rank == s[i-1].rank + 1:
                return False

        return True

    def is_flush(self):
        if Counter(self.suits).most_common(1)[0][1] == 5:
            return True

        return False

    def is_straight_flush(self):
        if self.is_straight() and self.is_flush():
            return True

        return False

    def is_full_house(self):
        if self.n_of_a_kinds(2) and self.n_of_a_kinds(3):
            return True

        return False

    def is_royal_flush(self):
        if self.is_straight_flush() and sorted(self.ranks) == [10,11,12,13,14]:
            return True

        return False

    @property
    def suits(self):
        return [c.suit for c in self.cards]

    @property
    def ranks(self):
        return [c.rank for c in self.cards]

    def sorted_hand(self):
        s = sorted(self.cards)
        return s


def determine_winner(hand1:PokerHand, hand2:PokerHand):
    winner = None

    # Rules dont specify who wins in the event of two royal flushes, so assume that won't happen
    if hand1.is_royal_flush():
        return hand1
    if hand2.is_royal_flush():
        return hand2

    if hand1.is_straight_flush():
        if hand2.is_straight_flush():
            if hand1.high_card > hand2.high_card:
                return hand1

            return hand2

        return hand1

    if hand1.n_of_a_kinds(4):
        if hand2.n_of_a_kinds(4):
            if hand1.high_card > hand2.high_card:
                return hand1

            return hand2

        return hand1

    if hand1.is_full_house():
        if hand2.is_full_house():
            if hand1.high_card > hand2.high_card:
                return hand1

            return hand2

        return hand1

    if hand1.is_flush():
        if hand2.is_flush():
            if hand1.high_card > hand2.high_card:
                return hand1

            return hand2

        return hand1

    if hand1.is_straight():
        if hand2.is_straight():
            if hand1.high_card > hand2.high_card:
                return hand1

            return hand2

        return hand1

    if hand1.n_of_a_kinds(3):
        if hand2.n_of_a_kinds(3):
            if hand1.high_card > hand2.high_card:
                return hand1

            return hand2

        return hand1

if __name__ == '__main__':
    cards = [Card('H', 10),
             Card('H', 12),
             Card('H', 14),
             Card('H', 13),
             Card('D', 11)]
    hand = PokerHand(cards)
    print(hand.cards)
    print(hand.sorted_hand())
    print("High Card:", hand.high_card)
    print("Two of a Kind:", hand.n_of_a_kinds(2))
    print("Straight", hand.is_straight())
    print("Flush", hand.is_flush())
    print("Full House", hand.is_full_house())
    print("Straight Flush", hand.is_straight_flush())
    print("Royal Flush", hand.is_royal_flush())