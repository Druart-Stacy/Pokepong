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
background = Actor("arene.png")

sounds.champion.play()
sounds.champion.set_volume(0.4)
# Raquette du joueur 1
player1 = Actor("red.png")
player1.pos = (40, 50)
player1_score = 0

# Raquette du joueur 2
player2 = Actor("blue.png")
player2.pos = (900, 50)
player2_score = 0

# Nouvelle variable d'état du jeu
game_state = "menu"
start_button_clicked = False
paused = False

# bouton pour démarrer le jeu
start_button = Actor("button.png")
start_button.pos = (WIDTH // 2, HEIGHT // 2)


# player1 joueur ordinateur
def computer_player1_movement():
    if player1.y < ball.y:
        player1.y += 5
    elif player1.y > ball.y:
        player1.y -= 5
# player2 joueur ordinateur
def computer_player_movement():
    if player2.y < ball.y:
        player2.y += 4
    elif player2.y > ball.y:
        player2.y -= 4

# placement des joueurs sur l'ecran
    player1.left = max(player1.left, 0)
    player1.right = min(player1.right, WIDTH)
    player2.left = max(player2.left, 0)
    player2.right = min(player2.right, WIDTH)

# Rebond de la balle sur les raquettes
def ball_movement():
    global ball_speed
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

# collision entre les players et la balle
    if ball.colliderect(player1):
        x, y = ball.pos
        x = player1.pos[0] + P1_SIZE[0] / 2 + BALL_SIZE[0] / 2
        ball.pos = x, y 
        ball_speed[0] *= -1
        sounds.ping_pong_8bit_beeep.play()

    if ball.colliderect(player2):
        x, y = ball.pos
        x = player2.pos[0] - P2_SIZE[0] / 2 - BALL_SIZE[0] / 2
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
    global game_state, start_button_clicked, paused

    if game_state == "playing" and not paused:
        ball_movement()
        computer_player1_movement()
        computer_player_movement()
        update_scores()

def update_scores():
    global player1_score, player2_score, game_state

    if ball.left < 0:
        player2_score += 1
        if player2_score == 5:
            game_state = "player2_wins"
            sounds.champion.stop()  # Arrête la musique du champion
        else:
            reset_ball()

    if ball.right > WIDTH:
        player1_score += 1
        if player1_score == 5:
            game_state = "player1_wins"
            sounds.champion.stop()  # Arrête la musique du champion
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
    global game_state, paused

    screen.clear()
    background.draw()
    player1.draw()
    player2.draw()
    ball.draw()

# Afficher le bouton de démarrage
    if game_state == "menu":
        start_button.draw()

# Afficher les scores à l'écran
    screen.draw.text(str(player1_score), (WIDTH//4, 50), color="red", fontsize=60)
    screen.draw.text(str(player2_score), (WIDTH*3//4, 50), color="blue", fontsize=60)

# Afficher l'écran du gagnant ou du perdant
    if game_state == "player1_wins":
        sounds.victoir1.play()
        screen.draw.text("T'as gagné, appuie sur 'R' pour redémarrer.", (WIDTH // 2 - 250, HEIGHT // 2), color="green", fontsize=40)
        #screen.draw.text ("t'as gagnier ,à + minable \n,appuie sur 'R'\n pour redemarrer ", (WIDTH // 2 - 250, HEIGHT // 2), color="red", fontsize=60)
        if keyboard.R:
            reset_game()

    elif game_state == "player2_wins":
        sounds.gameover.play()
        screen.draw.text("T'as perdu,appuie sur 'R' pour redémarrer.", (WIDTH // 2 - 250, HEIGHT // 2), color="green", fontsize=40)
        # ("T'as perdu minable!! \n,appuie 'R' pour redemarrer.....\n ou pas je m'en fous", (WIDTH // 2 - 250, HEIGHT // 2), color="red", fontsize=60)
        
        # si la touche r est press redemmare le jeu
        if keyboard.R:
            reset_game()
            

    elif paused:
        screen.draw.text("Pause. Appuie sur 'P' pour reprendre.", (WIDTH // 2 - 200, HEIGHT // 2), color="green", fontsize=30)

def on_mouse_move(pos):
    player1.pos = (player1.pos[0], pos[1])

#  metre le jeu en pause
def on_key_down(key):
    global paused
    if key == keys.P:
        pause()

# mise en place du buttun start
def on_mouse_down(pos, button):
    global game_state, start_button_clicked
    if start_button.collidepoint(pos) and game_state == "menu" and not start_button_clicked:
        game_state = "playing"
        start_button_clicked = True  

def reset_game():
    global player1_score, player2_score, game_state, paused
    player1_score = 0
    player2_score = 0
    game_state = "playing"
    paused = False
    reset_ball()
    
def pause():
    global paused
    paused = not paused
    
pgzrun.go()
