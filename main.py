import pygame as pg #get commands for pygame
#preparation stuff
backColor=(50,190,0) #set the color of the background
screen=pg.display.set_mode((700,700)) #Add a window
pg.display.set_caption("Chrys World") #change the name of the window
dude=pg.image.load("dude.png").convert_alpha() #load and scale up a red dude
dude=pg.transform.scale(dude,size=(50,50))
sword=pg.image.load("coolsword.png").convert_alpha() #do the same for a cool red sword
sword=pg.transform.scale(sword,size=(25,60))
pg.display.set_icon(dude)
dudeW,dudeH=dude.get_size() #get the width and height of the dude
def getMouse(): #get mouse position
    global mouseX #mouseX and mouseY are global variables
    global mouseY
    mouseX, mouseY = pg.mouse.get_pos()
mdown=False #flag for if the mouse was already pressed
running=True
while running: #loop
    screen.fill(backColor) #Fill the screen with background color
    getMouse()
    mouseFocus=pg.mouse.get_focused
    if mouseFocus==0:
        pg.mouse.set_visible=False
    else:
        pg.mouse.set_visible=True
    screen.blit(dude, dest=(mouseX-(dudeW/2),mouseY-(dudeH/2))) #put the dude on the screen, using the width and height to center it on the mouse
    pg.display.flip() #refresh
    for event in pg.event.get():
        if event.type==pg.QUIT: #If the window is closed, stop the loop
            running=False
        elif event.type==pg.MOUSEBUTTONDOWN: #when the mouse is clicked, rotate the dude. But only rotate him once per mouse press.
            if mdown==False: 
                mdown=True
                dude=pg.transform.rotate(dude,90)
        elif event.type==pg.MOUSEBUTTONUP:
            mdown=False