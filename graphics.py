import pygame

def draw(board, scale, window):
    debug = False

    y_size = len(board)
    x_size = len(board[0])
    window.fill((200, 200, 200))
    color_unexposed = (200, 200, 200)
    color_exposed = (170, 170, 170)
    border = (0, 0, 0)
    pygame.font.init()
    font = pygame.font.SysFont("Arial", scale)

    for i in range(y_size):
        for j in range(x_size):
            field = pygame.Rect(j * scale, i * scale, scale, scale)
           
            if board[i][j].exposed:
                pygame.draw.rect(window, color_exposed, field)
                pygame.draw.rect(window, border, field, 1)
                if board[i][j].mine:
                    if debug:
                        pygame.draw.rect(window, (255, 100, 100), field)
                        pygame.draw.rect(window, border, field, 1)
                    text = font.render("*", False, (0, 0, 0))
                    window.blit(text, (j * scale, i * scale))
                elif board[i][j].neighbours != 0:
                    text = font.render(str(board[i][j].neighbours), False, (0, 0, 0))
                    window.blit(text, (j * scale, i * scale))  
            elif board[i][j].flagged:
                pygame.draw.rect(window, color_unexposed, field)
                pygame.draw.rect(window, border, field, 1)
                if debug and board[i][j].mine:
                    pygame.draw.rect(window, (255, 100, 100), field)
                    pygame.draw.rect(window, border, field, 1)
                text = font.render("P", False, (0, 0, 0))
                window.blit(text, (j * scale, i * scale))
            else:
                pygame.draw.rect(window, color_unexposed, field)
                pygame.draw.rect(window, border, field, 1)
                if debug and board[i][j].mine:
                    pygame.draw.rect(window, (255, 100, 100), field)
                    pygame.draw.rect(window, border, field, 1)

def mineCount(window, win_size, flagged, mines):
    text_color = (255, 0, 0)
    pygame.font.init()
    font = pygame.font.SysFont("Arial", win_size[1] // 20)
    window.blit(font.render(str(flagged) + '/' + str(mines), False, text_color), (0, 0))

def gameOver(window, win_size):
    text_color = (0, 255, 255)
    pygame.font.init()
    font = pygame.font.SysFont("Arial", win_size[1] // 8)
    window.blit(font.render("GAME OVER", False, text_color), (0, 0))
    
def gameWon(window, win_size):
    text_color = (0, 255, 255)
    pygame.font.init()
    font = pygame.font.SysFont("Arial", win_size[1] // 12)
    window.blit(font.render("CONGRATULATIONS!!!", False, text_color), (0, 0))
