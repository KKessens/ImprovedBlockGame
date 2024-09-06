import pygame
import random
import os
import json


ORIGINALWIDTH, ORIGINALHEIGHT = 900, 500
DISPLAY = pygame.display.set_mode((ORIGINALWIDTH, ORIGINALHEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Block Game")

GREEN = (0, 250, 0)
RED = (250, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 250)
VELOCITY = 2
characterVelocity = 0
score = 0
pygame.font.init()
font = pygame.font.SysFont("menlo", 25)
font2 = pygame.font.SysFont("menlo", 50, True)
font3 = pygame.font.SysFont("menlo", 40, True)
font4 = pygame.font.SysFont("menlo", 30, True)
width, height = ORIGINALWIDTH, ORIGINALHEIGHT
widthRatio, heightRatio = width / ORIGINALWIDTH, height / ORIGINALHEIGHT
triangle = pygame.image.load(os.path.join('Sprites', 'Triangle.png'))
circle = pygame.image.load(os.path.join('Sprites', 'Circle.png'))
grassImage = pygame.image.load(os.path.join('Sprites', 'Grass.png'))
pygame.display.set_icon(circle)



class Enemy():
    """
    A class representing the enemy or the spikes at the top of the screen, which end the game if they make contact with the player.

    Attributes:
    - box (Rect): the box that represents the enemy
    - hitBottom (bool): determines whether the box has hit the "bottom" of the screen
    - image (Surface): the image that will be drawn onto the enemy with its scale adjusted
    """

    def __init__(self, x, y):
        """
        Initializes a new enemy

        Parameters:
        - x (int): initial x position of the enemy.
        - y (int): initial y position of the enemy.
        """

        self.box = pygame.Rect(x * widthRatio, y * heightRatio, 20 * widthRatio, 20 * heightRatio)
        self.hitBottom = False
        self.image = pygame.transform.scale(triangle, ((20 * (widthRatio + 0.5)), (20 * heightRatio)))
    def drawEnemy(self):
        """
        Draws the enemy to the screen
        """
        # draws the hitbox of the enemy
        #pygame.draw.rect(DISPLAY, RED, self.box)
        DISPLAY.blit(self.image, (self.box.x - 5, self.box.y))
    def moveDown(self):
        """
        Moves the enemy down, and when it hits the bottom of the screen, moves it back to the top
        """

        global VELOCITY
        # determines if the enemy is at the bottom, if it is resets the y-coordinate to 0
        # otherise moves the enemy down
        if self.box.y > height - (20 * heightRatio):
            self.box.y = 0
            self.hitBottom = True
        else:
            self.box.y += VELOCITY * heightRatio
            self.hitBottom = False
    def checkCollision(self, character):
        """
        checks for a collision between the enemy and the "character" which represents the player

        Parameters:
        - character (Rect): The Rect which represents the player

        Returns:
        boolean: True if a collision between the character and enemy was detected, false if otherwise
        """
        if self.box.colliderect(character):
            return True

def controlCharacter(character):
    """
    Controls the character/player's movements

    Parameters:
    - character (Rect): The Rect of the character to control
    """
    global characterVelocity

    # provides control for the character by increasing or decreasing the velocity of the character when the correct keys are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and characterVelocity < 15:
        characterVelocity += 0.4

    if keys[pygame.K_a] or keys[pygame.K_LEFT] and characterVelocity > -15:
        characterVelocity -= 0.4

    # provides friction for the character
    if characterVelocity < 0:
        characterVelocity += 0.2
    elif characterVelocity > 0:
        characterVelocity -= 0.2

    # if the character hits the edge of the screen, the character's velocity is reversed
    if character.x <= 0:
        characterVelocity *= -1
        characterVelocity += 1
    elif  character.x + (20 * widthRatio) >= width:
        characterVelocity *= -1
        characterVelocity -= 1


    # moves the character an amount determined by the character's velocity
    character.x += characterVelocity * widthRatio

def run():
    """
    Method which runs the main game
    """
    global width
    global height
    global endGame
    global VELOCITY
    global heightRatio
    global widthRatio
    global font

    atBottom = False
    endGame = False
    randomNumber = 20
    # main character
    character = pygame.Rect(440 * widthRatio, 468 * heightRatio, 20 * widthRatio, 20 * heightRatio)
    enemyList = []
    # sets the display properties, with the difference being that the size of the display cannot be changed in this method
    DISPLAY = pygame.display.set_mode((width, height))
    # creates 45 ememies and adds them to the enemyList
    for i in range(45):
        enemy = Enemy(20 * i, 0)
        enemyList.append(enemy)
    clock = pygame.time.Clock()
    run = True
    # image for the sphere used for the character and the grass used for the floor
    #sphere = pygame.transform.scale(circle, (20 * (widthRatio + 1), 20 * (heightRatio + 1)))

    sphere = pygame.transform.scale(circle, (20 * widthRatio , 20 * widthRatio ))
    grass = pygame.transform.scale(grassImage, (width / 3, 20 * heightRatio))

    # updates the font size
    minRatio = min(widthRatio, heightRatio)
    font = pygame.font.SysFont("menlo", int(25 * minRatio))

    # main loop that runs the game
    while run:
        # sets the fps to 60
        clock.tick(60)
        DISPLAY.fill(BLUE)
        # controls each enemy in the list
        for enemy in enemyList:
            # Determines if the enemy should be displayed or not. If it is not displayed then it is a "safe" position for the
            # player to move to and a collision is not checked
            if enemyList[randomNumber] == enemy or enemyList[randomNumber - 1] == enemy or enemyList[randomNumber - 2] == enemy:
                enemy.moveDown()
            else:
                enemy.drawEnemy()
                enemy.moveDown()
                if enemy.checkCollision(character) == True:
                    endGame = True

            # when the enemy hits the bottom a new random number is created which will determine which position is safe
            if enemy.hitBottom == True:
                atBottom = True
                randomNumber = random.randint(0, 44)
            else:
                atBottom = False


        # Rectangles that the grass image will be displayed onto
        grassRectangle1 = pygame.Rect(0, height - (19 * heightRatio), width/3, 20 * heightRatio)
        grassRectangle2 = pygame.Rect(width/3, height - (19 * heightRatio), width/3, 20 * heightRatio)
        grassRectangle3 = pygame.Rect(width * 2/3, height - (19 * heightRatio), width/3, 20 * heightRatio)
        #pygame.draw.rect(DISPLAY, BLACK, grassRectangle1)
        DISPLAY.blit(grass, (grassRectangle1.x, grassRectangle1.y))
        #pygame.draw.rect(DISPLAY, BLACK, grassRectangle2)
        DISPLAY.blit(grass, (grassRectangle2.x, grassRectangle2.y))
        #pygame.draw.rect(DISPLAY, BLACK, grassRectangle3)
        DISPLAY.blit(grass, (grassRectangle3.x, grassRectangle3.y))


        controlCharacter(character)

        # when an enemy hits the bottom (all enemies hit it at the same time) VELOCITY is increased and the score is updated
        # VELOCITY cannot go above 6
        if atBottom == True:

            if VELOCITY < 6:
                VELOCITY += 1/4
            global score
            score += 10

        if endGame == True:
            break

        # displays the score in the top left
        Font = font.render(f"Score: {score}", True, RED)
        DISPLAY.blit(Font, (20 * widthRatio, 20 * heightRatio))

        #pygame.draw.rect(DISPLAY, GREEN, character)
        # draws the sphere image onto the character rectangle
        DISPLAY.blit(sphere, (character.x, character.y))

        #updates the display
        pygame.display.update()


        for event in pygame.event.get():
            # loop that checks for events

            if event.type == pygame.QUIT:
                # quits the game when user exits the game
                run = False
                pygame.quit()
                exit()


def endScreen():
    """
    Screen that is displayed once the game ends
    """
    global width
    global height
    global widthRatio
    global heightRatio
    global characterVelocity
    global score
    global VELOCITY
    global font2
    global font4

    run = True

    clock = pygame.time.Clock()

    # Sets the display. Note, this display is resizable unlike the display in the run method
    DISPLAY = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # gets the current high score
    with open('HighScore.json', 'r') as f:
        HighScore = json.loads(f.read())
        f.close()

    # checks to see if high score needs to be updated, and if so, updates it
    if score > HighScore:
        HighScore = score
        with open('HighScore.json', 'w') as f:
            f.write(json.dumps(HighScore))



    # main loop for the end screen
    while run:

        # smallest ratio for the width and height, used when calculating the size of the fonts
        minRatio = min(widthRatio, heightRatio)
        font2 = pygame.font.SysFont("menlo", int(50 * minRatio), True)
        font4 = pygame.font.SysFont("menlo", int(30 * minRatio), True)

        continueBox = pygame.Rect(300 * widthRatio, 200 * heightRatio, 300 * minRatio, 50 * minRatio)
        DISPLAY.fill(BLACK)

        # text that is displayed to the screen
        text = font2.render(f"Your score was: {score}", True, RED)
        highScoreText = font2.render(f"Highscore: {HighScore}", True, (200, 200, 200))
        againText = font4.render("Play Again", True, BLACK)

        # displays the text to the screen
        DISPLAY.blit(text, (width/4, 50 * heightRatio))
        DISPLAY.blit(highScoreText, (width/4, 115 * heightRatio))
        pygame.draw.rect(DISPLAY, GREEN, continueBox)
        DISPLAY.blit(againText, (345 * widthRatio, 208 * heightRatio))

        # updates the display
        pygame.display.update()

        # sets the fps to 60
        clock.tick(60)

        # loop that checks for events
        for event in pygame.event.get():

            # presses the continue button when the mouse is down and the mouse is inside continueBox
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] > continueBox.x and position[0] < continueBox.x + (300 * widthRatio) and position[1] > continueBox.y and position[1] < continueBox.y + (50 * heightRatio):
                    VELOCITY = 2
                    characterVelocity = 0
                    score = 0
                    run = False

            # quits the game when the user quits the application
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            # updates width, height, and their respective ratios when the screen is resized
            if event.type == pygame.VIDEORESIZE:
                width = event.w
                height = event.h
                widthRatio = width / ORIGINALWIDTH
                heightRatio = height / ORIGINALHEIGHT


def startScreen():
    """
    Screen that is displayed at the start of the game
    """
    global width
    global height
    global widthRatio
    global heightRatio
    global font3
    run = True

    clock = pygame.time.Clock()

    # main loop of the start screen
    while run:

        # sets the fps to 60
        clock.tick(60)

        # smallest ratio for the width and height, used when calculating the size of the fonts
        minRatio = min(widthRatio, heightRatio)
        font3 = pygame.font.SysFont("menlo", int(40 * minRatio), True)


        continueBox = pygame.Rect(600 * widthRatio, 210 * heightRatio, 250 * minRatio, 50 * minRatio)
        DISPLAY.fill(BLACK)

        # text that is displayed to the screen
        text = font3.render("Dodge the Triangles", True, GREEN)
        continueText = font3.render("Continue", True, BLACK)

        # displays the text to the screen and draws the continueBox
        pygame.draw.rect(DISPLAY, RED, continueBox)
        DISPLAY.blit(continueText, (610 * widthRatio, 210 * heightRatio))
        DISPLAY.blit(text, (20 * widthRatio, 210 * heightRatio))

        # updates the display
        pygame.display.update()

        # loop that checks for events
        for event in pygame.event.get():

            # presses the continue button when the mouse is down and the mouse is inside continueBox
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] < continueBox.x + (250 * widthRatio) and position[0] > continueBox.x and position[1] < continueBox.y + (50 * heightRatio) and position[1] > continueBox.y:
                    run = False

            # quits the game when the user quits the application
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            # updates width, height, and their respective ratios when the screen is resized
            if event.type == pygame.VIDEORESIZE:
                width = event.w
                height = event.h
                widthRatio = width / ORIGINALWIDTH
                heightRatio = height / ORIGINALHEIGHT
