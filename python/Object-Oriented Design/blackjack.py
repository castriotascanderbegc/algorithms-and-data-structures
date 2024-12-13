"""
    Blackjack is a popular card game played in casinos. 
    The goal is to get a hand with a value as close to 21 as possible without going over.
    
    The player is dealt (or draws) two cards and can choose to draw more or stop. 
    The dealer is dealt two cards as well, but only one is visible to the player. 
    The player wins if their hand is closer to 21 than the dealer's hand. 
    But if they go over 21 they automatically lose. 
    If the player and dealer have the same value, it's a tie.


    Basics
        Only two players, including the dealer
        Only one deck of cards, which is refilled after each round
        We are implementing a gambling system for the non-dealer player
    Cards
        There are 52 cards in a deck
        Each card has a suit (hearts, spades, diamonds, clubs) and there are 13 cards in each suit
        A card could be numbered (2-10) and have the same point value: a face (jack, queen, king) and have a point value of 10
        an ace and have a point value of 1 or 11, whichever is better for the player
    Game Round
        To start each round, both the dealer and the player are dealt two cards
        One of the dealer's cards is hidden from the player
        The player can choose to draw one more card until they go over 21 or decide to stop
        If they go over 21, they lose and the round is over
        The dealer will draw until they have a hand value of N or more, where N is the player's hand value
        If the dealer goes over 21, the player wins
        At the end, if the dealer's hand value is greater than the player's, the dealer wins
    Gambling
        A player can start with an arbitrary amount of money
        The player can bet as much money as they have
        The dealer will never run out of money
"""

# Let's create a Suit - 4 distinct values
from enum import Enum
import random
class Suit(Enum):
    CLUBS, DIAMONDS, HEARTS, SPADES = 'clubs', 'diamonds', 'hearts', 'spades'

# A Card class will have a Suit and a Value
# Please, note for the sake of our example, the Suit of the Card will not be relevant. Will only focus on the real Value
class Card:
    # A card will have a suit and a value. The value will be a number between 1 and 10.
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value
    
    def getSuit(self):
        return self._suit
    
    def getValue(self):
        return self._value

    def print(self):
        print((self.getSuit(), self.getValue()))

# A Deck will have an array of Cards
# A Deck will be responsible for shuffling and drawing (popping) Cards
class Deck:
    # The deck will have an array of cards, and will be responsible for shuffling and drawing cards.
    # The simplest way to build the deck is to iterate 13 times for each suit.
    def __init__(self):
        self._cards = []

        for suit in Suit:
            for value in range(1, 14):
                self._cards.append(Card(suit, min(value, 10)))

    
    def print(self):
        for card in self._cards:
            card.print()
    
    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        for i in range(len(self._cards)):
            j = random.randint(1, 51)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]

# A hand will contain an array of cards, and the total score, which will be the sum of the values of the cards.
class Hand:
    def __init__(self):
        self._cards = []
        self._score = 0
    
    def addCard(self, card):
        self._cards.append(card)
        if card.getValue() == 1:    # to handle an ace
            self._score += 11 if self._score + 11 <= 21 else 1
        else:
            self._score += card.getValue()
        
        print('Score: ', self._score)

    def getCards(self):
        return self._cards
    
    def getScore(self):
        return self._score

    def print(self):
        for card in self.getCards():
            card.print()
            # print(card.getSuit(), card.getValue()

from abc import ABC, abstractmethod

# A Player could be either the User or the Delear since both will have a Hand
# A Player will be responsible for the Move --> Draw a Card or Stop drawing
# It is an Abstract Class
class Player(ABC):
    # A Player abstract class which has a Hand and can make a move.
    def __init__(self, hand):
        self._hand = hand
    
    def getHand(self):
        return self._hand
    
    def clearHand(self):
        self._hand = Hand()

    def addCard(self, card):
        self._hand.addCard(card)

    @abstractmethod
    def makeMove(self):
        pass

# The UserPlayer will be able to place a Bet based on a Balance he owns
class UserPlayer(Player):
    def __init__(self, balance, hand):
        # The UserPlayer will have a Balance and be able to place a Bet.
        super().__init__(hand)
        self._balance = balance
    
    def getBalance(self):
        return self._balance
    
    def placeBet(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient Funds")
        self._balance -= amount
        return amount
    
    def receiveWinnings(self, amount):
        self._balance += amount
    
    # It will also override makeMove() to prompt the user for input: returning true to draw a card and false to stop.
    def makeMove(self):
        if self.getHand().getScore() > 21:
            return False
        
        move = input("Draw card? [y/n] ")
        return move == 'y'

# The Dealer will be less involved since they don't need to place bets or receive winnings. 
# It will also override makeMove() but they will draw until their hand value is greater than or equal to some targetScore.
# In the our GameRound this targetScore will be the player's hand value.
class Dealer(Player):
    def __init__(self, hand):
        super().__init__(hand)
        self._targetScore = 17
    
    def updateTargetScore(self, score):
        self._targetScore = score

    def makeMove(self):
        return self.getHand().getScore() < self._targetScore

# The GameRound will be responsible for controlling the flow of the game. It must be provided a UserPlayer, Dealer, and Deck.
# It will also be responsible for prompting the user for a bet amount, dealing the initial cards, and cleaning up the round.
class GameRound:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck
    
    def getUserBet(self):
        amount = int(input("Enter the bet amount: "))
        return amount
    
    def dealInitialCards(self):
        for i in range(2):
            self._player.addCard(self._deck.draw())
            self._dealer.addCard(self._deck.draw())
        
        print("Player's hand")
        self._player.getHand().print()

        print("Dealer's first card")
        dealerCard = self._dealer.getHand().getCards()[0]
        dealerCard.print()
    
    def cleanupRound(self):
        self._player.clearHand()
        self._dealer.clearHand()
        print("Player's balance: ", self._player.getBalance())
    
    def play(self):
        self._deck.shuffle()

        if self._player.getBalance() <= 0:
            print('Player has no more money =)')
            return

        userBet = self.getUserBet()
        self._player.placeBet(userBet)

        self.dealInitialCards()

        # User makes moves
        while self._player.makeMove():
            drawnCard = self._deck.draw()
            print('Player draws', drawnCard.getSuit(), drawnCard.getValue())
            self._player.addCard(drawnCard)
            print('Player score: ', self._player.getHand().getScore())

        if self._player.getHand().getScore() > 21:
            print('Player busts!')
            self.cleanupRound()
            return
    
        # Dealer makes moves
        while self._dealer.makeMove():
            self._dealer.addCard(self._deck.draw())
        
        # determine winner
        if self._dealer.getHand().getScore() > 21 or self._player.getHand().getScore() > self._dealer.getHand().getScore():
            print('Player wins')
            self._player.receiveWinnings(userBet * 2)
        elif self._dealer.getHand().getScore() > self._player.getHand().getScore():
            print('Player loses')
        else:
            print('Game ends in a draw')
            self._player.receiveWinnings(userBet)
        self.cleanupRound()


player = UserPlayer(1000, Hand())
dealer = Dealer(Hand())

while player.getBalance() > 0:
    gameRound = GameRound(player, dealer, Deck()).play()



