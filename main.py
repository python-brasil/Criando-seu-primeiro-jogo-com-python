import pygame
import sys
import random

# Inicialização do pygame
pygame.init()

# Definições da janela
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jogo Snake Python Brasil")

# Cores
white = (255, 255, 255)
black = (46, 49, 54, 1)
blue = (57, 126, 184, 1)
yellow = (255, 224, 82, 1)

# Tamanho do bloco e velocidade
block_size = 20
speed = 10

# Relógio para controle de FPS
clock = pygame.time.Clock()

# Função para desenhar a cobra
def draw_snaake(snake):
    for segment in snake:
        pygame.draw.rect(window, blue, pygame.Rect(segment[0], segment[1], block_size, block_size))

# Função principal do jogo
def game():
    snake = [[100, 100]]
    direction = [block_size, 0]
    food = [random.randrange(0, window_size[0] - block_size, block_size),
            random.randrange(0, window_size[1] - block_size, block_size)]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = [0, -block_size]
                elif event.key == pygame.K_DOWN:
                    direction = [0, block_size]
                elif event.key == pygame.K_LEFT:
                    direction = [-block_size, 0]
                elif event.key == pygame.K_RIGHT:
                    direction = [block_size, 0]

        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        snake.insert(0, new_head)

        if snake[0] == food:
            food = [random.randrange(0, window_size[0] - block_size, block_size),
            random.randrange(0, window_size[1] - block_size, block_size)]
        else:
            snake.pop()

        window.fill(black)
        pygame.draw.rect(window, yellow, pygame.Rect(food[0], food[1], block_size, block_size))
        draw_snaake(snake)

        pygame.display.flip()
        clock.tick(speed)


game()