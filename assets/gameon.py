import pygame
import random

# Initialisera pygame
pygame.init()

# Ladda in musik
pygame.mixer.init()
pygame.mixer.music.load('musik.mp3')
pygame.mixer.music.play(-1)  # Spela musiken på loop

# Skapa fönstret
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Ladda in bilder
player_img = pygame.image.load('player.png')
ball_img = pygame.image.load('balls.png')
square_img = pygame.image.load('kvadrat.png')
triangle_img = pygame.image.load('triangel.png')

# Spelarens position
player_x = screen_width // 2
player_y = screen_height - 100

# Bollens position och hastighet
ball_x = random.randint(0, screen_width)
ball_y = 0
ball_speed = 0.5

# Kvadratens position och hastighet
square_x = random.randint(0, screen_width)
square_y = 0
square_speed = 1

# Triangelns position och hastighet
triangle_x = random.randint(0, screen_width)
triangle_y = 0
triangle_speed = 1.2

# Kollision
def is_collision(enemy_x, enemy_y, player_x, player_y):
    distance = ((enemy_x - player_x)**2 + (enemy_y - player_y)**2)**0.5
    if distance < 27:
        return True
    return False

# Spelloopen
running = True
while running:
    screen.fill((0, 0, 0))  # Svart bakgrund
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Musposition för att styra spelaren
    player_x, _ = pygame.mouse.get_pos()
    player_x -= player_img.get_width() // 2

    # Bollen rör sig
    ball_y += ball_speed
    if ball_y > screen_height:
        ball_y = 0
        ball_x = random.randint(0, screen_width)

    # Kvadraten rör sig
    square_y += square_speed
    if square_y > screen_height:
        square_y = 0
        square_x = random.randint(0, screen_width)

    # Triangeln rör sig
    triangle_y += triangle_speed
    if triangle_y > screen_height:
        triangle_y = 0
        triangle_x = random.randint(0, screen_width)

    # Kolla kollision
    if is_collision(ball_x, ball_y, player_x, player_y) or is_collision(square_x, square_y, player_x, player_y) or is_collision(triangle_x, triangle_y, player_x, player_y):
        running = False  # Spelet är över

    # Rita spelaren och objekten
    screen.blit(player_img, (player_x, player_y))
    screen.blit(ball_img, (ball_x, ball_y))
    screen.blit(square_img, (square_x, square_y))
    screen.blit(triangle_img, (triangle_x, triangle_y))
    
    pygame.display.update()
