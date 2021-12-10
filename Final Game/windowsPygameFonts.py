#ravi vasan
#11/18/21

#####original MENU code from Ms. Suarez



import pygame, os,random,time

from pygame import color
os.system('cls')
pygame.init()

#STUFF FOR THE GAME

from paddle import Paddle
from ball import Ball




colors = {'black':(0,0,0), 
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,145), 
          'white':(255,255,255), 
          'purple':(150,0,150), 
          'orange':(255, 165, 0)}

WHITE=colors.get('white')
BLACK=colors.get('black')
BLUE=colors.get('blue')
background1 = pygame.image.load("Final Game/Final Game Images/TREES WITH BLUE SKY.png")
background2 = pygame.image.load("Final Game/Final Game Images/HANNUKAH.png")
background3 = pygame.image.load("Final Game/Final Game Images/EASTER.jpg")
background4 = pygame.image.load("Final Game/Final Game Images/JULY FOURTH.jpg")
background5 = pygame.image.load("Final Game/Final Game Images/VALENTINE'S DAY.jpg")

WIDTH=700
HEIGHT=500
window = (700, 500)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleA.rect.y = 200

ball = Ball(BLUE, 10, 10)
ball.rect.x = 670
ball.rect.y = 195


all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0


## LISTS FOR MENU MESSAGES

background1 = pygame.image.load("Final Game/Final Game Images/TREES WITH BLUE SKY.png")
background2 = pygame.image.load("Final Game/Final Game Images/HANNUKAH.png")
background3 = pygame.image.load("Final Game/Final Game Images/EASTER.jpg")
background4 = pygame.image.load("Final Game/Final Game Images/JULY FOURTH.jpg")
background5 = pygame.image.load("Final Game/Final Game Images/VALENTINE'S DAY.jpg")

backgroundMessages = [ background1, background2, background3, background4, background5]
screenMessage=[ "900x900", "900x600", "600x600"]
backgroundMessage = ["Easter", "Hannukah", "July Fourth", "Christmas", "Valentine's Day"]
settingMessages=["Screen Size", "Background colors", "Object Colors","Sounds On/Off"]
mainMenu=["Instructions", 'Settings', "Level 1", "Level 2", "ScoreBoard", "Exit"]
colors = {'black':(0,0,0), 
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,145), 
          'white':(255,255,255), 
          'purple':(150,0,150), 
          'orange':(255, 165, 0)}



#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
BLUE=colors.get('blue')
COLOR=WHITE
MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
SCOREBOARD=False
OBJECTCOLOR=False
SOUNDS=False
flag=False

# Screen and square definition
WIDTH=700
HEIGHT=500
wbox=30
hbox=30
x=70
y=150
xs=50
ys=200
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")
square=pygame.Rect(x,y, wbox,hbox)
screenSize=pygame.Rect(xs,ys,wbox*4, hbox*4)
win.fill(COLOR)
squaresSize=[pygame.Rect(xs,ys,wbox*4, hbox*4), pygame.Rect(xs,ys,wbox*4, hbox*3), pygame.Rect(xs,ys,wbox*3, hbox*3)]
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('times new roman', 80)
MENU_FONT=pygame.font.SysFont('times new roman', 40)
INSTRUCTIONS_FONT=pygame.font.SysFont('times new roman', 30)
SCOREBOARD_FONT = pygame.font.SysFont('times new roman', 30)
text= TITLE_FONT.render('message',1,BLACK)
#New window title
background = pygame.image.load("Classwork\Game Images\Final Game Pictures\CHRISTMAS!.jpg")

#making instructions file

myInstructions = open('instructions.txt', 'w')
myInstructions.write('This is a game of PONG \nit is a two player game \nyou will need another person to play with you \none person use the up and down buttons to play \nthe other person will use the w and s buttons to play')
myInstructions.close()

myScoreboard = open('scoreboard.txt', 'w')
myScoreboard.write(" ")
myScoreboard.close()

maxscore = 0
myScoreboard = open('scoreboard.txt', 'a') #opens my scoreboard
myScoreboard.write('\tHighest score:\t' + str(maxscore))

if sel == 4:
    myFile = open("scoreboard.txt", "r")
    print(myFile.read())
    myFile.close()



#Function to print Titles to all screens
def display_Title(message,ym):
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

#Function to print all the menus 
def Menu_function(line):
    pygame.time.delay(100)
    ym=y
    square.y=y
    xm=x+wbox+10
    for i in range(0,len(line)):
        word=line[i]
        pygame.draw.rect(win, BLUE, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym
    
def MainMenuWin(xm,ym):
    global MAINMENU
    global INSTRUCTIONS
    global SETTINGS
    global LEVEL1
    global LEVEL2
    global SCOREBOARD
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        SETTINGS = True  
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 1")
        display_Title("Level 1",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL1 = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 2")
        display_Title("Level 2",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=550 and ym<=575: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("ScoreBoard")
        display_Title("Scoreboard",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=650 and ym<=675: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("Exit",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        global run
        run=False
def SettingMenuWin(xm,ym):
    global SETTINGS
    global SCREEN
    global BACKGROUND
    global OBJECTCOLOR
   
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        display_Title("Screen Size", 70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        SCREEN = True  
                   
    if xm>=70 and xm<=95 and ym>=250 and ym<=275 and flag: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("BACKGROUND COLORS",  70)
        display_Title("BACK", 750)
        pygame.display.update()
        BACKGROUND = True
        SETTINGS = False             
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("OBJECT COLORS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("SOUNDS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True

def Menu_Back():
    win.fill(COLOR)
    display_Title("MAIN", 70)
    Menu_function(mainMenu)
    pygame.display.update()

def Setting_Back():
    win.fill(COLOR)
    display_Title("SETTINGS", 70)
    Menu_function(settingMessages)
    display_Title("Back", HEIGHT-50)
    pygame.display.update()

def Screen_size():
    pygame.time.delay(100)
    ym=ys
    screenSize.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(win, BLUE, squary)
        word= screenMessage[i]
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200

def Background_theme():
    pygame.time.delay(100)
    ym=ys
    backgroundMessage.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(win, BLUE, squary)
        word= backgroundMessage[i]
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200


def level_1():
    win.blit(background, (0,0))
    pygame.display.blit

display_Title("MENU", 40)
Menu_function(mainMenu)
run=True 
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    mouse_pos=(0,0)
    if eve.type==pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            xm=mouse_pos[0]
            ym=mouse_pos[1]
            if MAINMENU:
                MainMenuWin(xm,ym)
            if INSTRUCTIONS:
                myInstructions=open('instructions.txt', 'r')
                yi=150
                for line in myInstructions.readlines():
                    text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                    win.blit(text, (40,yi))
                    pygame.display.update()
                    pygame.time.delay(100)
                    yi+=50
                myInstructions.close()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    INSTRUCTIONS = False
            if SETTINGS:
                SettingMenuWin(xm,ym)
                flag=True
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Menu_Back()
                    MAINMENU = True
                    SETTINGS = False
                    flag=False
            if SCREEN:
                Screen_size()
                display_Title("Back", HEIGHT-50)
                pygame.display.update()
                if xm>450 and xm <540 and ym>200 and ym<290: 
                    WIDTH=600
                    HEIGHT=600
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.fill(COLOR)
                    Screen_size()
                    display_Title("Back", HEIGHT-50)

                    pygame.display.update()
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
            if SCOREBOARD:
                myScoreboard=open('scoreboard.txt', 'r')
                yi=150
                for line in myScoreboard.readlines():
                    text=SCOREBOARD_FONT.render(line, 1, BLACK)
                    win.blit(text, (40,yi))
                    pygame.display.update()
                    pygame.time.delay(100)
                    yi+=50
                myScoreboard.close()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    SCOREBOARD = False
            if BACKGROUND:
                Background_theme
                flag = True

                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    BACKGROUND = False
            if OBJECTCOLOR:
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    OBJECTCOLOR = False
            if LEVEL1:
                #here is the game
                while carryOn:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            carryOn = False
                        elif event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                                    carryOn = False
                
                    #Moving the paddles when the use uses the arrow keys for player A or W/S keys for player B 
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        paddleA.moveUp(10)
                    if keys[pygame.K_s]:
                        paddleA.moveDown(10)
                    if keys[pygame.K_UP]:
                        paddleB.moveUp(10)
                    if keys[pygame.K_DOWN]:
                        paddleB.moveDown(10)    
                
                
                    all_sprites_list.update()
                
                    #Checking if the ball is bouncing against any of the 4 walls
                    if ball.rect.x>=690:
                        scoreA += 1
                        ball.velocity[0] = -ball.velocity[0]
                    if ball.rect.x<=0:
                        scoreB += 1
                        ball.velocity[0] = -ball.velocity[0]
                    if ball.rect.y>490:
                        ball.velocity[1] = -ball.velocity[1]
                    if ball.rect.y<0:
                        ball.velocity[1] = -ball.velocity[1] 

                    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                        ball.bounce()

                    screen.fill(BLACK)
                    # screen.blit(background1, (-200, -200))
                    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)

                    all_sprites_list.draw(screen)
                    # print(scoreA, scoreB)
                    if scoreA >= 10 or scoreB >= 10:
                        LEVEL1 = False
                        MAINMENU = True


                    #SCORE
                    font = pygame.font.Font(None, 74)
                    text = font.render(str(scoreA), 1, WHITE)
                    screen.blit(text, (250, 10))
                    text = font.render(str(scoreB), 1, WHITE)
                    screen.blit(text, (420, 10))

                    pygame.display.flip()

                    clock.tick(60)

                # put the restart game and back button to main menu here. Insert any sprite that you want. 
                # do not put the play again button in the game screen. Go back to main menu before doing back or play again. 

                pygame.quit()

                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    LEVEL1 = False
            if LEVEL2:
                #Play game
                while carryOn:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            carryOn = False
                        elif event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                                    carryOn=False
                
                    #Moving the paddles when the use uses the arrow keys for player A or W/S keys for player B 
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        paddleA.moveUp(5)
                    if keys[pygame.K_s]:
                        paddleA.moveDown(5)
                    if keys[pygame.K_UP]:
                        paddleB.moveUp(5)
                    if keys[pygame.K_DOWN]:
                        paddleB.moveDown(5)    
                
                
                    all_sprites_list.update()
                
                    #Checking if the ball is bouncing against any of the 4 walls
                    if ball.rect.x>=690:
                        scoreA += 1
                        ball.velocity[0] = -ball.velocity[0]
                    if ball.rect.x<=0:
                        scoreB += 1
                        ball.velocity[0] = -ball.velocity[0]
                    if ball.rect.y>490:
                        ball.velocity[1] = -ball.velocity[1]
                    if ball.rect.y<0:
                        ball.velocity[1] = -ball.velocity[1] 

                    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                        ball.bounce()

                    screen.fill(BLACK)
                    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)

                    all_sprites_list.draw(screen)

                    #SCORE
                    font = pygame.font.Font(None, 74)
                    text = font.render(str(scoreA), 1, WHITE)
                    screen.blit(text, (250, 10))
                    text = font.render(str(scoreB), 1, WHITE)
                    screen.blit(text, (420, 10))

                    pygame.display.flip()

                    clock.tick(60)

                pygame.quit()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    LEVEL2 = False