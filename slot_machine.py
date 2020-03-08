#Imports the pygame module
import pygame

#Imports the time module so that we can stop the code for x-amount of secons
import time

#Imports the random module so that we can make random numbers
import random

#Initiates thes pygame module
pygame.init()

#Initiazes the sound module
pygame.mixer.init()

#Hides the cursor
pygame.mouse.set_visible(0)

#Define color variables since Python doesn't have build in color definition
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Dimensions of the chevrons
cevron_height = 260
cevron_width = 300

#Wheel positions
x = 450
y = 910

x2 = 735
y2 = 390

x3 = 1035
y3 = 650

rel_y = 5
rel_y2 = 5
rel_y3 = 5

#Deposit, bet, and freespins variables
deposit = 1000
bet = 0
free_spins = 0
prize = 10

wait = 1.1

#Variables for the number of playlines
playline1 = True
playline2 = False
playline3 = False

win_playline1 = False
win_playline2 = False
win_playline3 = False

#Variables for betting
bet_10 = False
bet_50 = False
bet_100 = False

#Creates a new object that can call the 'render' method
gameFont = pygame.font.SysFont(None, 75)
prizeFont = pygame.font.SysFont(None, 75)
fontColor = green


#Gets the screen size an places it in an object
display_size = pygame.display.Info()

#Setes the display widht and height to the screens resolution
display_height = display_size.current_h
display_width = display_size.current_w


#Create an integer that holds the display size
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

#Sets the title of the window
pygame.display.set_caption('Sundowns Slot Machine')

#Sets the ingame timing, game clock so that everything runs at the same speed in game.
clock = pygame.time.Clock()

#////////////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#///////////////////////////////////////////////////////////////////////////// Game Graphics and videos Here\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

#Pygame function: create a variable, and within that variable an image is loaded
wheel = pygame.image.load('graphics/wheel2.jpg').convert()
#Scales the image
wheel = pygame.transform.scale(wheel, (305, 1050))
5#Pygame function: create a variable, and within that variable an image is loaded
left_ui = pygame.image.load('graphics/left_ui2.jpg').convert()
#Scales the image
left_ui = pygame.transform.scale(left_ui, (450, 1050))

#Pygame function: create a variable, and within that variable an image is loaded
right_ui = pygame.image.load('graphics/right_ui2.jpg').convert()
#Scales the image
right_ui = pygame.transform.scale(right_ui, (570, 1050))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Game Graphics and videos Here //////////////////////////////////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////////////////////#


#////////////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#///////////////////////////////////////////////////////////////////////////// Game Sounds Here\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

#Import sound file
doh = pygame.mixer.Sound("sounds/doh.wav")
wohoo = pygame.mixer.Sound("sounds/wohoo.wav")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Game sounds Here ///////////////////////////////////////////////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////////////////////#


#////////////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#                                                                              Functions Here                                                                                          #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////////////////////#

def graphics():
    playlines()
    draw_left_ui()
    draw_right_ui()
    draw_deposit()
    draw_bet()
    draw_freespins()
    draw_prize()

def draw_left_ui():
    #Draws the left UI
    gameDisplay.blit(left_ui, (0,0))


def draw_right_ui():
    gameDisplay.blit(right_ui, ((display_width - 580),0))


def playlines():
    #Draws the first playline
    pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 6, display_width - 780, 4])

    if playline2 == True:    
        #Draws playline 2
        #Horisontal lines
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 - 260, 300, 4])
        
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 260, 4, 255])
        
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])


    
    if playline3 == True:
        #Draws playline 3
        #Horisontal lines
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 + 249, 300, 4])
        
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 2, 4, 255])
        
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])

        
def playlines_win():
    global win_playline1
    global win_playline2
    global win_playline3

    if win_playline1 == True:
        #Draws the first playline
        pygame.draw.rect(gameDisplay, green, [390, display_height/2 - 6, display_width - 780, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 6, display_width - 780, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)

        #Draws the first playline
        pygame.draw.rect(gameDisplay, green, [390, display_height/2 - 6, display_width - 780, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 6, display_width - 780, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        
        #Draws the first playline
        pygame.draw.rect(gameDisplay, green, [390, display_height/2 - 6, display_width - 780, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 6, display_width - 780, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()

    if win_playline2 == True:
        pygame.draw.rect(gameDisplay, green, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, green, [990, display_height/2 - 260, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, green, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, green, [987, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, green, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 - 260, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)

        pygame.draw.rect(gameDisplay, green, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, green, [990, display_height/2 - 260, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, green, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, green, [987, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, green, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 - 260, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)

        pygame.draw.rect(gameDisplay, green, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, green, [990, display_height/2 - 260, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, green, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, green, [987, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, green, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 - 260, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 - 260, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 260, 4, 255])
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)

    if win_playline3 == True:
        pygame.draw.rect(gameDisplay, green, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, green, [990, display_height/2 + 249, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, green, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, green, [987, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, green, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 + 249, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)

        pygame.draw.rect(gameDisplay, green, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, green, [990, display_height/2 + 249, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, green, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, green, [987, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, green, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 + 249, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)

        pygame.draw.rect(gameDisplay, green, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, green, [990, display_height/2 + 249, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, green, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, green, [987, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, green, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        pygame.draw.rect(gameDisplay, red, [390, display_height/2 + 249, 300, 4])
        pygame.draw.rect(gameDisplay, red, [990, display_height/2 + 249, 300, 4])
        #Vertical lines
        pygame.draw.rect(gameDisplay, red, [688, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [987, display_height/2 - 2, 4, 255])
        pygame.draw.rect(gameDisplay, red, [395, display_height/2 - 6, display_width - 790, 4])
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Pause for a certain amount of time
        time.sleep(wait)
        
    win_playline1 = False
    win_playline2 = False
    win_playline3 = False
        

def draw_deposit():
    textsurface = gameFont.render(str(deposit), False, fontColor)
    gameDisplay.blit(textsurface,(55,121))

def bet_handling():
    global bet
    
    #Playline 1 and whatever bet has been entered will remain the same
    if bet_10 == True and playline2 == False and playline3 == False:
        bet = 10

    elif bet_50 == True and playline2 == False and playline3 == False:
        bet = 50
        
    elif bet_100 == True and playline2 == False and playline3 == False:
        bet = 100



    #If playline two has been chosen, the bet will be multiplied by two
    if bet_10 == True and playline2 == True and playline3 == False:
        bet = 20

    elif bet_50 == True and playline2 == True and playline3 == False:
        bet = 100
        
    elif bet_100 == True and playline2 == True and playline3 == False:
        bet = 200



    #If playline three has been chosen, the bet will be multiplued by two
    if bet_10 == True and playline2 == True and playline3 == True:
        bet = 60

    elif bet_50 == True and playline2 == True and playline3 == True:
        bet = 300
        
    elif bet_100 == True and playline2 == True and playline3 == True:
        bet = 600

    draw_prize()
    


def draw_bet():
    textsurface = gameFont.render(str(bet), False, fontColor)
    gameDisplay.blit(textsurface,(55,268))

def draw_freespins():
    textsurface = gameFont.render(str(free_spins), False, fontColor)
    gameDisplay.blit(textsurface,(55,402))

def draw_prize():
    textsurface = gameFont.render('Prize:', False, fontColor)
    gameDisplay.blit(textsurface,(55,850))
    
    textsurface = prizeFont.render(str(prize), False, fontColor)
    gameDisplay.blit(textsurface,(55,905))


def win_conditions(y, y2, y3):

    #Fetches the global integers
    global deposit
    global bet
    global free_spins
    global prize
    global playline2
    global playline3
    global win_playline1
    global win_playline2
    global win_playline3
    
    #Checks if playline 1 to 3 is active
    if playline1 == True:

        #These are the conditions for which the user wins
        #If all the wheels are the same
        if y == y2 and y2 == y3:
            #How much the player has won
            win_amount = bet*1000
            bet = win_amount
            deposit += win_amount
            prize = win_amount
            win_amount = 0
            win_playline1 = True

        #Burns, Burns, Smithers or Burns Smithers, Burns    
        if y == 390 and y2 == 390 and y3 == 650 or y == 390 and y2 == 650 and y3 == 390:
            #How much the player has won
            win_amount = bet*3
            bet = win_amount
            deposit += win_amount
            prize = win_amount
            win_amount = 0
            win_playline1 = True

        #Donut, Donut, Homer or Donut, Homer, Donut    
        if y == 130 and y2 == 130 and y3 == 910 or y == 130 and y2 == 910 and y3 == 130:
            #How much the player has won
            win_amount = bet*2
            bet = win_amount
            deposit += win_amount
            prize = win_amount
            win_amount = 0
            win_playline1 = True

        #Smithers, Burns Homer OR Homer, Burns, Smithers OR Smithers, Homer, Burns  
        if y == 650 and y2 == 390 and y3 == 910 or y == 910 and y2 == 650 and y3 == 390 or y == 390 and y2 == 910 and y3 == 650:
            #How much the player has won
            win_amount = bet*0
            bet = win_amount
            deposit += win_amount
            prize = win_amount
            free_spins = 3
            win_amount = 0
            win_playline1 = True

        #Checks if playline 1 and 2 is active
        if playline2 == True:

            #These are the conditions for which the user wins
            #If all the wheels are the same
            if y+(130*2) == y2 and y3+(130*2) == y2 or y == 910 and y2 == 130 and y3 == 910:
                #How much the player has won
                win_amount = bet*10
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                win_amount = 0
                win_playline2 = True
                

            #Burns, Burns, Smithers or Burns Smithers, Burns    
            if y == 130 and y2 == 390 and y3 == 390 or y == 130 and y2 == 650 and y3 == 130:
                #How much the player has won
                win_amount = bet*3
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                win_amount = 0
                win_playline2 = True

            #Donut, Donut, Homer or Donut, Homer, Donut    
            if y == 910 and y2 == 130 and y3 == 650 or y == 910 and y2 == 910 and y3 == 910:
                #How much the player has won
                win_amount = bet*2
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                win_amount = 0
                win_playline2 = True

            #Smithers, Burns, Homer OR Homer, Burns, Smithers OR Smithers, Homer, Burns  
            if y == 390 and y2 == 390 and y3 == 650 or y == 650 and y2 == 650 and y3 == 130 or y == 130 and y2 == 910 and y3 == 390:
                #How much the player has won
                win_amount = bet*0
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                free_spins = 3
                win_amount = 0
                win_playline2 = True

        #Checks if playline 1 and 3 is active
        if playline3 == True:

            #///////////////////////////////////////////////////Conditions One\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
            #These are the conditions for which the user wins
            #If all the wheels are the same
            if y2+(130*2) == y and y2+(130*2) == y3 or y == 130 and y2 == 910 and y3 == 130:
                #How much the player has won
                win_amount = bet*10
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                win_amount = 0
                win_playline3 = True

            #Burns, Burns, Smithers OR Burns, Smithers, Burns    
            if y == 650 and y2 == 390 and y3 == 910 or y == 650 and y2 == 650 and y3 == 650:
                #How much the player has won
                win_amount = bet*3
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                win_amount = 0
                win_playline3 = True

            #Donut, Donut, Homer or Donut, Homer, Donut    
            if y == 390 and y2 == 130 and y3 == 130 or y == 390 and y2 == 910 and y3 == 390:
                #How much the player has won
                win_amount = bet*2
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                win_amount = 0
                win_playline3 = True

            #Smithers, Burns Homer OR Homer, Burns, Smithers OR Smithers, Homer, Burns
            if y == 910 and y2 == 390 and y3 == 130 or y == 130 and y2 == 650 and y3 == 650 or y == 650 and y2 == 910 and y3 == 910:
                #How much the player has won
                win_amount = bet*0
                bet = win_amount
                deposit += win_amount
                prize = win_amount
                free_spins = 3
                win_amount = 0
                win_playline3 = True

    win()
    bet = 0

def win():
    wohoo.play()
    graphics()
    playlines_win()

def lose():
    #Plays sound file
    doh.play()
    graphics()

def wheel_stop():
    #Plays sound file
    doh.play()


def draw_wheel(x,y):
    #Draw the wheel on the screen
    gameDisplay.blit(wheel, (x,y))


#////////////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#///////////////////////////////////////////////////////////////////////////// Spin Wheels Animation\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
def spin_wheel(x, y, x2, y2, x3, y3, spin_time, spin_time2, spin_time3):

    #Get the global rel_y variables
    global rel_y
    global rel_y2
    global rel_y3
    

    while spin_time + spin_time2 + spin_time3 > 0:


        #Random spin_time
        spin_time_random = random.randrange(1,2)
        
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update(390, 0, (display_width - 780), display_height)

        if spin_time > 0:


        
            #Get the screen and the image heights and divide it...or something I don't quite understand this part of the code, but it works...Somehow
            rel_y = y % wheel.get_rect().height
                
            #Draw the wheel and parse the magical arguments from before to the draw_wheel function
            draw_wheel(x, rel_y - wheel.get_rect().height)

            #Check to see if the wheel has gone outside of the screen. It it has, set the new image to rotate so that it 'wraps' around
            if rel_y < display_size.current_h:
                    #Draw the new on the new position
                gameDisplay.blit(wheel, (x, rel_y))


            #Decerases the spintime for every round
            spin_time -= spin_time_random

            #Controls the wheel spin speed
            y +=100

            if y > 1040:
                y = 0

            if spin_time <= 1:
                    
                #Check the wheels position and correct it if it's above or below a certain threshold
                if y < 130:
                    y = 130

                if y > 0 + 130 and y < 260 + 130:
                    y = 0 + 130

                if y > 260 + 130 and y < 520 + 130:
                    y = 260 + 130

                if y > 520 + 130 and y < 780 + 130:
                    y = 520 + 130

                if y > 780 + 130 and y < 1040 + 130:
                    y = 780 + 130

                if y > 1040 + 130:
                    y = 0 + 130

                wheel_stop()

        if spin_time2 > 0:
            #Get the screen and the image heights and divide it...or something I don't quite understand this part of the code, but it works...Somehow
            rel_y2 = y2 % wheel.get_rect().height
                
                #Draw the wheel and parse the magical arguments from before to the draw_wheel function
            draw_wheel(x2, rel_y2 - wheel.get_rect().height)

                #Check to see if the wheel has gone outside of the screen. It it has, set the new image to rotate so that it 'wraps' around
            if rel_y2 < display_size.current_h:
                    #Draw the new on the new position
                gameDisplay.blit(wheel, (x2, rel_y2))


            #Decerases the spintime for every round
            spin_time2 -= spin_time_random

            #Controls the wheel spin speed
            y2 +=100

            if y2 > 1040:
                y2 = 0

            if spin_time2 <= 1:

                #Check the wheels position and correct it if it's above or below a certain threshold
                if y2 < 130:
                    y2 = 130

                if y2 > 0 + 130 and y2 < 260 + 130:
                    y2 = 0 + 130

                if y2 > 260 + 130 and y2 < 520 + 130:
                    y2 = 260 + 130

                if y2 > 520 + 130 and y2 < 780 + 130:
                    y2 = 520 + 130

                if y2 > 780 + 130 and y2 < 1040 + 130:
                    y2 = 780 + 130

                if y2 > 1040 + 130:
                    y2 = 0 + 130

                wheel_stop()


        if spin_time3 > 0:
        

            #Get the screen and the image heights and divide it...or something I don't quite understand this part of the code, but it works...Somehow
            rel_y3 = y3 % wheel.get_rect().height
                
                #Draw the wheel and parse the magical arguments from before to the draw_wheel function
            draw_wheel(x3, rel_y3 - wheel.get_rect().height)

                #Check to see if the wheel has gone outside of the screen. It it has, set the new image to rotate so that it 'wraps' around
            if rel_y3 < display_size.current_h:
                    #Draw the new on the new position
                gameDisplay.blit(wheel, (x3, rel_y3))


            #Decerases the spintime for every round
            spin_time3 -= spin_time_random


            #Controls the wheel spin speed
            y3 +=100

            if y3 > 1040:
                y3 = 0

            if spin_time3 <= 1:

                #Check the wheels position and correct it if it's above or below a certain threshold
                if y3 < 130:
                    y3 = 130

                if y3 > 0 + 130 and y3 < 260 + 130:
                    y3 = 0 + 130

                if y3 > 260 + 130 and y3 < 520 + 130:
                    y3 = 260 + 130

                if y3 > 520 + 130 and y3 < 780 + 130:
                    y3 = 520 + 130

                if y3 > 780 + 130 and y3 < 1040 + 130:
                    y3 = 780 + 130

                if y3 > 1040 + 130:
                    y3 = 0 + 130

                wheel_stop()

            playlines()
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Spin Wheels Animation //////////////////////////////////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////////////#

   



    #Get the screen and the image heights and divide it...or something I don't quite understand this part of the code, but it works...Somehow
    rel_y = y % wheel.get_rect().height
    rel_y2 = y2 % wheel.get_rect().height
    rel_y3 = y3 % wheel.get_rect().height
            
    #Draw the wheel and parse the magical arguments from before to the draw_wheel function
    draw_wheel(x, rel_y - wheel.get_rect().height)
    draw_wheel(x2, rel_y2 - wheel.get_rect().height)
    draw_wheel(x3, rel_y3 - wheel.get_rect().height)

    #Check to see if the wheel has gone outside of the screen. It it has, set the new image to rotate so that it 'wraps' around
    if rel_y2 < display_size.current_h or rel_y2 < display_size.current_h or rel_y3 < display_size.current_h:
        #Draw the new on the new position
  
        gameDisplay.blit(wheel, (x, rel_y))
        gameDisplay.blit(wheel, (x2, rel_y2))
        gameDisplay.blit(wheel, (x3, rel_y3))

    
    #Draws all the graphics
    playlines()

    #Update the display, so that all the graphics on the screen will be updated
    pygame.display.update()

    win_conditions(y, y2, y3)






#////////////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#                                                                              Main Code Here                                                                          #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////#

#Defines the main loop function. Stuff here is the definitions before the game starts, including variable declarations
def main_loop():
    
    #Gets the global variable 'bet'
    global bet
    global deposit
    global free_spins
    global prize

    global playline1
    global playline2
    global playline3

    global bet_10
    global bet_50
    global bet_100

    #Draws the wheel when the screen loads for the first time
    draw_wheel(x, rel_y)
    draw_wheel(x2, rel_y2)
    draw_wheel(x3, rel_y3)

  
    #Sets a boolean variable 'crashed' to false. Its purpose is to check wether we have crashed and the loop needs to break
    UserQuit = False
    #While 'crashed' is false, run this loop
    while not UserQuit:

        
#////////////////////////////////////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#/////////////////////////////////////////////////////////////////////////////Event Handling\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        #Gets any event that happens - cursor location, key press, button presses etc per fram, per second
        for event in pygame.event.get():

            #If the event type is the user having pressed the "x" (quit button) in the window, the program will terminate
            if event.type == pygame.QUIT:
                #Sets the 'crashed' boolean to 'true' so that the while loop breaks
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                prize = 0
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                

                #Checks for the amount of money the player has bet
                if event.key == pygame.K_1:
                    #Sets the bet statements
                    bet_10 = True
                    bet_50 = False
                    bet_100 = False

                if event.key == pygame.K_2:
                    #Sets the bet statements
                    bet_10 = False
                    bet_50 = True
                    bet_100 = False
                    
                if event.key == pygame.K_3:
                    #Sets the bet statements
                    bet_10 = False
                    bet_50 = False
                    bet_100 = True

                    
                #Cheks what playlines the user wants to bet on
                if event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6:

                    draw_wheel(x, rel_y - wheel.get_rect().height)
                    draw_wheel(x2, rel_y2 - wheel.get_rect().height)
                    draw_wheel(x3, rel_y3 - wheel.get_rect().height)

                    #Check to see if the wheel has gone outside of the screen. It it has, set the new image to rotate so that it 'wraps' around
                    if rel_y < display_size.current_h or rel_y2 < display_size.current_h or rel_y3 < display_size.current_h: 
                        draw_wheel(x, rel_y)
                        draw_wheel(x2, rel_y2)
                        draw_wheel(x3, rel_y3)


                #Checks for the number of playlines chosen
                if event.key == pygame.K_4:
                    playline1 = True
                    playline2 = False
                    playline3 = False
                    #Go to the playline draw function
                    playlines()
                    
                    
                if event.key == pygame.K_5 :
                    playline1 = True
                    playline2 = True
                    playline3 = False
                    #Go to the playline draw function
                    playlines()
                    

                if event.key == pygame.K_6:
                    playline1 = True
                    playline2 = True
                    playline3 = True
                    #Go to the playline draw function
                    playlines()


                #Checks if the user has pressed the 'down' key. If he has, go to the 'spin_wheel' function
                if event.key == pygame.K_DOWN and bet > 0 and deposit > 0 and deposit >= bet:
                    #prize = 0
                    draw_prize()

                    extra_randomness = random.randrange(0, 50)
                    extra_randomness2 = random.randrange(0, 100)
                    extra_randomness3 = random.randrange(0, 100)
                    #Generates a random spintime number
                    spin_time = random.randrange(50, 60) + extra_randomness
                    #Generates a random spintime number
                    spin_time2 = random.randrange(5, 150) + spin_time + extra_randomness2
                    #Generates a random spintime number
                    spin_time3 = random.randrange(5, 150) + spin_time + spin_time2 + extra_randomness3

                    if free_spins <= 0:
                        #Subtracts the bet amount from the deposit
                        deposit -= bet

                    else:
                        #Decrease the number og free_spins by 1
                        free_spins -= 1
                    
                    #Go to the 'spin_wheel' function
                    spin_wheel(x, y, x2, y2, x3, y3, spin_time, spin_time2, spin_time3)

                #Go to the bet handling function
                bet_handling()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Event Handlings End//////////////////////////////////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////////////////////////////////////////////////#


        graphics()
            
        #Update the display, so that all the graphics on the screen will be updated
        pygame.display.update()
        #Define the target frames.  Argument is frames per second 
        clock.tick(60)


#Draws all the graphics
graphics()

#Draws the wheel
#spin_wheel(x, y, x2, y2, x3, y3, 0, 0, 0)

pygame.display.update()

#Goes to the main loop to start the game
main_loop()
