import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.get_value()

    def get_value(self):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards[:len(self.cards)//2], self.cards[len(self.cards)//2:]

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def add_cards(self, cards):
        self.deck.extend(cards)

    def play_card(self):
        return self.deck.pop(0) if self.deck else None

    def has_cards(self):
        return bool(self.deck)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        half1, half2 = self.deck.deal()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.player1.add_cards(half1)
        self.player2.add_cards(half2)
        
    def play_round(self):
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()
        if not card1 or not card2:
            return False  # Game over

        print(f"{self.player1.name} plays {card1}, {self.player2.name} plays {card2}")

        if card1.value > card2.value:
            print(f"{self.player1.name} wins the round!")
            self.player1.add_cards([card1, card2])
        elif card1.value < card2.value:
            print(f"{self.player2.name} wins the round!")
            self.player2.add_cards([card1, card2])
        else:
            print("War!")
            # self.handle_war([card1, card2])

        return True
    
    def handle_war(self, war_pile):
        ...
        
    def play_game(self):
        round_count = 0
        while self.player1.has_cards() and self.player2.has_cards():
            print(f"\nRound {round_count + 1}")
            if not self.play_round():
                break
            round_count += 1

        if self.player1.has_cards():
            print(f"{self.player1.name} wins the game!")
        elif self.player2.has_cards():
            print(f"{self.player2.name} wins the game!")
        else:
            print("The game is a draw!")

if __name__ == "__main__":
    game = Game()
    game.play_game()