#PONG pygame

import random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [0,0]
ball_vel = [0,0]
player1_vel = 0
player2_vel = 0
l_score = 0
r_score = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hello World')

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ball_vel = [horz,-vert]

# define event handlers
def init():
    global player1_pos, player2_pos, player1_vel, player2_vel,l_score,r_score  # these are floats
    global score1, score2  # these are ints
    player1_pos = [HALF_PAD_WIDTH - 1,HEIGHT/2]
    player2_pos = [WIDTH +1 - HALF_PAD_WIDTH,HEIGHT/2]
    l_score = 0
    r_score = 0
    if random.randrange(0,2) == 0:
        ball_init(True)
    else:
        ball_init(False)


#draw function of canvas
def draw(canvas):
    global player1_pos, player2_pos, ball_pos, ball_vel, l_score, r_score
           
    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    if player1_pos[1] > HALF_PAD_HEIGHT and player1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        player1_pos[1] += player1_vel
    elif player1_pos[1] == HALF_PAD_HEIGHT and player1_vel > 0:
        player1_pos[1] += player1_vel
    elif player1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and player1_vel < 0:
        player1_pos[1] += player1_vel
    
    if player2_pos[1] > HALF_PAD_HEIGHT and player2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        player2_pos[1] += player2_vel
    elif player2_pos[1] == HALF_PAD_HEIGHT and player2_vel > 0:
        player2_pos[1] += player2_vel
    elif player2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and player2_vel < 0:
        player2_pos[1] += player2_vel

    #update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    #draw paddles and ball
    pygame.draw.circle(canvas, RED, ball_pos, 20, 0)
    pygame.draw.polygon(canvas, GREEN, [[player1_pos[0] - HALF_PAD_WIDTH, player1_pos[1] - HALF_PAD_HEIGHT], [player1_pos[0] - HALF_PAD_WIDTH, player1_pos[1] + HALF_PAD_HEIGHT], [player1_pos[0] + HALF_PAD_WIDTH, player1_pos[1] + HALF_PAD_HEIGHT], [player1_pos[0] + HALF_PAD_WIDTH, player1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, GREEN, [[player2_pos[0] - HALF_PAD_WIDTH, player2_pos[1] - HALF_PAD_HEIGHT], [player2_pos[0] - HALF_PAD_WIDTH, player2_pos[1] + HALF_PAD_HEIGHT], [player2_pos[0] + HALF_PAD_WIDTH, player2_pos[1] + HALF_PAD_HEIGHT], [player2_pos[0] + HALF_PAD_WIDTH, player2_pos[1] - HALF_PAD_HEIGHT]], 0)

    #ball collision check on top and bottom walls
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #ball collison check on gutters or paddles
    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(player1_pos[1] - HALF_PAD_HEIGHT,player1_pos[1] + HALF_PAD_HEIGHT,1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        r_score += 1
        ball_init(True)
        
    if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(player2_pos[1] - HALF_PAD_HEIGHT,player2_pos[1] + HALF_PAD_HEIGHT,1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
        l_score += 1
        ball_init(False)

    #update scores
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
    canvas.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
    canvas.blit(label2, (470, 20))  
    
    
#keydown handler
def keydown(event):
    global player1_vel, player2_vel
    
    if event.key == K_UP:
        player2_vel = -8
    elif event.key == K_DOWN:
        player2_vel = 8
    elif event.key == K_w:
        player1_vel = -8
    elif event.key == K_s:
        player1_vel = 8

#keyup handler
def keyup(event):
    global player1_vel, player2_vel
    
    if event.key in (K_w, K_s):
        player1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        player2_vel = 0

init()


#game loop
while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)