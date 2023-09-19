import pygame
import sys

pygame.init()

GRAY = (51, 56, 61)
GREEN = (144, 232, 188)
RED = (219, 158, 167)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 400
GRID_SIZE = min(WIDTH, HEIGHT) // 3

GRID_LINE_WIDTH = 2
CROSS_LINE_WIDTH = 5
PADDING = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

grid = [['' for _ in range(3)] for _ in range(3)]

def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), GRID_LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), GRID_LINE_WIDTH)

def draw_cross(x, y):
    pygame.draw.line(screen, GREEN, (x - GRID_SIZE // 2, y - GRID_SIZE // 2), (x + GRID_SIZE // 2, y + GRID_SIZE // 2),
                     CROSS_LINE_WIDTH)
    pygame.draw.line(screen, GREEN, (x - GRID_SIZE // 2, y + GRID_SIZE // 2), (x + GRID_SIZE // 2, y - GRID_SIZE // 2),
                     CROSS_LINE_WIDTH)

def draw_circle(x, y):
    pygame.draw.circle(screen, RED, (x, y), GRID_SIZE // 2 - CROSS_LINE_WIDTH, CROSS_LINE_WIDTH)

def check_winner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != '':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != '':
            return grid[0][i]

    if grid[0][0] == grid[1][1] == grid[2][2] != '':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != '':
        return grid[0][2]

    return None

def check_draw():
    for row in grid:
        if '' in row:
            return False
    return True

current_player = 'X'
winner = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if winner is None and not check_draw():
                x, y = event.pos
                col = x // GRID_SIZE
                row = y // GRID_SIZE
                if grid[row][col] == '':
                    grid[row][col] = current_player
                    current_player = 'O' if current_player == 'X' else 'X'
                    winner = check_winner()

    screen.fill(GRAY)

    WIDTH, HEIGHT = screen.get_size()

    draw_grid()

    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'X':
                draw_cross(col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2)
            elif grid[row][col] == 'O':
                draw_circle(col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2)

    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Победил игрок {winner}!", True, GREEN)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        text_bg_rect = pygame.Rect(
            text_rect.left - PADDING,
            text_rect.top - PADDING,
            text_rect.width + 2 * PADDING,
            text_rect.height + 2 * PADDING
        )
        pygame.draw.rect(screen, GRAY, text_bg_rect)

        screen.blit(text, text_rect)
    elif check_draw():
        font = pygame.font.Font(None, 36)
        text = font.render("Ничья!", True, GREEN)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        text_bg_rect = pygame.Rect(
            text_rect.left - PADDING,
            text_rect.top - PADDING,
            text_rect.width + 2 * PADDING,
            text_rect.height + 2 * PADDING
        )
        pygame.draw.rect(screen, GRAY, text_bg_rect)

        screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
sys.exit()
