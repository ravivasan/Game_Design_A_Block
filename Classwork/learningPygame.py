# ravi vasan
# 10/15/21
# learning today:
#     display
#     opening windows 
#     changing size window 
#     basic game loop 

import pygame,os, random

from pygame.constants import K_DOWN
os.system('cls')

#first thing to do is to initilaize pygame

pygame.init()


check = True
height = 600
width = 600
colors = {"black":(0, 0, 0),
          "red":(255, 0, 0), 
          "green":(0, 255, 0), 
          "blue":(0, 0, 255), 
          "white":(255, 255, 255), 
          "purple":(150, 0, 150), 
          "orange":(255, 69, 0),
          "maroon":(128, 0, 0)}
keyList = list(colors.keys())
# valueList = list(colors)

# print(keyList)
# print(valueList)


while check:
    # height = input("height of the window: (100-1000)\n")
    # width = input("width of your window: (100-1000)\n")
    # color = input("pick a color: black, red, green, blue, white, purple\n")
    # random.choice(keyList)
    color = random.choice(keyList)
    
    try:
        height = int(height)
        width = int(width)
        check = False
    except ValueError:
        check = True


color = colors.get(color)

window = pygame.display.set_mode((width, height))
window.fill(color) #(RGB) the most you can get is 255 for each color
window = pygame.display.flip() #refresh the window with new color
pygame.display.set_caption("my game window") #change title of your window 
window = pygame.display.flip()

hbox = 50
wbox = 50
speed = 5
rect = pygame.Rect( width/2, height/2, wbox, hbox)
pygame.draw.rect(window, color, rect)
pygame.display.update()
run=True

#main loop for the game:
while run:
    pygame.time.delay(100)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run = False
    
    # how to get the location of the mouse
    # x, y = pygame.mouse.get_pos()
    # print("("+ str(x)+ "," + str(y)+ ")")
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        rect.y -= speed
    if keyPressed[pygame.K_DOWN]:
        rect.y += speed
    if keyPressed[pygame.K_RIGHT]:
        rect.x += speed
    if keyPressed[pygame.K_LEFT]:
        rect.x -= speed
    
    window.fill(color)
    pygame.display.update()
    pygame.draw.rect(window, colors.get(color), rect)
    pygame.display.update() 
    

pygame.quit()

