import pgzrun

# TAILLE DE L'ECRAN
WIDTH = 1000
HEIGHT = 800

# Sprites du jeu
ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT/2]
ball_speed = [5, -5]
background=Actor("arene.png")


# Raquette du joueur 1
player1 = Actor("red")
player1.pos = (100, HEIGHT - 50)
player1_score = 0

# Raquette du joueur 2
player2 = Actor("blue")
player2.pos = (900, 50)
player2_score = 0

# Nouvelle variable d'état du jeu
game_state = "playing"  # "playing", "player1_wins", "player2_wins", "game_over"

def update():
    if game_state == "playing":
        ball_movement()
        computer_player_movement()
        update_scores()

def ball_movement():
    global ball_speed

def computer_player_movement():
    if player2.y < ball.y:
        player2.y += 5  
    elif player2.y > ball.y:
        player2.y -= 5  

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    player1.left = max(player1.left, 0)
    player1.right = min(player1.right, WIDTH)
    
    player2.left = max(player2.left, 0)
    player2.right = min(player2.right, WIDTH)

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] *= -1

    if ball.left < 0 or ball.right > WIDTH:
        ball_speed[1] *= -1

    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *= -1

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

    screen.clear()
    background.draw()
    player1.draw()
    player2.draw()
    ball.draw()

    # Afficher les scores à l'écran
    screen.draw.text(str(player1_score), (WIDTH//4, 50), color="white", fontsize=60)
    screen.draw.text(str(player2_score), (WIDTH*3//4, 50), color="white", fontsize=60)

    # Afficher l'écran du gagnant ou du perdant
    if game_state == "player1_wins":
        screen.draw.text("Winner: Player 1! Press 'R' to restart.", (WIDTH // 2 - 250, HEIGHT // 2), color="white", fontsize=60)
        if keyboard.R:
            reset_game()

    elif game_state == "player2_wins":
        screen.draw.text("Winner: Player 2! Press 'R' to restart.", (WIDTH // 2 - 250, HEIGHT // 2), color="white", fontsize=60)
        if keyboard.R:
            reset_game()

    elif game_state == "game_over":
        screen.draw.text("Game Over! Press 'R' to restart.", (WIDTH // 2 - 200, HEIGHT // 2), color="white", fontsize=60)
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
