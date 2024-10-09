import pgzrun


# TAILLE DE L'ECRAN
WIDTH = 800
HEIGHT = 600

# taille des players et de la balle
P1_SIZE = 47, 98
P2_SIZE = 50, 106

BALL_SIZE = 43, 43

# Sprites du jeu
ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT/2]
ball_speed = [5, -5]

# image de font
background=Actor("arene.png")

# Raquette du joueur 1
player1 = Actor("red.png")
player1.pos = (40,50)
player1_score = 0

# Raquette du joueur 2
player2 = Actor("blue.png")
player2.pos = (900, 50)
player2_score = 0

# Nouvelle variable d'état du jeu
game_state = "playing" 

# player2 joueur ordinateur
def computer_player_movement():
    if player2.y < ball.y:
        player2.y += 0
    elif player2.y > ball.y:
        player2.y -= 0

# placement des joueurs sur l'ecran
    player1.left = max(player1.left, 0)
    player1.right = min(player1.right, WIDTH)
    player2.left = max(player2.left, 0)
    player2.right = min(player2.right, WIDTH)

def ball_movement():
    global ball_speed
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
# Rebond de la balle sur les raquettes
    if ball.colliderect(player1):
        x, y = ball.pos
        x = player1.pos[0] + P1_SIZE[0] /2 + BALL_SIZE[0] / 2
        ball.pos = x, y 
        ball_speed[0] *= -1
        sounds.ping_pong_8bit_beeep.play()
    
    if ball.colliderect(player2):
        x, y = ball.pos
        x = player2.pos[0] - P2_SIZE[0] /2 - BALL_SIZE[0] / 2
        ball.pos = x, y 
        ball_speed[0] *= -1
        sounds.ping_pong_8bit_beeep.play()

# Rebond de la balle sur les bords de l'écran
    if ball.left < 0 or ball.right > WIDTH:
        ball_speed[0] *= -1
        
# Rebond de la balle sur le haut et le bas de l'écran
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *= -1
        sounds.ping_pong_8bit_beeep.play()

def update():
    if game_state == "playing":
        ball_movement()
        computer_player_movement()
        update_scores()

def update_scores():
    global player1_score, player2_score, game_state

    if ball.left < 0:
        player2_score += 1
        if player2_score == 5:
            game_state = "player2_wins"
    

        else:
            reset_ball()

    if ball.right > WIDTH:
        player1_score += 1
        if player1_score == 5:
            game_state = "player1_wins"
            
        
            
        else:
            reset_ball()

def reset_ball():
    global game_state
    if player1_score == 5 or player2_score == 5:
        game_state = "game_over"
    else:
        game_state = "playing"
        ball.pos = [WIDTH/2, HEIGHT/2]

def draw():
    global game_state
    global sound

    screen.clear()
    background.draw()
    player1.draw()
    player2.draw()
    ball.draw()

    # Afficher les scores à l'écran
    screen.draw.text(str(player1_score), (WIDTH//4, 50), color="red", fontsize=60)
    screen.draw.text(str(player2_score), (WIDTH*3//4, 50), color="blue", fontsize=60)

    # Afficher l'écran du gagnant ou du perdant
    if game_state == "player1_wins":
        sounds.victoir1.play()
        screen.draw.text(" tu as gagnier ,Press 'R'\n pour redemarrer ", (WIDTH // 2 - 250, HEIGHT // 2), color="red", fontsize=60)
        # ("t'as gagnier ,à + minable \n,Press 'R'\n pour redemarrer ", (WIDTH // 2 - 250, HEIGHT // 2), color="red", fontsize=60)

        if keyboard.R:
            reset_game()

    elif game_state == "player2_wins":
        
        sounds.gameover.play()
        screen.draw.text("T'as perdu .\n Press 'R' pour redemarrer", (WIDTH // 2 - 250, HEIGHT // 2), color="red", fontsize=60)
        
    
        # ("T'as perdu minable!!.\n,Press 'R' pour redemarrer.....\n ou pas je m'en fou", (WIDTH // 2 - 250, HEIGHT // 2), color="red", fontsize=60)
        
        # si la touche r est press redemmare le jeu
        if keyboard.R:
            reset_game()


def on_mouse_move(pos):
    player1.pos = (player1.pos[0], pos[1])


def reset_game():
    global player1_score, player2_score, game_state
    player1_score = 0
    player2_score = 0
    game_state = "playing"
    reset_ball()


# Lance le jeu
pgzrun.go()
