from collections import Counter

class Card(object):
    FACE_CARD_RANK = {'A': 14,
                      'K': 13,
                      'Q': 12,
                      'J': 11,
                      'T': 10}

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

    def two_of_a_kinds(self):
        return self.n_of_a_kinds(2)

    def is_two_pair(self):
        return len(self.two_of_a_kinds()) == 2

    def three_of_a_kind(self):
        return self.n_of_a_kinds(3)

    def four_of_a_kind(self):
        return self.n_of_a_kinds(4)

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

def get_highest_unique_card(h1, h2):
    print("call")
    print(h1.cards, h2.cards)
    if max(h1.cards) > max(h2.cards):
        return h1
    elif max(h2.cards) > max(h1.cards):
        return h2
    else:
        cards1 = [c for c in h1.cards if c.rank not in [max(h1.cards)]]
        cards2 = [c for c in h2.cards if c.rank not in [max(h2.cards)]]
        return get_highest_unique_card(PokerHand(cards1), PokerHand(cards2))

def determine_winner(hand1:PokerHand, hand2:PokerHand):
    functions = [PokerHand.is_royal_flush,
                 PokerHand.is_straight_flush,
                 PokerHand.four_of_a_kind,
                 PokerHand.is_full_house,
                 PokerHand.is_flush,
                 PokerHand.is_straight,
                 PokerHand.three_of_a_kind,
                 PokerHand.is_two_pair,
                 PokerHand.two_of_a_kinds]

    for f in functions:
        if f(hand1) or f(hand2):
            print('\n', f.__name__)
            print("Match!")
            if f(hand1) and f(hand2):
                print("Both had same match")
                if f is PokerHand.two_of_a_kinds or f is PokerHand.is_two_pair:
                    print("two of a kind function")
                    if max(hand1.two_of_a_kinds()) > max(hand2.two_of_a_kinds()):
                        print("hand 1 had higher pair")
                        return hand1

                    elif max(hand1.two_of_a_kinds()) == max(hand2.two_of_a_kinds()):
                        print("hands had same pair")
                        high_rem1 = max([c for c in hand1.cards if c.rank not in hand1.two_of_a_kinds()])
                        print("high_rem1", high_rem1)
                        high_rem2 = max([c for c in hand2.cards if c.rank not in hand2.two_of_a_kinds()])
                        print("high_rem2", high_rem2)

                        if high_rem1 > high_rem2:
                            return hand1
                        return hand2

                    else:
                        print("hand2 had higher pair")
                        return hand2

                elif f is PokerHand.is_full_house:
                    print("Full House Function")
                    if max(hand1.three_of_a_kind()) > max(hand2.three_of_a_kind()):
                        print("Hand1 has higher Threeofkind")
                        return hand1

                    # Assuming a 52 card deck, the three of a kind can never be the same.
                    # elif max(hand1.three_of_a_kind()) == max(hand2.three_of_a_kind()):
                    #     print("Both have same threeofkind")
                    #     if max(hand1.two_of_a_kinds()) > max(hand2.two_of_a_kinds()):
                    #         print("hand 1 had higher pair")
                    #         return hand1
                    #
                    #     elif max(hand1.two_of_a_kinds()) == max(hand2.two_of_a_kinds()):
                    #         print("hands had same pair")
                    #         high_rem1 = max([c for c in hand1.cards if c.rank not in hand1.two_of_a_kinds().extend(hand1.three_of_a_kind())])
                    #         print("high_rem1", high_rem1)
                    #         high_rem2 = max([c for c in hand2.cards if c.rank not in hand2.two_of_a_kinds().extend(hand2.three_of_a_kind())])
                    #         print("high_rem2", high_rem2)
                    #
                    #         if high_rem1 > high_rem2:
                    #             return hand1
                    #         return hand2
                    #
                    #     else:
                    #         print("hand2 had higher pair")
                    #         return hand2

                    else:
                        print("hand2 has higher threeofkind")
                        return hand2

                if hand1.high_card > hand2.high_card:
                    print("higher card in hand1")
                    print(hand1.high_card, hand2.high_card)
                    return hand1

                print("higher card in hand2")
                print(hand1.high_card, hand2.high_card)
                return hand2

            if hand1.is_straight_flush():
                print("only hand1 matched")
                return hand1

            print("only hand 2 matched")
            return hand2

    print("no matches, checking high card.")
    print(hand1.high_card, hand2.high_card)
    if hand1.high_card > hand2.high_card:
        return hand1

    return hand2

if __name__ == '__main__':
    with open(r"C:\GitHub\projectEuler\resources\p054_test_cases.txt", 'r') as file:
        hand1wins = 0
        for n, line in enumerate(file):
            all_cards = line.strip().split(' ')
            h1 = PokerHand([Card.from_txt(c) for c in all_cards[:5]])
            h2 = PokerHand([Card.from_txt(c) for c in all_cards[5:]])

            winner = determine_winner(h1, h2)

            print(get_highest_unique_card(h1,h2))

            if winner is h1:
                hand1wins += 1
                print(f"Hand 1 Wins deal {n + 1} (lineno)")

            else:
                print(f"Hand 2 Wins Deal {n + 1} (lineno)")

            print()
            print("="*20)
            print()

        print(hand1wins)