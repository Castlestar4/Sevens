from random import randint
from time import sleep
from os import system


def Upup(Up):
  if Up == 'X':
    return 0
  elif Up == 'K':
    return 6
  elif Up == 'Q':
    return 5
  elif Up == 'J':
    return 4
  elif Up == '10':
    return 3
  elif Up == '9':
    return 2
  elif Up == '8':
    return 1

def Downdown(Down):
  if Down == 0:
    return 0
  elif Down == 1:
    return 6
  elif Down == 2:
    return 5
  elif Down == 3:
    return 4
  elif Down == 4:
    return 3
  elif Down == 5:
    return 2
  elif Down == 6:
    return 1

def endChoice():
  correctInput = False
  while correctInput == False:
    answer = input ('Do you wish to continue? (y/n) ')
    if answer == 'n' or answer == 'No' or answer == 'no' or answer == 'N':
      playing = False
      correctInput = True
      gameMode = 'over'
    elif answer == 'y' or answer == 'Yes' or answer == 'yes' or answer == 'Y':
      gameMode = 'toTheEnd'
      playing = True
      correctInput = True
    else:
      print ('Incorrect input')
  return (playing, gameMode)


#Takes remaining cards and creates a hand with numebr of cards in hand given to it by main program
def MakeHand(Cards, cardsPerHand):
  from random import randint
  Hand = []
  for i in range (cardsPerHand):
    num = randint(0,(len(Cards)-1))
    Hand.append(Cards[num])
    del Cards[num]
  return(Hand)

def listPrint(lista):
  for i in range (0, (len(lista))):
    if i == (len(lista)-1):
      print (lista[i])
    else:
      print (lista[i], end = ', ')

#Takes the number of players and works out how many cards each hand gets
def FindCardsPerHand():
  print ('How many people would you like to play against?')
  good = False
  while good == False:
    Players = int(input('2, 3, 4, 5 or 6? '))
    if Players == 2:
      return 17, 3
      good = True
    if Players == 3:
      return 13, 4
      good = True
    if Players == 4:
      return 10, 5
      good == True
    if Players == 5:
      return 8, 6
      good == True
    if Players == 6:
      return 7, 7
      good = True

#Lays card given by program and deletes card from hand
def LayCard(card, hand, Diamonds, Clubs, Hearts, Spades):
  #Is it a seven?
  if card[1] == '7':
    if card[0] == 'D':
      Diamonds.append(card)
    elif card[0] == 'C':
      Clubs.append(card)
    elif card[0] == 'H':
      Hearts.append(card)
    elif card[0] == 'S':
      Spades.append(card)
  #Adding at start if it is less than seven
  if card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
    if card[0] == 'D':
      Diamonds.append(card)
    elif card[0] == 'C':
      Clubs.append(card)
    elif card[0] == 'H':
      Hearts.append(card)
    elif card[0] == 'S':
      Spades.append(card)
  elif int(card[1]) < 7 and int(card[-1]) != 0:
    if card[0] == 'D':
      Diamonds.insert(0,card)
    elif card[0] == 'C':
      Clubs.insert(0,card)
    elif card[0] == 'H':
      Hearts.insert(0,card)
    elif card[0] == 'S':
      Spades.insert(0,card)
  #Adding at end if it is more than 7
  elif int(card[1]) > 7 or (int(card[1]) == 1 and int(card[-1]) == 0):
    if card[0] == 'D':
      Diamonds.append(card)
    elif card[0] == 'C':
      Clubs.append(card)
    elif card[0] == 'H':
      Hearts.append(card)
    elif card[0] == 'S':
      Spades.append(card)
  #Deleting item from hand
  hand.remove(card)
  return(hand, Diamonds, Clubs, Hearts, Spades)

#Calcualtes the card number above the current one layed
def CalculateAbove(Card):
  num =  Card[-1]
  if num == '0':
    return 'J'
  elif num == 'J':
    return 'Q'
  elif num == 'Q':
    return 'K'
  elif num == 'K':
    return 'X'
  else:
    return str((int(num))+1)

def FindCard(CardNeeded, CtHand):
  found = False
  for i in range (0,len(CtHand)):  
    if CardNeeded == CtHand[i]:
      return True
  return False

#Laying a seven if have no other options
def FindaLay7(CtHand, Diamonds, Clubs, Hearts, Spades):
  seven = False
  if len(Spades) == 0:
    HaveCard = FindCard('S7', CtHand)
    if HaveCard == True:
      seven = True
      LayCard('S7', CtHand, Diamonds, Clubs, Hearts, Spades)
      print ('This computer lays S7')
  if len(Clubs) == 0 and seven == False:
    HaveCard = FindCard('C7', CtHand)
    if HaveCard == True:
      seven = True
      LayCard('C7', CtHand, Diamonds, Clubs, Hearts, Spades)
      print ('This computer lays C7')
  if len(Hearts) == 0 and seven == False:
    HaveCard = FindCard('H7', CtHand)
    if HaveCard == True:
      seven = True
      LayCard('H7', CtHand, Diamonds, Clubs, Hearts, Spades)
      print ('This computer lays H7')
  if seven == False:
    print ('This computer knocks')

#Finding Diamond options
def FindDiamondOptions(CtHand, Options, Diamonds):
  LowDiamond = False
  HighDiamond = False
  DiamondsLowCard = Diamonds[0]
  DiamondsLowNum = int(DiamondsLowCard[1]) - 1
  CardNeeded = 'D' + str(DiamondsLowNum)
  HaveCard = FindCard(CardNeeded, CtHand)
  if HaveCard == True:
    LowDiamond = True
    Options += 1
  DiamondsHighCard = Diamonds[-1]
  DiamondsHighNum = CalculateAbove(DiamondsHighCard)
  CardNeeded = 'D' + str(DiamondsHighNum)
  if CardNeeded != 'DX':
    HaveCard = FindCard(CardNeeded, CtHand)
    if HaveCard == True:
      Options += 1
      HighDiamond = True
  return (Options, HighDiamond, LowDiamond)

#FindingHeartOptions
def FindHeartOptions(CtHand, Options, Hearts):
  LowHeart = False
  HighHeart = False
  HeartsLowCard = Hearts[0]
  HeartsLowNum = int(HeartsLowCard[1]) - 1
  CardNeeded = 'H' + str(HeartsLowNum)
  HaveCard = FindCard(CardNeeded, CtHand)
  if HaveCard == True:
    LowHeart = True
    Options += 1
  HeartsHighCard = Hearts[-1]
  HeartsHighNum = CalculateAbove(HeartsHighCard)
  CardNeeded = 'H' + str(HeartsHighNum)
  if CardNeeded != 'HX':
    HaveCard = FindCard(CardNeeded, CtHand)
    if HaveCard == True:
      Options += 1
      HighHeart = True
  return(Options, HighHeart, LowHeart)

#Finding Clubs options
def FindClubOptions(CtHand, Options, Hearts):
  LowClub = False
  HighClub = False
  ClubsLowCard = Clubs[0]
  ClubsLowNum = int(ClubsLowCard[1]) - 1
  CardNeeded = 'C' + str(ClubsLowNum)
  HaveCard = FindCard(CardNeeded, CtHand)
  if HaveCard == True:
    LowClub = True
    Options += 1
  ClubsHighCard = Clubs[-1]
  ClubsHighNum = CalculateAbove(ClubsHighCard)
  CardNeeded = 'C' + str(ClubsHighNum)
  if CardNeeded != 'CX':
    HaveCard = FindCard(CardNeeded, CtHand)
    if HaveCard == True:
      Options += 1
      HighClub = True
  return (Options, HighClub, LowClub)

#FindingSpadeOptions
def FindSpadeOptions(CtHand, Options, Spades):
  LowSpade = False
  HighSpade = False
  SpadesLowCard = Spades[0]
  SpadesLowNum = int(SpadesLowCard[1]) - 1
  CardNeeded = 'S' + str(SpadesLowNum)
  HaveCard = FindCard(CardNeeded, CtHand)
  if HaveCard == True:
    LowSpade = True
    Options += 1
  SpadesHighCard = Spades[-1]
  SpadesHighNum = CalculateAbove(SpadesHighCard)
  CardNeeded = 'S' + str(SpadesHighNum)
  if CardNeeded != 'SX':
    HaveCard = FindCard(CardNeeded, CtHand)
    if HaveCard == True:
      Options += 1
      HighSpade = True
  return (Options, HighSpade, LowSpade)

def Strategy(Diamonds, Clubs, Hearts, Spades, Hand):
  Options = 0
  if len(Diamonds) > 0:
    Options, highDiamond, lowDiamond = FindDiamondOptions (Hand, Options, Diamonds)
    if highDiamond == True:
      DUp = CalculateAbove(Diamonds[-1])
      DUp = Upup(DUp)
    else:
      DUp = 0
    if lowDiamond == True:
      temp = Diamonds[0]
      DDown = int(temp[1])-1
      DDown = Downdown(DDown)
    else:
      DDown = 0
  else:
    lowDiamond = False
    DUp = 0
    DDown = 0
    highDiamond = False
  if len(Hearts) > 0:
    Options, highHeart, lowHeart = FindHeartOptions(Hand, Options, Hearts)
    if highHeart == True:
      HUp = CalculateAbove(Hearts[-1])
      HUp = Upup(HUp)
    else:
      HUp = 0
    if lowHeart == True:
      temp = Hearts[0]
      HDown = int(temp[1])-1
      HDown = Downdown(HDown)
    else:
      HDown = 0
  else:
    lowHeart = False
    HUp = 0
    HDown = 0
    highHeart = False
  if len(Clubs) > 0:
    Options, highClub, lowClub = FindClubOptions(Hand, Options, Clubs)
    if highClub == True:
      CUp = CalculateAbove(Clubs[-1])
      CUp = Upup(CUp)
    else:
      CUp = 0
    if lowClub == True:
      temp = Clubs[0]
      CDown = int(temp[1])-1
      CDown = Downdown(CDown)
    else:
      CDown = 0 
  else:
    highClub = False
    CUp = 0
    CDown = 0
    lowClub = False
  if len(Spades) > 0:
    Options, highSpade, lowSpade = FindSpadeOptions(Hand, Options, Spades)
    if highSpade == True:
      SUp = CalculateAbove(Spades[-1])
      SUp = Upup(SUp)
    else:
      SUp = 0
    if lowSpade == True:
      temp = Spades[0]
      SDown = int(temp[1])-1
      SDown = Downdown(SDown)
    else:
      SDown = 0
  else:
    lowSpade = False
    SUp = 0
    SDown = 0
    highSpade = False
    sleep(randint(1,3))
  if Options == 0:
    FindaLay7(Hand, Diamonds, Clubs, Hearts, Spades)
  else:
    StrategyList = []
    StrategyList.append(DUp)
    StrategyList.append(DDown)
    StrategyList.append(HUp)
    StrategyList.append(HDown)
    StrategyList.append(SUp)
    StrategyList.append(SDown)
    StrategyList.append(CUp)
    StrategyList.append(CDown)
    Max = 0
    MaxOption = 0
    for i in range (0, 8):
      if StrategyList[i] > Max:
        Max = StrategyList[i]
        MaxOption = i
    if MaxOption == 0:
      temp = CalculateAbove(Diamonds[-1])
      card = 'D' + temp
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 1:
      temp = Diamonds[0]
      below = int(temp[1]) -1
      card = 'D' + str(below)
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 2:
      temp = CalculateAbove(Hearts[-1])
      card = 'H' + temp
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 3:
      temp = Hearts[0]
      below = int(temp[1])-1
      card = 'H' + str(below)
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 4:
      temp = CalculateAbove(Spades[-1])
      card = 'S' + temp
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 5:
      temp = Spades[0]
      below = int(temp[1])-1
      card = 'S' + str(below)
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 6:
      temp = CalculateAbove(Clubs[-1])
      card ='C' + temp
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
    if MaxOption == 7:
      temp = Clubs[0]
      below = int(temp[1])-1
      card = 'C' + str(below)
      Hand, Diamonds, Clubs, Hearts, Spades = LayCard(card, Hand, Diamonds, Clubs, Hearts, Spades)
      print ('They layed', card)
  return (Hand, Diamonds, Clubs, Hearts, Spades)

# Set Up Hands
Hearts = []
Diamonds = []
Clubs = []
Spades = []
Cards = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK']
cardsPerHand, noPlayers = FindCardsPerHand()
Ct1Hand = MakeHand(Cards, cardsPerHand)
Ct2Hand = MakeHand(Cards, cardsPerHand)
Ct3Hand = []
Ct4Hand = []
Ct5Hand = []
Ct6Hand = []
if cardsPerHand == 13 or cardsPerHand == 10 or cardsPerHand == 7:
  Ct3Hand = MakeHand(Cards, cardsPerHand)
if cardsPerHand == 10:
  cardsPerHand = 11
  Ct4Hand = MakeHand(Cards, cardsPerHand)
if cardsPerHand == 8:
  cardsPerHand = 9
  Ct3Hand = MakeHand(Cards, cardsPerHand)
  Ct4Hand = MakeHand(Cards, cardsPerHand)
  Ct5Hand = MakeHand(Cards, cardsPerHand)
if cardsPerHand == 7:
  Ct4Hand = MakeHand(Cards, cardsPerHand)
  cardsPerHand = 8
  Ct5Hand = MakeHand(Cards, cardsPerHand)
  Ct6Hand = MakeHand(Cards, cardsPerHand)
PlayerHand = Cards
#Hands complete
#PlayerHand, Ct1,2,3,4,5,6Hand - based on number of players input by user
oneGo = 0
twoGo = 0

threeGo = 0

fourGo = 0

fiveGo = 0

sixGo = 0

D7Player = FindCard('D7', PlayerHand)
if D7Player == True:
  print ('You have the seven of diamonds!')
  playerPlacement = 1
  oneGo = 2
  twoGo = 3
  if noPlayers>3:
    threeGo = 4
    if noPlayers>4:
      fourGo = 5
      if noPlayers>5:
        fiveGo = 6
        if noPlayers>6:
          sixGo = 7
else:
#Determines when the user will take their go
  playerPlacement = randint(2, noPlayers)
  print ('Your go wil be number ', playerPlacement)
  oneSevenD = FindCard('D7', Ct1Hand)
  twoSevenD = FindCard('D7', Ct2Hand)
  if oneSevenD == True:
    oneGo = 1
    twoGo = 2
    if noPlayers>3:
      threeGo = 3
      if noPlayers>4:
        fourGo = 4
        if noPlayers>5:
          fiveGo = 5
          if noPlayers>6:
            sixGo =6
  elif twoSevenD == True:
    oneGo = 2
    twoGo = 1
    if noPlayers>3:
      threeGo = 3
      if noPlayers>4:
        fourGo = 4
        if noPlayers>5:
          fiveGo = 5
          if noPlayers>6:
            sixGo = 6
  else:
    threeSevenD = FindCard('D7', Ct3Hand)
    if threeSevenD == True:
      threeGo = 1
      oneGo = 2
      twoGo = 3
      if noPlayers>4:
        fourGo =4
        if noPlayers>5:
          fiveGo = 5
          if noPlayers>6:
            sixGo = 6
    else:
      fourSevenD = FindCard('D7', Ct4Hand)
      if fourSevenD == True:
        fourGo = 1
        oneGo = 2
        twoGo = 3
        threeGo = 4
        if noPlayers>5:
          fiveGo = 5
          if noPlayers>6:
            sixGo = 6
      else:
        fiveSevenD = FindCard('D7', Ct5Hand)
        if fiveSevenD == True:
          fiveGo = 1
          oneGo = 2
          twoGo = 3
          threeGo = 4
          fourGo = 5
          if noPlayers>6:
            sixGo = 6
        else:
          sixGo = 1
          oneGo = 2
          twoGo = 3
          threeGo = 4
          fourGo = 5
          fiveGo = 6
  if playerPlacement == oneGo:
    oneGo = noPlayers
  elif playerPlacement == twoGo:
    twoGo = noPlayers
  elif playerPlacement == threeGo:
    threeGo = noPlayers
  elif playerPlacement == fourGo:
    fourGo = noPlayers
  elif playerPlacement == fiveGo:
    fiveGo = noPlayers
  elif playerPlacement == sixGo:
    sixGo = noPlayers
input('Press enter to play ')
system('clear')

gameMode = 'Playing'
playing = True
count = 1
while playing == True:
  for i  in range (1,(noPlayers+1)):
    if playing == True:
      print ('Round ', count)
      listPrint(Diamonds)
      listPrint(Hearts)
      listPrint(Clubs)
      listPrint(Spades)
      print ('')
      print ('Your hand: ')
      listPrint(PlayerHand)
      print ('')
      sleep(0.5)
    x = True
    if gameMode == 'toTheEnd':
      if len(Diamonds) == 13 and len(Hearts) == 13 and len(Clubs) == 13 and len(Spades) == 13:
        x = False
        playing = False
      if oneGo == i and len(Ct1Hand) == 0 and playing == True:
        x = False
        print ('Player one has no cards left')
        input('Press enter ')
        system('clear')
      if twoGo == i and len(Ct2Hand) == 0 and playing == True:
        x = False
        print ('Player two has no cards left')
        input('Press enter ')
        system('clear')
      if threeGo == i and len(Ct3Hand) == 0 and playing == True:
        x = False
        print ('Player three has no cards left')
        input('Press enter ')
        system('clear')
      if fourGo == i and len(Ct4Hand) == 0 and playing == True:
        x = False
        print ('Player four has no cards left')
        input('Press enter ')
        system('clear')
      if fiveGo == i and len(Ct5Hand) == 0 and playing == True:
        x = False
        print ('Player five has no cards left')
        input('Press enter ')
        system('clear')
      if sixGo == i and len(Ct6Hand) == 0 and playing == True:
        print ('Player six has no cards left')
        input ('Press enter ')
        system('clear')
        x = False
      if playerPlacement == i and len(PlayerHand) == 0 and playing == True:
        x = False
        print ('You have no cards left!')
        input('Press enter ')
        system('clear')
    if x == True and gameMode != 'over':
      sleep (0.5)
      if oneGo == i:
        print ('It\'s player one\'s go!')
        if count == 1 and oneGo == 1:
          LayCard('D7', Ct1Hand, Diamonds, Clubs, Hearts, Spades)
          print ('They layed D7')
        else:
          Ct1Hand, Diamonds, Clubs, Hearts, Spades = Strategy(Diamonds, Clubs, Hearts, Spades, Ct1Hand)

      elif threeGo == i:
        print ('It\'s player three\'s go!')
        if count == 1 and threeGo == 1:
          LayCard('D7', Ct3Hand, Diamonds, Clubs, Hearts, Spades)
          print ('They layed D7')
        else:
          Ct3Hand, Diamonds, Clubs, Hearts, Spades = Strategy(Diamonds, Clubs, Hearts, Spades, Ct3Hand)
        
      elif twoGo == i:
        print ('It\'s player two\'s go!')
        if count == 1 and twoGo == 1:
          LayCard('D7', Ct2Hand, Diamonds, Clubs, Hearts, Spades)
          print ('They layed D7')
        else:
          Ct2Hand, Diamonds, Clubs, Hearts, Spades = Strategy(Diamonds, Clubs, Hearts, Spades, Ct2Hand)

      elif fourGo == i:
        print ('It\'s player four\'s go!')
        if count == 1 and fourGo == 1:
          LayCard('D7', Ct4Hand, Diamonds, Clubs, Hearts, Spades)
          print ('They layed D7')
        else:
          Ct4Hand, Diamonds, Clubs, Hearts, Spades = Strategy(Diamonds, Clubs, Hearts, Spades, Ct4Hand)

      elif fiveGo == i:
        print ('It\'s player four\'s go!')
        if count == 1 and fiveGo == 1:
          LayCard('D7', Ct5Hand, Diamonds, Clubs, Hearts, Spades)
          print ('They layed D7')
        else:
          Ct5Hand, Diamonds, Clubs, Hearts, Spades = Strategy(Diamonds, Clubs, Hearts, Spades, Ct5Hand)

      elif sixGo == i:
        print ('It\'s player four\'s go!')
        if count == 1 and sixGo == 1:
          LayCard('D7', Ct6Hand, Diamonds, Clubs, Hearts, Spades)
          print ('They layed D7')
        else:
          Ct6Hand, Diamonds, Clubs, Hearts, Spades = Strategy(Diamonds, Clubs, Hearts, Spades, Ct6Hand)
            
      elif playerPlacement == i:
        print ('Your go!')
        sleep(1)
        print ('\n')
        cardInHand = False
        CanLay = False
        sevenp = False
        if count == 1 and  playerPlacement == 1:
          print ('You lay D7')
          LayCard('D7', PlayerHand, Diamonds, Clubs, Hearts, Spades)
          cardInHand = True
          CanLay = True
          sevenp = True
          input('Press enter ')
        while cardInHand == False or CanLay == False:
          CanLay = False
          cardInHand = False
          chosenCard = input('Please enter the card you wish to lay: (type \'k\' if you cannot lay) ')
          if chosenCard != 'k':
            cardInHand = FindCard(chosenCard, PlayerHand)
          if cardInHand == False and chosenCard != 'k':
            print ('You don\'t seem to have this card - enter again')
          if cardInHand == True:
            if chosenCard[1] == '7':
              CanLay = True
            elif chosenCard[0] == 'D' and len(Diamonds)>0:
              a = CalculateAbove(Diamonds[-1])
              low = Diamonds[0]
              b = int(low[1])-1
              if a == '10':
                a = '0'
              if a == chosenCard[-1]:
                CanLay = True
              elif str(b) == str(chosenCard[1]):
                CanLay = True
            elif chosenCard[0] == 'C' and len(Clubs)>0:
              c = CalculateAbove(Clubs[-1])
              low = Clubs[0]
              d = int(low[1])-1
              if c == '10':
                c = '0'
              if c == chosenCard[-1]:
                CanLay = True
              elif str(d) == str(chosenCard[1]):
                CanLay = True
            elif chosenCard[0] == 'H' and len(Hearts)>0:
              e = CalculateAbove(Hearts[-1])
              low = Hearts[0]
              f = int(low[1])-1
              if e == '10':
                e = '0'
              if e == chosenCard[-1]:
                CanLay = True
              elif str(f) == str(chosenCard[1]):
                CanLay = True
            elif chosenCard[0] == 'S' and len(Spades)>0:
              g = CalculateAbove(Spades[-1])
              low = Spades[0]
              h = int(low[1])-1
              if g == '10':
                g = '0'
              if g == chosenCard[-1]:
                CanLay = True
              elif str(h) == str(chosenCard[1]):
                CanLay = True
            if CanLay == False and chosenCard != 'k':
              print ('It doesn\'t look like you can lay that card, try again')
          if chosenCard == 'k':
            CanLay = True
            cardInHand = True
        if sevenp == False:
          if chosenCard != 'k':
            LayCard(chosenCard, PlayerHand, Diamonds, Clubs, Hearts, Spades)
      
      #Game over
      if len(PlayerHand) == 0 and gameMode == 'Playing':
        sleep (3)
        system('clear')
        sleep (1)
        print ('You win!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2
      if len(Ct1Hand) == 0 and gameMode == 'Playing':
        sleep(3)
        system ('clear')
        sleep (1)
        print ('Player one wins!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2
      if len(Ct2Hand) == 0 and gameMode == 'Playing':
        sleep(3)
        system('clear')
        sleep(1)
        print ('Player two wins!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2
      if len(Ct3Hand) == 0 and gameMode == 'Playing' and threeGo != 0:
        sleep (3)
        system('clear')
        sleep (1)
        print ('Player three wins!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2
      if len(Ct4Hand) == 0 and gameMode == 'Playing' and fourGo != 0:
        sleep (3)
        system('clear')
        sleep (1)
        print ('Player four wins!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2
      if len(Ct5Hand) == 0 and gameMode == 'Playing' and fiveGo != 0:
        sleep (3)
        system('clear')
        sleep (1)
        print ('Player five wins!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2
      if len(Ct6Hand) == 0 and gameMode == 'Playing' and sixGo != 0:
        sleep (3)
        system('clear')
        sleep (1)
        print ('Player six wins!')
        sleep (1)
        playing, gameMode = endChoice()
        if gameMode == 'over':
          i = noPlayers + 2

      if playerPlacement != i:
        input('Press enter ')
      system ('clear')
  count = count + 1
sleep (1)
system('clear')
print ('Good game!')
