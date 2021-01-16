import copy




class Card:
    ## Initializes a card instance
    def __init__(self, name):
        self._name = name
        self._playerList = []
        self._solved = False

    ## Returns the card's name    
    def name(self):
        return self._name

    ## Returns a list of players that may have the card
    def playerList(self):
        return self._playerList

    ## Sets self._players to players
    def set_players(self, players):
        self._playerList = players

    ## Removes a player from self._players
    def remove(self, player):
        if player in self._playerList:
            self._playerList.remove(player)
            if len(self._playerList) == 0:
                print('\n' + f'{self._name} is the solution')

    ## Sets self._players to a list with a single player  
    def set(self, player):
        self._playerList = [player]
        self._solved = True
        print('\n' + f'{player} has {self._name}')

    ## Prints self._players
    def __str__(self):
        if self._solved == False:
            return (f'{str(self._name):>15}: {self._playerList}')
        else:
            return (f'{str(self._name):>15}: {self._playerList[0].upper()}')


class Player:
    ## Initializes a player instance
    def __init__(self, name):
        self._name = name
        self._sets = []

    ## Returns the name of the player
    def name(self):
        return self._name

    ## Returns the list of sets a player has
    def sets(self):
        return self._sets

    ## Adds a set to self._sets
    def addSet(self, sets):
        self._sets.append(sets)

    ## Removes a set from self._sets
    def removeFromSet(self, i, card):
        self._sets[i].remove(card)

    ## Changes the set at index i in self._sets to []
    def eraseSet(self, i):
        self._sets[i] = []




## Creating all data
## Dictionary of cards, with each card instance as values and card names as keys
cards = {}

mustard = Card('mustard')
cards['mustard'] = mustard
plum = Card('plum')
cards['plum'] = plum
green = Card('green')
cards['green'] = green
peacock = Card('peacock')
cards['peacock'] = peacock
scarlet = Card('scarlet')
cards['scarlet'] = scarlet
white = Card('white')
cards['white'] = white
knife = Card('knife')
cards['knife'] = knife
candlestick = Card('candlestick')
cards['candlestick'] = candlestick
revolver = Card('revolver')
cards['revolver'] = revolver
rope = Card('rope')
cards['rope'] = rope
lead = Card('lead')
cards['lead'] = lead
wrench = Card('wrench')
cards['wrench'] = wrench
hall = Card('hall')
cards['hall'] = hall
lounge = Card('lounge')
cards['lounge'] = lounge
dining = Card('dining')
cards['dining'] = dining
kitchen = Card('kitchen')
cards['kitchen'] = kitchen
ballroom = Card('ballroom')
cards['ballroom'] = ballroom
conservatory = Card('conservatory')
cards['conservatory'] = conservatory
billiard = Card('billiard')
cards['billiard'] = billiard
library = Card('library')
cards['library'] = library
study = Card('study')
cards['study'] = study


## Dictionary of players, with player instances as values and player names as keys
playerDict = {}
allPlayers = []

player1 = Player('player1')
playerDict['player1'] = player1
allPlayers.append('player1')
player2 = Player('player2')
playerDict['player2'] = player2
allPlayers.append('player2')
player3 = Player('player3')
player4 = Player('player4')
player5 = Player('player5')


## List of all valid card inputs
cardInputs = ['done', 'back']
for words in cards:
    cardInputs.append(words)


## List of all valid player inputs
playerInputs = ['done', 'back', 'show', 'over', 'none', 'player1', 'player2']

        
## Prints the list of cards with each player that may have the card
def show():
    print('\n\n')
    for items in cards:
        print(cards[items])
    print('\n\n')


## Gets a user input and ensures that it is valid, depending on the type of input
## Str, Str -> Str
def userInput(text, typeOfInput):
    data = input(text)
    if typeOfInput == 'player':
        while data not in playerInputs:
            data = input('invalid input. Try again')
    if typeOfInput == 'card':
        while data not in cardInputs:
            data = input('invalid input. Try again')
    if typeOfInput == 'whoIsSuggesting':
        while data not in playerInputs and data!='me':
            data = input('invalid input. Try again')
    if typeOfInput == 'numPlayers':
        data = int(data)
        while (data < 3 or data > 6):
            data = int(input('invalid input. Try again'))
    return data


## A calculation function that checks the must-have list after updating the can-have. Loop until no changes are made to the can-have list
def calculate():
    changed = True
    while changed == True:
        changed = False
        for player in playerDict:
            for i in range (len(playerDict[player].sets())):
                for items in playerDict[player].sets()[i]:
                    if player not in cards[items].playerList():
                        playerDict[player].removeFromSet(i, items)
                        if len(playerDict[player].sets()[i]) == 1:
                            cards[playerDict[player].sets()[i][0]].set(player)
                            changed = True
                            playerDict[player].eraseSet(i)




## Main
## Setting up number of players
numPlayers = userInput("How many people are playing?", "numPlayers")
if numPlayers >= 4:
    playerDict['player3'] = player3
    allPlayers.append('player3')
    playerInputs.append('player3')
if numPlayers >= 5:
    playerDict['player4'] = player4
    allPlayers.append('player4')
    playerInputs.append('player4')
if numPlayers == 6:
    playerDict['player5'] = player5
    allPlayers.append('player5')
    playerInputs.append('player5')

for card in cards:
    cards[card].set_players(copy.copy(allPlayers))


## Setting up the user's cards. Type done when finished
done = False
while done == False:
    card = userInput('enter your card', 'card')
    if card == 'done':
        done = True
    else:
        cards[card].set('me')


## Input suggestions. Type over when game ends, and show to print all info so far
over = False
while over == False:
    back = True
    playerSuggesting = userInput('Who is suggesting?', 'whoIsSuggesting')
    if playerSuggesting == 'over':
        over = True
    elif playerSuggesting == 'show':
        show()
    elif playerSuggesting == 'me':
        while back == True:
            back = False
            players = copy.copy(allPlayers)
            c1 = userInput('what card did you suggest?', 'card')
            p1 = userInput('which player showed you that card?', 'player')
            c2 = userInput('what card did you suggest?', 'card')
            p2 = userInput('which player showed you that card?', 'player')
            c3 = userInput('what card did you suggest?', 'card')
            p3 = userInput('which player showed you that card?', 'player')
            if c1 == 'back' or  c2 == 'back' or c3 == 'back' or p1 == 'back' or p2 == 'back' or p3 == 'back':
                back = True
        if p1 != 'none':
            cards[c1].set(p1)
            players.remove(p1)
        if p2 != 'none':
            cards[c2].set(p2)
            players.remove(p2)
        if p3 != 'none':
            cards[c3].set(p3)
            players.remove(p3)
        if p1 == 'none':
            for items in players:
                cards[c1].remove(items)
        if p2 == 'none':
            for items in players:
                cards[c2].remove(items)
        if p3 == 'none':
            for items in players:
                cards[c3].remove(items)
        calculate()
        print('\n')
        
    else:
        know1Card = False
        while back == True:
            players = copy.copy(allPlayers)
            players1 = []
            players.remove(playerSuggesting)
            back = False
            c1 = userInput('which card was suggested', 'card')
            c2 = userInput('which card was suggested', 'card')
            c3 = userInput('which card was suggested', 'card')
            if c1 == 'back' or c2 == 'back' or c3 == 'back':
                back = True
            done = False
            while done == False:
                revealingPlayer = userInput('which player revealed a card', 'player')
                if revealingPlayer == 'back':
                    back = True
                elif revealingPlayer == 'done' or revealingPlayer == 'none':
                    done = True
                else:
                    players.remove(revealingPlayer)
                    players1.append(revealingPlayer)
        for player in players1:
            playerDict[player].addSet([c1,c2,c3])
        for items in players:
            cards[c1].remove(items)
            cards[c2].remove(items)
            cards[c3].remove(items)
        if cards[c1].playerList() == [playerSuggesting] or cards[c2].playerList() == [playerSuggesting] or cards[c3].playerList() == [playerSuggesting] or cards[c1].playerList() == ['me'] or cards[c2].playerList() == ['me'] or cards[c3].playerList() == ['me']:
            know1Card = True
        if know1Card == True and players == []:
            print(f'{c1}, {c2}, and {c3} are in play' + '\n')
        calculate()
        print('\n')


show()
