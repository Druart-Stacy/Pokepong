import pgzrun

# DEBUT TAILLE DE L ECRAN
WIDTH = 1000
HEIGHT = 800
center = [400, 300]
# FIN TAILLE DE L ECRAN

# sprites du jeu
ball = Actor("ball")
ball.pos = [600, 800] 
ball_speed = [5, -5]

# player= Actor("player")
# player.pos =(WIDTH/5, HEIGHT-50)
player_1 = Actor('player')
player_1.pos=[0,0]
player_2 = Actor('player')
player_2.pos=[0,0]

def update():
    center[0]= center[0] + 1
    # if ball.colliderect(player):
    #     invert_verti_speed()
    global ball_speed

    # Déplacement de la balle
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    if ball.right >= WIDTH:
       invert_horizontal_speed()
# Rebond de la balle sur les bords de l'écran (haut et bas)
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Rebond de la balle sur les bords latéraux de l'écran

#debut retire le commentaire pour remetre en lateral
    # if ball.left < 0 or ball.right > WIDTH:
    #     ball_speed[0] = -ball_speed[0]

    if ball.top < 0 or ball.bottom > HEIGHT:
       ball_speed[1] = -ball_speed[1]
#fin retire le commentaire pour remetre en lateral
    # Rebond de la balle sur les raquettes
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed[1] = -ball_speed[1]

    
def draw():
    screen.clear()
    screen.draw.circle(center, 10, "green")
    player_1.draw()
    player_2.draw()
    
   
    
def on_mouse_move(pos):
    # player.pos=[pos[1] player.pos[0]]
    player_1.pos = (player_1.pos[0], pos[1])
    player_2.pos = (player_2.pos[0], pos[1])
def invert_horizontal_speed():
 ball_speed[0] = ball_speed[0] * -1
def invert_vertical_speed():
 ball_speed[1] = ball_speed[1] * -1

# def invert_horizontal_speed():
#     ball_speed[0] = ball_speed[1]*-1
# def invert_vertical_speed():
#     ball_speed[1] = ball_speed[0]*-1
pgzrun.go()

# import pgzrun
# import random

# # TAILLE DE L'ECRAN
# WIDTH = 1000
# HEIGHT = 800
# center = [400, 300]

# # Sprites du jeu
# ball = Actor("ball")
# ball.pos = [WIDTH/2, HEIGHT/2]
# ball_speed = [5, -5]

# # Raquette du joueur 1
# player1 = Actor("player")
# player1.pos = (WIDTH/9, HEIGHT-50)

# # Raquette du joueur 2
# player2 = Actor("player")
# player2.pos = (WIDTH*8/9, 50)

# def update():
#     ball_movement()

# def ball_movement():
#     global ball_speed

#     # Déplacement de la balle
#     ball.x += ball_speed[0]
#     ball.y += ball_speed[1]

#     # Déplacement de la raquette du joueur 1 avec les touches gauche et droite
#     if keyboard.left:
#         player1.x -= 5
#     elif keyboard.right:
#         player1.x += 5

#     # Déplacement de la raquette du joueur 2 avec les touches Q et D
#     if keyboard.q:
#         player2.x -= 5
#     elif keyboard.d:
#         player2.x += 5

#     # Assurez-vous que les raquettes ne sortent pas de l'écran
#     player1.left = max(player1.left, 0)
#     player1.right = min(player1.right, WIDTH)
#     player2.left = max(player2.left, 0)
#     player2.right = min(player2.right, WIDTH)

#     # Rebond de la balle sur les bords de l'écran
#     if ball.left < 0 or ball.right > WIDTH:
#         ball_speed[0] = -ball_speed[0]

#     # Rebond de la balle sur les raquettes
#     if ball.colliderect(player1) or ball.colliderect(player2):
#         ball_speed[1] = -ball_speed[1]

#     # Rebond de la balle sur le haut et le bas de l'écran
#     if ball.top < 0 or ball.bottom > HEIGHT:
#         ball_speed[1] = -ball_speed[1]

# def draw():
#     screen.clear()
#     screen.draw.circle(center, 10, "green")
#     player1.draw()
#     player2.draw()
#     ball.draw()

# # Lance le jeu
# pgzrun.go()
