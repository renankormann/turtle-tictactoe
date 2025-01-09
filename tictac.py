import turtle

# Setting up the window and turtle details
screen = turtle.getscreen()
screen.bgcolor("black")
t = turtle.Turtle()
t.pencolor("green")
t.speed(5)
size_x = 45
turtle.register_shape("x", ((size_x,size_x),(-size_x,-size_x),(0,0),(-size_x,size_x),(size_x,-size_x), (0,0)))
t.shape("circle")
t.shapesize(0.2,0.2,0.2)

# Function to draw the tic-tac-toe board.
def draw_board():
    t.penup()
    t.goto(30,90)
    t.pendown()
    t.goto(30,-90)
    t.penup()
    
    t.goto(-30,90)
    t.pendown()
    t.goto(-30,-90)
    t.penup()
    
    t.goto(-90,30)
    t.pendown()
    t.goto(90,30)
    t.penup()
    t.goto(-90,-30)
    t.pendown()
    t.goto(90,-30)
    t.penup()

# Function to draw x when player 1 plays.
def draw_x(position):
    t.shapesize(0.2,0.2,0.2)
    t.shape("x")
    if position == 1:
        t.penup()
        t.goto(-60,60)
        t.stamp()
    if position == 2:
        t.penup()
        t.goto(0,60)
        t.stamp()
    if position == 3:
        t.penup()
        t.goto(60,60)
        t.stamp()
    if position == 4:
        t.penup()
        t.goto(-60,0)
        t.stamp()    
    if position == 5:
        t.penup()
        t.goto(0,0)
        t.stamp()
    if position == 6:
        t.penup()
        t.goto(60,0)
        t.stamp()
    if position == 7:
        t.penup()
        t.goto(-60,-60)
        t.stamp()
    if position == 8:
        t.penup()
        t.goto(0,-60)
        t.stamp()
    if position == 9:
        t.penup()
        t.goto(60,-60)
        t.stamp()

# Function to draw O when player 2 plays.
def draw_circle(position):
    t.shape("circle")
    t.shapesize(1)
    if position == 1:
        t.penup()
        t.goto(-60,60)
        t.stamp()
    if position == 2:
        t.penup()
        t.goto(0,60)
        t.stamp()
    if position == 3:
        t.penup()
        t.goto(60,60)
        t.stamp()
    if position == 4:
        t.penup()
        t.goto(-60,0)
        t.stamp()    
    if position == 5:
        t.penup()
        t.goto(0,0)
        t.stamp()
    if position == 6:
        t.penup()
        t.goto(60,0)
        t.stamp()
    if position == 7:
        t.penup()
        t.goto(-60,-60)
        t.stamp()
    if position == 8:
        t.penup()
        t.goto(0,-60)
        t.stamp()
    if position == 9:
        t.penup()
        t.goto(60,-60)
        t.stamp()

# Function to clear the board.
def clear_board():
    t.clearstamps()
 
# Class holding all game functions.     
class TicTact:
    # 'board' holds the squares that you can play from 1 to 9 and 'moves' holds how many moves were done, when moves reach '9' and
    # nobody won, it means it's a draw.
    board = {1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None, 9 : None}
    moves = 0
    
    # local function for the players.
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        draw_board()
    
    # Function determining that if 'moves' is even, it's player 1 turn, and if it's odd, it's player 2 turn. The function also
    # returns the correct either 'x' or 'O'.
    def move(self, play):
        if self.board[play] == None and self.moves <= 9:
            if self.moves % 2 != 0:
                self.board[play] = "o"
                draw_circle(play)
                self.moves += 1 
            else:
                self.board[play] = "x"
                draw_x(play)
                self.moves += 1        

    # Function to check if someone won after a move.
    def round_check(self):
        winner = ""
        if self.board[1] != None and self.board[1] == self.board[2] and self.board[1] == self.board[3]:
            winner = self.board[1]
        if self.board[1] != None and self.board[1] == self.board[5] and self.board[1] == self.board[9]:
            winner = self.board[1]
        if self.board[1] != None and self.board[1] == self.board[4] and self.board[1] == self.board[7]:
            winner = self.board[1]
        if self.board[2] != None and self.board[2] == self.board[5] and self.board[2] == self.board[8]:
            winner = self.board[2]
        if self.board[3] != None and self.board[3] == self.board[5] and self.board[3] == self.board[7]:
            winner = self.board[3]
        if self.board[3] != None and self.board[3] == self.board[6] and self.board[3] == self.board[9]:
            winner = self.board[3]
        if self.board[4] != None and self.board[4] == self.board[5] and self.board[4] == self.board[6]:
            winner = self.board[4]
        if self.board[7] != None and self.board[7] == self.board[8] and self.board[7] == self.board[9]:
            winner = self.board[7]
        return winner

#Main code for the program to run
def main():
    # Asks for players names and save it player1 or 2
    player1 = input("Input the name of player one. Player one is 'x': ")
    player2 = input("Input the name of player two. Player two is 'o': ")
    game = TicTact(player1, player2)
    # Integer to hold the position to play.
    play = 0
    # Plays the game until moves < 9.
    while game.moves < 9:
        if game.moves % 2 == 0:
            print(f"{player1}, ", end="")
        if game.moves % 2 == 1:
            print(f"{player2}, ", end="")
        play = int(input("choose the square you want to play: "))
        game.move(play)
        round_check = game.round_check()
        if round_check != "":
            if round_check == "o":
                print(f"{player2} WON")
                break
            if round_check == "x":
                print(f"{player1} WON")
                break
        if game.moves == 9 and round_check == "":
            print("DRAW")


main()


