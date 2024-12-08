import pygame
from pygame.locals import *
pygame.init()

#нстройки игры
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Пинг-понг')
clock = pygame.time.Clock()

black = (0, 0,  0)
white = (255, 255, 255) #red green blue
green = (0, 255, 0)

font = pygame.font.Font(None, 70)

paddle_width = 20
paddle_height = 130



ball_size = 20

player1 = pygame.Rect(50, height // 2 - paddle_height//2, paddle_width, paddle_height)
player2 = pygame.Rect(width - 70, height // 2 - paddle_height//2, paddle_width, paddle_height)
ball = pygame.Rect(width//2 - ball_size//2, height//2 - ball_size//2,ball_size, ball_size)

ball_speed = [10, 10]
paddle_speed = 10

score1 = 0
score2 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[K_s] and player1.bottom < height:
        player1.y += paddle_speed
    if keys[K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[K_DOWN] and player2.bottom < height:
        player2.y += paddle_speed

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = width // 2 - ball_size // 2, height//2 - ball_size//2
        ball_speed = [10,10]
    if ball.right >= width:
        score1 += 1
        ball.x, ball.y = width // 2 - ball_size // 2, height//2 - ball_size//2
        ball_speed = [-10, 10]



    screen.fill(black)
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)
    pygame.draw.aaline(screen, green, (width//2, 0), (width//2,height))
    pygame.draw.ellipse(screen, white, ball)

    score_text1 = font.render(str(score1), True, white)
    score_text2 = font.render(str(score2), True, white)

    screen.blit(score_text1, (width//4, 20))
    screen.blit(score_text2, (3 * width // 4, 20))


    pygame.display.flip()
    clock.tick(60)
pygame.quit()