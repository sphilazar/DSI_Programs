# coding: utf-8
import random

class Card:
  def __init__(self, rank, suit):
    suit_chars = {'spade':'♠', 'heart':'♥', 'diamond':'♦', 'club':'♣'}
    
    if suit not in suit_chars.values():
      suit = suit_chars[suit.lower()]
    
    self.rank = rank
    self.suit = suit
    
  def __repr__(self):
    return "<Card: %s>"%( self.rank+self.suit )


class Deck:
  def __init__(self):
    self.cards = []
    
    for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
      for face in ['♠','♥','♦','♣']:
        self.cards.append( Card(rank, face) )
        
  def shuffle(self):
    random.shuffle(self.cards)
    
  def __len__(self):
    return len(self.cards)

  def showcards(self):
    for card in self.cards:
        print(card.rank + card.suit)

  def hascards(self):
    if self.cards:
        return True
    return False

  def playcard(self):
    return self.cards[0]

  def reset(self,n=1):
    self.cards = self.cards[n:]

def winnerloser(w,l,index=1):
    print(w.cards[index-1].rank + w.cards[index-1].suit + ' beats ' + l.cards[index-1].rank + l.cards[index-1].suit)
    w.cards += w.cards[:index]
    w.cards += l.cards[:index]

def islarger(c1,c2):
    faces = {'J':'10','Q':'11','K':'12','A':'13'}
    rank1 = c1.rank
    rank2 = c2.rank
    if c1.rank in faces:
        rank1 = faces.get(c1.rank)
    if c2.rank in faces:
        rank2 = faces.get(c2.rank)
    if int(rank1) > int(rank2):
        return True
    elif int(rank2) > int(rank1):
        return False

def war(p1,p2,n=1):
    print('War!')
    index = (4*n)-1
    if index >= len(p1.cards) or index >= len(p2.cards):
        index = min(len(p1.cards)-1,len(p2.cards)-1)
        return index
    print(p1.cards[index].rank + p1.cards[index].suit + ' vs. ' + p2.cards[index].rank + p2.cards[index].suit)
    if p1.cards[index].rank == p2.cards[index].rank and (p1.hascards() and p2.hascards()):
        n += 1
        return war(p1,p2,n)
    elif islarger(p1.cards[index],p2.cards[index]):
        winnerloser(p1,p2,index+1)
        return index
    else:
        winnerloser(p2,p1,index+1)
        return index

def play(p1,p2,wars=0):
    c1 = p1.playcard()
    c2 = p2.playcard()
    if c1.rank == c2.rank:
        print(p1.cards[0].rank + p1.cards[0].suit + ' ties with ' + p2.cards[0].rank + p2.cards[0].suit)
        wars += 1
        index = war(p1,p2)
        p1.reset(index+1)
        p2.reset(index+1)
    elif islarger(c1,c2):
        winnerloser(p1,p2)
        p1.reset()
        p2.reset()
    else:
        winnerloser(p2,p1)
        p1.reset()
        p2.reset()
    return wars

# main  
turn_data = []
war_data = []
trials = input('How many times do you want to play war?: ')

while len(turn_data) < trials:
    p1 = Deck()
    p2 = Deck()
    p1.shuffle()
    p2.cards = p1.cards[26:]
    p1.cards = p1.cards[:26]
    p1.showcards()
    p2.showcards()
    turns = 0
    wars = 0
    while p1.hascards() and p2.hascards():    
        print('Player 1 has '+ str(len(p1.cards)) + ' cards.')
        print('Player 2 has '+ str(len(p2.cards)) + ' cards.')
        wars = play(p1,p2,wars)
        turns += 1
    print('This game lasted '+ str(turns) + ' turns.')
    print('This game had '+ str(wars) + ' wars.')
    turn_data.append(turns)
    war_data.append(wars)
print(turn_data)
print('Average turns in ' + str(trials) + ' trials: ' + str(sum(turn_data)/len(turn_data)))
print(war_data)
print('Average wars in ' + str(trials) + ' trials: ' + str(sum(war_data)/len(war_data)))
