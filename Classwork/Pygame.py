#ravi vasan
#10/15/2021

#learning diplay,
# opening windows,
# changing size window,
# basic game loop
# K_UP           up arrow
# K_DOWN         down arrow
# K_RIGHT        right arrow
# K_LEFT         left arrow

 

import pygame, os, random, math

from pygame.draw import circle
os.system ('cls')

#first thing to do is to initilialize pygame
pygame.init()
check=True
height=500
width=500
colors = {'black':(0,0,0),
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,255), 
          'white':(255,255,255), 
          'purple':(150,0,150)}
keyList = list(colors.keys())


while check:
    # height= input("Height of the window: (100- 1000) ")
    # width = input(" Width of your window:  (10-1000 ")
    #color= input("What color do you prefer red,green,blue,white,blacl, purple ")
    color = random.choice(keyList)
    try:
        height= int(height)
        width=int(width)
        check = False

    except ValueError:
        check = True

color= colors.get(color)
window= pygame.display.set_mode((height,width)) #set up color
window.fill(color)
pygame.display.flip() # refresh window with new color
#change title of your window
pygame.display.set_caption("my game window")
pygame.display.flip()

hbox=50
wbox=50
speed=5
radius = hbox/2
xc = random.randint(25, 500)
yc = random.randint(25, 500)

rect=pygame.Rect(width/2, height/2, wbox, hbox )
pygame.draw.rect(window, colors.get('red'), rect)

pygame.draw.circle(window, colors.get('blue'), (xc, yc), radius)
pygame.display.flip()
run=True


x = 0
y = 0
x + wbox == width
y + hbox == height



# radius = hbox/2
# circle = pygame.circle(width, height,)
# pygame.draw.circle(window, colors.get(), circle)
#main loop for the game:
while run:
    pygame.time.delay(50)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False

    #how to get the position of the mouse

    # x,y=pygame.mouse.get_pos()

    # print("( "+ str(x)+ " , "+ str(y)+" )")
#rectangle movement and border
    keyPressed= pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        if rect.y < 0:
            rect.y = height
        else:
            rect.y -= speed
           
    
    if keyPressed[pygame.K_DOWN]:
        if rect.y>height:
            rect.y=0   
        else:
            rect.y += speed     
            
    
    if keyPressed[pygame.K_LEFT]:
        if rect.x < 0:
            rect.x = width
        else:
            rect.x -= speed
       
    if keyPressed[pygame.K_RIGHT]:
        if rect.x > width:
            rect.x = 0 
        else:
            rect.x += speed

#circle movement and border
    keyPressed= pygame.key.get_pressed()
    if keyPressed[pygame.K_w] and yc >= 0:
        yc -= speed
             
    if keyPressed[pygame.K_s] and yc <= height:
        yc += speed        

    if keyPressed[pygame.K_a] and xc >= 0:
        xc -= speed

    if keyPressed[pygame.K_d] and xc <= width:
        xc += speed
   


    point = (xc, yc)
    collide = pygame.Rect.collidepoint(rect, point)
    #collide function
    if collide:
            radius += wbox/2
            rect.x = random.randrange(25, width)
            rect.y = random.randrange(25, height)



    window.fill(color)
    pygame.display.flip()
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.draw.circle(window, colors.get('blue'), (xc, yc), radius)
    pygame.display.flip()

pygame.quit()