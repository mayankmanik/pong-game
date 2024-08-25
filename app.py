import time
import random
import pygame

#  initialise pygame
pygame.init()

#  create screen
screen = pygame.display.set_mode((1000, 700))

#  title icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# gameVariables
redX = 5
redY = 300
greenX = 975
greenY = 300
redXchange = 0
redYchange = 0
greenXchange = 0
greenYchange = 0
ballY = random.randint(30, 350)
ballX = 500
speed = 0.8
ballXchange = 0.6
ballYchange = 0.6

# score and fonts
green_score = 0
red_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)


def restart():
    global ballX, ballY
    ballY = random.randint(30, 350)
    ballX = 500
    time.sleep(1)

def checkCollision(red_player, green_player, ball):
    global ballXchange, ballYchange, ballX, ballY, green_score, red_score
    red_collision = pygame.Rect.colliderect(red_player, ball)
    green_collision = pygame.Rect.colliderect(green_player, ball)
    
    if red_collision or green_collision:
        pygame.mixer.Sound.play(plob_sound)
        ballXchange *= random.choice((-1, 1))
        ballYchange *= random.choice((-1, 1))

    if ballX > 985 and green_collision == False:
        pygame.mixer.Sound.play(score_sound)
        restart()
        green_score += 1

    if ballX < 15 and red_collision == False:
        pygame.mixer.Sound.play(score_sound)
        restart()
        red_score += 1

def gameScreen(redX, redY, greenX, greenY, ballX, ballY):
    player1color = (255, 53, 94)
    player2color = (60, 208, 112)
    pygame.draw.aaline(screen, (255, 255, 255), (500, 0), (500, 700))
    red_player = pygame.draw.rect(
        screen, player1color, pygame.Rect(redX, redY, 20, 100))
    green_player = pygame.draw.rect(
        screen, player2color, pygame.Rect(greenX, greenY, 20, 100))
    ball = pygame.draw.circle(screen, (255, 215, 0), [ballX, ballY], 15, 0)

    checkCollision(red_player, green_player, ball)


# sound
plob_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

#  game loop
running = True
while running:
    screen.fill((83, 104, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                greenYchange = -speed
            if event.key == pygame.K_DOWN:
                greenYchange = +speed
            if event.key == pygame.K_LEFT:
                greenXchange = -speed
            if event.key == pygame.K_RIGHT:
                greenXchange = +speed
            if event.key == pygame.K_a:
                redXchange = -speed
            if event.key == pygame.K_d:
                redXchange = +speed
            if event.key == pygame.K_s:
                redYchange = +speed
            if event.key == pygame.K_w:
                redYchange = -speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                greenYchange = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                redYchange = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                greenXchange = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                redXchange = 0

    # player movement & boundary
    redY += redYchange
    redX += redXchange
    greenY += greenYchange
    greenX += greenXchange

    if redY < 0:
        redY = 0
    if greenY < 0:
        greenY = 0
    if redY > 600:
        redY = 600
    if greenY > 600:
        greenY = 600
    if redX > 476:
        redX = 476
    if redX < 5:
        redX = 5
    if greenX < 505:
        greenX = 505
    if greenX > 975:
        greenX = 975

    gameScreen(redX, redY, greenX, greenY, ballX, ballY)

    #  ball movement & boundary
    ballX += ballXchange
    ballY += ballYchange

    if ballY < 15 or ballY > 685:
        pygame.mixer.Sound.play(plob_sound)
        ballYchange = -ballYchange

    # score display
    player_text = basic_font.render(f"{green_score}", True, (200, 200, 200))
    screen.blit(player_text, (460, 420))
    red_text = basic_font.render(
        f"{red_score}", True, (200, 200, 200))
    screen.blit(red_text, (520, 420))

    # update screen
    pygame.display.update()
