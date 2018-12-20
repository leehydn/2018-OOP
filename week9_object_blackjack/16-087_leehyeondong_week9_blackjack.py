#
# Blackjack Game, graphics version
#
image_path="./blackjack/"

import random
import time
import sys
from cs1graphics import *

FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace' ]
SUITS = [ 'Clubs', 'Diamonds', 'Hearts', 'Spades' ]
CARD_SIZE = (40, 80)
CARD_SIZE_X = CARD_SIZE[0]; 

# --------------------------------------------------------------------

class Card(object):
  """A card has a face and suit."""

  def __init__(self, face, suit):
    assert(face in FACES and suit in SUITS)
    self.face = face
    self.suit = suit
    face_str=face
    if(type(face)==int): face_str=str(face)
    self.image = Image(image_path+suit+"_"+face_str+".png") 
  
  def __str__(self):
    """Returns the string of a card (example : "8 of Diamonds") """
    return "{} of {}".format(self.face, self.suit)

  def value(self):
    """Returns the face value of the card."""
    value_dict = {
      "Ace": 11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
      "King": 10, "Queen": 10, "Jack": 10
    }
    
    return value_dict.get(self.face)
    
    
# --------------------------------------------------------------------

class Deck(object):
  """A deck of cards."""
  def __init__(self):
    """Create a deck of 52 cards and shuffle them."""
    self.cards = []
    for suit in SUITS:
      for face in FACES:
        self.cards.append(Card(face, suit))
    random.shuffle(self.cards)

  def draw(self):
    """Draw the top card from the deck."""
    return self.cards.pop()

class CardGraphics(object):
  """Graphical representation of a card."""
  
  def __init__(self, card, hidden = False): # card : Card object , hidden : True  if hidden card, False if visible card
    self.l = Layer()      #layer for a card image
    self.hidden = hidden  
     
    self.bg = Image(image_path+"Back.png") 
    if hidden:
      self.bg.setDepth(0)
      self.l.add(self.bg)

    self.l.add(card.image)
   

  def show(self):
    """make a hidden card visible"""
    self.bg.setDepth(100)
    
# --------------------------------------------------------------------

class Hand(object):
  """A hand of cards displayed on a table."""

  def __init__(self, x, y, canvas):
    """Create an empty hand displayed at indicated position on canvas."""
    self.canvas = canvas  
    self.x = x            
    self.y = y            
    self.graphics = []    
    self.hand = []          

  def clear(self):
    """Make hand empty."""
    for item in self.graphics:
      self.canvas.remove(item.l)
    self.graphics = []
    self.hand = []

  def add(self, card, hidden = False):
    """Add a new card to the hand."""
    # add a card 
    self.hand.append(card)
    # make a cardgraphics object
    card_g = CardGraphics(card, hidden)
    self.graphics.append(card_g)
    # calculate the animation position and depth  
    new_x = self.x + (len(self.hand)-1) * CARD_SIZE_X*0.4 + CARD_SIZE_X/2
    # append on the canvas to show the card image
    self.canvas.add(card_g.l)
    # make animation using moveTo
    card_g.l.moveTo(new_x, self.y)  
    
  def show(self):
    """Make a hidden card(first card) in his hand visible."""
    self.graphics[-1].show()
    

  def value(self):
    """
    His hand is a list including card objects
    Compute and return the total value of the cards in his hand
    """
    counter = 0
    for i in self.hand:
      counter += i.value()
    return counter
    

# --------------------------------------------------------------------

class Table(object):
  """A graphical Blackjack table for playing Blackjack."""
  
  def __init__(self):
    self.canvas = Canvas(600, 400, 'dark green', 'Black Jack')
    # The start position of player's card is (CARD_SIZE[0], CARD_SIZE[1])
    self.player = Hand(CARD_SIZE[0], CARD_SIZE[1], self.canvas) 
    # The start position of dealer's card is (CARD_SIZE[0], 3 * CARD_SIZE[1])
    self.dealer = Hand(CARD_SIZE[0], 3 * CARD_SIZE[1], self.canvas)

    self.score = [ Text(), Text() ]
    for i in range(2):
      self.score[i].setFontColor('white')
      self.score[i].setFontSize(20)
      self.score[i].moveTo(self.canvas.getWidth() - CARD_SIZE[0], CARD_SIZE[1])
      self.canvas.add(self.score[i])
    self.score[1].move(0, 2 * CARD_SIZE[1])

    self.message = Text()
    self.message.setFontColor('red')
    self.message.setFontSize(20)
    dim = self.message.getDimensions()
    self.message.moveTo(self.canvas.getWidth() / 2 - dim[0] / 2, 
                        self.canvas.getHeight() - 80)
    self.canvas.add(self.message)

    self.question = Text()
    self.question.setFontColor('white')
    self.question.setFontSize(20)
    dim = self.question.getDimensions()
    self.question.moveTo(self.canvas.getWidth() / 2 - dim[0] / 2, 
                        self.canvas.getHeight() - 40)
    self.canvas.add(self.question)
    
  def clear(self):
    """Clear everything on the table."""
    self.player.clear()
    self.dealer.clear()
    self.message.setMessage("")
    self.question.setMessage("")
    for i in range(2):
      self.score[i].setMessage("")

  def set_score(self, which, text):
    self.score[which].setMessage(text)
    
  def show_message(self, text):
    self.message.setMessage(text)

  def ask(self, prompt):
    self.question.setMessage(prompt)
    while True:
      e = self.canvas.wait()
      d = e.getDescription()
      if d == "canvas close":
        sys.exit(1)
      if d == "keyboard":
        key = e.getKey() 
        if key == 'y':
          self.question.setMessage(prompt+" "+key)
          time.sleep(0.5)
          return True
        if key == 'n':
          self.question.setMessage(prompt+" "+key)
          time.sleep(0.5)
          self.question.setMessage("")
          return False
  
  def close(self):
    """Close the table to end playing."""
    self.canvas.close()
    
# --------------------------------------------------------------------

def blackjack(table):
  """Play one round of Blackjack.
  Returns 1 if player wins, -1 if dealer wins, and 0 for a tie."""

  deck = Deck()
    
  # initial two cards
  table.player.add(deck.draw())
  table.dealer.add(deck.draw(), True) # deal the hidden card of dealer
  table.player.add(deck.draw())
  table.dealer.add(deck.draw())
  table.set_score(0, str(table.player.value()))

  # player's turn to draw cards
  while table.player.value() < 21:
    if not table.ask("Would you like another card?"):
      break
    
    table.player.add(deck.draw())
    table.set_score(0, str(table.player.value()))
  
  # if the player's score is over 21, the player loses immediately.
  if table.player.value() > 21:
    table.show_message("You went over 21! You lost!")
    table.dealer.show()  # make the hidden card of dealer visible
    return -1

  table.set_score(1, str(table.dealer.value()))
  while table.dealer.value() < 17:
    table.dealer.add(deck.draw())
    table.set_score(1, str(table.dealer.value()))

  player_total = table.player.value()
  dealer_total = table.dealer.value()

  if dealer_total > 21:
    msg = "The dealer went over 21! You win!"
    result = 1
  elif player_total > dealer_total:
    msg = "You win!"
    result = 1
  elif player_total < dealer_total:
    msg = "You lost!"
    result = -1
  else:
    msg = "You have a tie!"
    result = 0
    
  table.dealer.show()  # make the hidden card of dealer visible
  table.show_message(msg)
  return result

# --------------------------------------------------------------------

def game_loop():
  table = Table()
  while True:
    blackjack(table)    
    if not table.ask("Another round?"):
      break    
    table.clear()
  table.close()

game_loop()

# --------------------------------------------------------------------
