

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)


class Deck(list):
    def __init__(self):
        suits = ('spades', 'diamonds', 'clubs', 'hearts')
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        for s in suits:
            for r in ranks:
                self.append(Card(rank=r, suit=s))


def main():
    deck = Deck()
    assert deck
    assert len(deck) == 52
    assert Card(rank='2', suit='spades') == Card(rank='2', suit='spades')
    assert deck[0] == Card(rank='2', suit='spades')
    assert deck[:2] == [Card('2', 'spades'), Card('3', 'spades')]
    assert deck[12::13] == [Card('A', 'spades'), Card('A', 'diamonds'),
                            Card('A', 'clubs'), Card('A', 'hearts')]
    assert Card('Q', 'hearts') in Deck()

    deck[0] = None; assert deck[0] is None
    deck[:2] = [None, None]; assert deck[:2] == [None, None]


if __name__ == '__main__':
    main()