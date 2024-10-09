import pgzrun
import random

# TAILLE DE L'ECRAN
WIDTH = 1000
HEIGHT = 800
center = [400, 300]

# Sprites du jeu
ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT/2]
ball_speed = [5, -5]

# Raquette du joueur 1
player1 = Actor("player")
player1.pos = (WIDTH/9, HEIGHT-50)

# Raquette du joueur 2
player2 = Actor("player")
player2.pos = (WIDTH*8/9, 50)

def update():
    ball_movement()

def ball_movement():
    global ball_speed

    # Déplacement de la balle
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Déplacement de la raquette du joueur 1 avec les touches gauche et droite
    if keyboard.left:
        player1.x -= 5
    elif keyboard.right:
        player1.x += 5

    # Déplacement de la raquette du joueur 2 avec les touches Q et D
    if keyboard.q:
        player2.x -= 5
    elif keyboard.d:
        player2.x += 5

    # Assurez-vous que les raquettes ne sortent pas de l'écran
    player1.left = max(player1.left, 0)
    player1.right = min(player1.right, WIDTH)
    player2.left = max(player2.left, 0)
    player2.right = min(player2.right, WIDTH)

    
    # Rebond de la balle sur les raquettes
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[1] = -ball_speed[1]

    # Rebond de la balle sur le haut et le bas de l'écran
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Notez que vous pouvez ajuster ces conditions pour avoir un rebond sur au moins 2 des 4 bords

def draw():
    screen.clear()
    screen.draw.circle(center, 10, "green")
    player1.draw()
    player2.draw()
    ball.draw()
def on_mouse_move(pos):
    # player.pos=[pos[1] player.pos[0]]
    player1.pos = (player1.pos[0], pos[1])
    player2.pos = (player2.pos[0], pos[1])
# Lance le jeu
pgzrun.go()
