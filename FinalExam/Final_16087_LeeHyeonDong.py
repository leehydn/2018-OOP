###################################################
# Word Quiz
# 2019 - FALL
# OOP FINAL PRACTICE TEST
#--------------------------------------------------
# ID :  16-087        <-  WRITE YOUR ID
# NAME : LeeHyeonDong     <-  WRITE YOUR NAME
###################################################
import random
import time
import sys
from cs1graphics import *

BOARD_SIZE = 3                #  default  3 X 3
CELL_NUMBER = BOARD_SIZE ** 2

COLORS = [ 'red', 'blue']
WINDOW_SIZE = (900,650)
CELL_SIZE = 70                # Graphic Cell Size
PLAYER = 0                    # Start from RED player
                              # 0: RED  1 : BLUE

###################################################
#  Card
###################################################
class Card(object):

    def __init__(self, word, kind , desc, score):
        self.word         = word     #str  apple
        self.description  = desc     #str  Description
        self.kind         = kind     #str  fruit
        self.score        = score    #int  10

###################################################
# Deck
#--------------------------------------------------
# Read "data.txt" file and  make card objects
# Make a dictionary self.cards
# key of self.cards is a score (10,20,30,40)
# value of self.cards is a list of card objects which score is the same as key
# Randomize card order using shuffle
#---------------------------------------------------
# ex)
#  a = Card ('apple', fruit, '����', 10)
#  b = Card ('lion', animal, '����', 10)
#  c = Card ('red' , color , '������', 10)
#  d = Card ('white' , color , '����', 20)
#  e = Card ('book' , object , 'å', 30)
#  self.cards = { 10:[a,b,c] , 20:[d], 30:[e] ... }
###################################################

class Deck(object):

    def __init__(self):

        self.cards = {}  #  make a dictionary. key- score , value - list of cards
        f = open ("data.txt","r")
        for line in f :
            w = line.split()
            score = int(w[3])
            aCard  = Card (w[0],w[1], w[2] , score)

            #--------------------------------------------------
            # Set self.cards using dictionary data structure
            # Each score is used as a key
            # Related card list is used as a value
            #--------------------------------------------------
            ###############################
            #   (1) Implement Here
            if score in self.cards.keys(): #if the key already exists
                self.cards[score].append(aCard)
            else:
                self.cards[score] = [aCard]
            ###############################


        #----------------------------------------
        # Shuffle each card list of self.cards
        #----------------------------------------
        ###############################
        #   (2) Implement Here
        for key in self.cards:
            random.shuffle(self.cards[key])
        ###############################

        f.close()


    def draw(self, score):

        #-----------------------------------------------
        # Take out and return one card object from deck object
        # which score is the same as a parameter
        #-----------------------------------------------
        ###############################
        #   (3) Implement Here
        return self.cards[score].pop()
        ###############################

########################################################
# Cell : the unit of Question Board
#        one cell has one card and related cellGraphic
########################################################

class Cell(object) :

    def __init__(self , row, column, card , centerPt) :
        self.row = row
        self.column = column
        self.card = card
        self.centerPt = centerPt
        self.state = 1    # 1:10  2:kind 3 : answer
        self.activity = False  #



        #######################################################
        # At start, player can select first column of each row
        # It means you can only select 10 point problems cell
        #######################################################
        ###############################
        #   (4) Implement Here
        if self.column == 0: #first column
            self.activity = True #make it available; 10 points problem
        ###############################


    def activate (self) :
        self.activity = True

    def deactivate (self) :
        self.activity = False

###################################################


class CellGraphic (object):


    def __init__ (self, cell , layer  ) :
        self.cell = cell
        self.layer = layer
        self.size =  CELL_SIZE

        self.layer1 = Layer()
        self.layer1.setDepth(30)

        self.layer2 = Layer()
        self.layer2.setDepth(40)

        self.layer3 = Layer()
        self.layer3.setDepth(50)


        #-----------------------------------------
        self.shape1 =  Square (self.size)
        self.shape1.setFillColor ('yellow')
        self.shape1.setDepth(40)

        self.text1  = Text (str(self.cell.card.score))
        self.text1.setFontColor('black')
        self.text1.setFontSize(20)
        self.text1.setDepth(30)

        self.layer1.add(self.shape1)
        self.layer1.add(self.text1)
        self.layer1.moveTo (self.cell.centerPt.getX()  , self.cell.centerPt.getY() )
        self.layer.add (self.layer1)
        #-----------------------------------------

        self.shape2 =  Square (self.size)
        self.shape2.setFillColor ('pink')
        self.shape2.setDepth(40)

        self.text2  = Text (self.cell.card.kind)
        self.text2.setFontColor('black')
        self.text2.setFontSize(10)
        self.text2.setDepth(30)

        self.layer2.add(self.shape2)
        self.layer2.add(self.text2)
        self.layer2.moveTo (self.cell.centerPt.getX()  , self.cell.centerPt.getY() )
        self.layer.add (self.layer2)

        #-----------------------------------------

        self.shape3 =  Square (self.size)
        self.shape3.setFillColor ('green')
        self.shape3.setDepth(40)

        self.text3  = Text (self.cell.card.word)
        self.text3.setFontColor('black')
        self.text3.setFontSize(10)
        self.text3.setDepth(30)

        self.layer3.add(self.shape3)
        self.layer3.add(self.text3)
        self.layer3.moveTo (self.cell.centerPt.getX()  , self.cell.centerPt.getY() )
        self.layer.add (self.layer3)




    def changeCell (self ) :

        #------------------------------------------------------
        # When the cellGraphic is selected,
        # cell.state is changed 1  ->  2  ->  3
        # And related the shape of cellGraphic also be changed
        # 10  ->  animal  -> lion (score -> kind -> word)
        #-------------------------------------------------------
        ###############################
        #   (5) Implement Here
        changing = {1: 2, 2: 3, 3: 3}; l=[self.layer1, self.layer2, self.layer3]
        self.cell.state = changing[self.cell.state]
        self.layer1.setDepth(30); self.layer2.setDepth(30); self.layer3.setDepth(30)
        l[self.cell.state-1].setDepth(3-self.cell.state)
        ###############################

    def deleteCell (self ) :
        self.layer.remove(self.layer1)
        self.layer.remove(self.layer2)
        self.layer.remove(self.layer3)

###################################################
class QuestionBoard(object) :

    def __init__ (self, x, y, canvas, deck) :
        self.l = Layer()
        self.x = x   # starting x position of  QuestionBoard
        self.y = y   # starting y position of  QuestionBoard
        self.canvas = canvas
        self.l.setDepth(40)
        self.l.moveTo(self.x, self.y)


        #------------------------------------------------------------------------------
        # initialize self.keys (list of list) using list comprehension (only one line)
        # for eample when  BOARD_SIZE is 3 ,
        # self.keys is set as  [ [10,20,30] ,[10,20,30], [10,20,30] ]
        # BOARD_SIZE is 4 ,
        # self.keys is set as  [ [10,20,30,40] ,[10,20,30,40], [10,20,30,40] , [10,20,30,40]]
        #--------------------------------------------------------------------------------
        ###############################
        #   (6) Implement Here
        self.keys = [[10*i for i in range(1, BOARD_SIZE+1)]] * BOARD_SIZE
        ###############################

        self.cells = []
        self.cellGraphics = []


        boardBoxSize = CELL_SIZE * BOARD_SIZE + 10 * (BOARD_SIZE+1)

        self.boardBox = Square ( boardBoxSize )
        self.boardBox.setFillColor ('coral')
        self.boardBox.setDepth(60)

        self.boardBox.move( boardBoxSize//2 - 10 ,  boardBoxSize//2 -10)
        self.l.add(self.boardBox)


        #-----------------------------------------------------------------------
        # Fill self.cells and self.cellGraphics using self.keys and deck
        # first, draw proper card object from deck and generate cell object
        # when you finish this part, questionBoard will be filled by cellGraphics
        #------------------------------------------------------------------------
        ###############################
        #   (7) Implement Here
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                newX = CELL_SIZE * 0.5 + col * CELL_SIZE*1.14
                newY = CELL_SIZE * 0.5 + row * CELL_SIZE*1.14
                newCell = Cell(row, col, deck.draw(self.keys[row][col]), Point(newX, newY))
                newCellGraphic = CellGraphic(newCell, self.l)
                self.cells.append(newCell); self.cellGraphics.append(newCellGraphic)
        ###############################
        self.canvas.add(self.l)



    def clear(self) :
        for i in range (len(self.cellGraphics)):
            self.cellGraphics [i].deleteCell()

        self.cells = []
        self.cellGraphics = []


    def findKey (self , x, y ) :
        c_x  =  x    # canvas position
        c_y  =  y
        l_x   = c_x - self.x   # position in the layer
        l_y   = c_y - self.y
        bsize = CELL_SIZE //2

        for i in range (len(self.cells)) :
            acell = self.cells[i]
            p_x  = acell.centerPt.getX()
            p_y  = acell.centerPt.getY()

            s_x =  p_x - bsize
            e_x =  p_x + bsize
            s_y =  p_y - bsize
            e_y =  p_y + bsize

            if ( (  s_x <= l_x <= e_x  )  and  (  s_y <= l_y <= e_y ) ) :
                return i
        return None   # it's not the cell


###################################################
class Table (object) :

    def __init__ (self):

        self.width  = WINDOW_SIZE[0]   #900
        self.height = WINDOW_SIZE[1]   #650
        self.center_x = self.width//2
        self.center_y = self.height//2

        self.canvas = Canvas(self.width, self.height, 'lemonchiffon', 'Word Quiz')
        self.title = Text("Word Quiz")
        self.title.setFontColor('black')
        self.title.setFontSize(45)
        self.title.moveTo (self.center_x ,40)
        self.canvas.add(self.title)


        self.question  = Text("")
        self.question.setFontColor('blue')
        self.question.setFontSize(30)
        self.question.moveTo(self.center_x, 100)
        self.canvas.add(self.question )


        self.answer  = Text("")
        self.answer.setFontColor('red')
        self.answer.setFontSize(30)
        self.answer.moveTo(self.center_x, 150)
        self.canvas.add(self.answer  )


        self.message = Text("message")
        self.message.setFontColor('black')
        self.message.setFontSize(20)
        self.message.moveTo(self.center_x,self.height - 70)
        self.canvas.add(self.message)

        self.ask = Text("")   # Another round ? (y/n)
        self.ask.setFontColor('green')
        self.ask.setFontSize(15)
        self.ask.moveTo(self.center_x,self.height - 30)
        self.canvas.add(self.ask)

        self.deck = Deck()


        self.scoreBoxRed = Rectangle (60 , 30)
        self.scoreBoxRed.setFillColor ('red')
        self.scoreBoxRed.setDepth(40)
        self.scoreBoxRed.moveTo(150, 350)
        self.canvas.add(self.scoreBoxRed)
        self.redText = Text("RED")
        self.redText.setFontColor('white')
        self.redText.setFontSize(15)
        self.redText.setDepth(30)
        self.redText.moveTo(150, 350)
        self.canvas.add(self.redText)

        self.scores = [ Text(' Score : 0'), Text(' Score : 0') ]
        for i in range(2):
            self.scores[i].setFontColor(COLORS[i])
            self.scores[i].setFontSize(15)
            self.scores[i].setDepth(30)
            self.scores[i].moveTo( 150, 400)
            self.canvas.add(self.scores[i])

        self.scores[1].moveTo(self.width - 150, 400)

        self.scoreBoxBlue = Rectangle (60 , 30)
        self.scoreBoxBlue.setFillColor ('blue')
        self.scoreBoxBlue.setDepth(40)
        self.scoreBoxBlue.moveTo(self.width - 150 , 350)
        self.canvas.add(self.scoreBoxBlue)
        self.blueText = Text("BLUE")
        self.blueText.setFontColor('white')
        self.blueText.setFontSize(15)
        self.blueText.setDepth(30)
        self.blueText.moveTo(self.width - 150, 350)
        self.canvas.add(self.blueText)

        self.boardBoxSize = CELL_SIZE * BOARD_SIZE + 10 * (BOARD_SIZE+1)
        self.questionBoard = QuestionBoard (self.center_x - self.boardBoxSize//2 ,  self.center_y - self.boardBoxSize//2  + 40, self.canvas, self.deck )


    def setBoard (self) :
        self.questionBoard = QuestionBoard (self.center_x - self.boardBoxSize//2 ,  self.center_y - self.boardBoxSize//2  + 40 , self.canvas, self.deck )


    def clear(self):
        self.question.setMessage("")
        self.answer.setMessage("")
        self.message.setMessage("")
        self.ask.setMessage("")
        self.questionBoard.clear()
        for i in range(2):
            self.scores[i].setMessage(' Score : 0')


    def close(self):
        self.canvas.close()


#####################################################
# selectOneQuestion
#----------------------------------------------------
# click questionBoard and select one cellGraphic
# player can only select which cell.activity == True
# return the index of selected cell
# change state of each cell's activity
#####################################################

def selectOneQuestion (table):

    while True:
        e = table.canvas.wait()
        if e == None :
            return (-1)  # window close

        d = e.getDescription()

        if d != 'mouse click':
            continue
        p = table.canvas.getMouseCoordinates()
        x = p.getX()
        y = p.getY()

        cell_index = table.questionBoard.findKey(x,y)    #  return questionBoard's  cells' index

        if cell_index == None :            # not cellGraphic
            continue
        else :
            print("Cell number {} selected".format(cell_index))
            aCell  = table.questionBoard.cells[cell_index]

            if aCell.activity == True  : # select a proper cellGraphic
                aCellGraphic = table.questionBoard.cellGraphics[cell_index]
                aCell.deactivate()
                aCellGraphic.changeCell()


                #---------------------------------------------------------------
                # Change the next column's activity state
                # for example after score 10 cell is selected
                # activity state of next column (score 20 cell) also be changed
                #---------------------------------------------------------------
                ###############################
                #   (8) Implement Here
                if cell_index % BOARD_SIZE != BOARD_SIZE-1:
                    table.questionBoard.cells[cell_index + 1].activate()
                ###############################

                return cell_index


###############################################################
#  solveOneQuestion
#--------------------------------------------------------------
# receive keyboard input
# after player's input, show the answer (cell state 3)
# while key answering, you can use backspace to fix the answer
###############################################################
def solveOneQuestion (table , index ) :

    acard = table.questionBoard.cells[index].card
    word_len = len (acard.word)
    word_string = "_ " * word_len
    table.question.setMessage (acard.description)
    table.answer.setMessage ( word_string  )


    step = 0
    acceptedWord = ""


    while step < word_len :
        e = table.canvas.wait()
        if e == None :   #  window close event
            return (-1)
        d = e.getDescription()

        if d != "keyboard":
            continue

        key = e.getKey()

        if key.isalpha() :
            acceptedWord = acceptedWord + key.lower()
            word_string = word_string[: 2*step] + key + word_string[ 2*step + 1 : ]
            table.answer.setMessage ( word_string  )
            step += 1


        if (key == '\b' and step > 0 ):    #backspace


            #------------------------------------------
            # You can fix your answer using backspace key
            # before last character is entered
            # table.answer message is also updated
            #------------------------------------------
            ###############################
            #   (9) Implement Here
            acceptedWord = acceptedWord[:-1]
            word_string = word_string[:2*step-2] + '_ ' + word_string[ 2*step : ]
            table.answer.setMessage(word_string)
            step -= 1
            ###############################


    aCellGraphic = table.questionBoard.cellGraphics[index]
    aCellGraphic.changeCell()

    if acceptedWord == acard.word :
        return int(acard.score)
    else :
        print(acceptedWord, acard.word)
        return 0

####################################
#   wordQuiz  -  one game
####################################
def wordQuiz (table) :

    flipped_cell = 0     # the number of cellGraphic already flipped
    playerScore = [0,0]  # the total scores of each player
    table.message.setMessage("START GAME !!!")
    time.sleep(1)

    PLAYER = 0  # start from red player

    while flipped_cell < CELL_NUMBER :
        table.message.setMessage("This is " + COLORS[PLAYER].upper() + " turn. \nSelect the problem cell ! ")
        table.title.setFontColor(COLORS[PLAYER])  # the color of title will be changed according to the player's turn
        time.sleep(1)


        #----------------------------------
        # Select a proper cellGraphics
        # Solve selected one word problem
        #----------------------------------
        index = selectOneQuestion (table)
        if index == -1 :
            return False # window close event

        table.message.setMessage("This is " + COLORS[PLAYER].upper() + " turn. \nKey in the word ! ")

        getScore = solveOneQuestion(table , index )
        if getScore == -1 :
            return False  # window close event


        if getScore > 0 :

            #----------------------------------------------
            # when the answer is correct, increase player's score
            # and show the changed player's score
            #----------------------------------------------
            ###############################
            #   (10) Implement Here
            playerScore[PLAYER] += getScore
            table.scores[PLAYER].setMessage(" Score : {}".format(playerScore[PLAYER]))
            ###############################

            table.message.setMessage(" Good Job!! Continue~~ ")
            time.sleep(1)

        else :

            #----------------------------------------------
            # When the answer is wrong , change player
            #----------------------------------------------
            ###############################
            #   (11) Implement Here
            PLAYER = (PLAYER + 1) % 2
            ###############################

        flipped_cell += 1

    #--------------------------------------------------------
    # After one game is finished, determine the winner
    # Show a message "RED Win!!" or "BLUE Win!!" or "Tie !!"
    #--------------------------------------------------------
    ###############################
    #   (12) Implement Here
    if playerScore[0] > playerScore[1]: #RED Win
        table.message.setMessage("RED Win!!")
    elif playerScore[0] < playerScore[1]:
        table.message.setMessage("BLUE Win!!") #BLUE Win
    else:
        table.message.setMessage("Tie !!") #Tie
    ###############################
    time.sleep(1)



###################################################
#   main function
#--------------------------------------------------
# Determine the board size (3 is default)
# Set table and  play a wordQuiz
# You can replay many times if you want
###################################################

def main():

    global BOARD_SIZE, CELL_NUMBER
    userInput = input ("Input Game Board Size 3 or 4 : ")
    if userInput != "4" :
        print ("DEFAULT BOARD SIZE 3 WILL BE SET")
    else :
        BOARD_SIZE = 4
        CELL_NUMBER = BOARD_SIZE **2

    table = Table()

    while True :
        finishState = wordQuiz(table)
        if finishState == False :   # window close event
            return

        table.ask.setMessage("Another round ? (y/n)")

        while True:
            e = table.canvas.wait()
            d = e.getDescription()
            if d == "keyboard":
                key = e.getKey()
                if key in ['y','Y'] :
                    table.ask.setMessage("Another round ? (y/n) "+ key)
                    time.sleep(1)
                    table.clear()
                    table.setBoard()
                    break
                else :      #game stop
                    table.close( )
                    return

####################################

main()
