# corriger beug de la ball qui reste coince dans la raquette
import pgzrun

# TAILLE DE L'ECRAN
WIDTH = 1000
HEIGHT = 800

# Sprites du jeu
ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT/2]
ball_speed = [5, -5]

# Raquette du joueur 1
player1 = Actor("player")
player1.pos = (100, HEIGHT - 50)
player1_score = 0

# Raquette du joueur 2
player2 = Actor("player")
player2.pos = (900, 50)
player2_score = 0

def update():
    ball_movement()
    computer_player_movement()
    update_scores()

def ball_movement():
    global ball_speed
def computer_player_movement():
    # Faites en sorte que player2 suive la position y de la balle
    if player2.y < ball.y:
        player2.y += 5  
    # ajuster la vitesse de suivi ici
    elif player2.y > ball.y:
        player2.y -= 5  
    # ajuster la vitesse de suivi ici

    # Déplacement de la balle
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Assurez-vous que les raquettes ne sortent pas de l'écran
    player1.left = max(player1.left, 0)
    player1.right = min(player1.right, WIDTH)
    
    player2.left = max(player2.left, 0)
    player2.right = min(player2.right, WIDTH)
    
    # Rebond de la balle sur les raquettes
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] *= -1

    # Rebond de la balle sur les bords de l'écran
    if ball.left < 0 or ball.right > WIDTH:
        ball_speed[1] *= -1

    # Rebond de la balle sur le haut et le bas de l'écran
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *= -1

def update_scores():
    global player1_score, player2_score

    # Vérifier si la balle a atteint les bords supérieur ou inférieur
    if ball.left < 0:
        player2_score += 1
        reset_ball()

    elif ball.right > WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    # Réinitialiser la position de la balle au centre
    ball.pos = [WIDTH/2, HEIGHT/2]

def draw():
    screen.clear()
    player1.draw()
    player2.draw()
    ball.draw()

    # Afficher les scores à l'écran
    screen.draw.text(str(player1_score), (WIDTH//4, 50), color="white", fontsize=60)
    screen.draw.text(str(player2_score), (WIDTH*3//4, 50), color="white", fontsize=60)

def on_mouse_move(pos):
    player1.pos = (player1.pos[0], pos[1])

# Lance le jeu
pgzrun.go()

