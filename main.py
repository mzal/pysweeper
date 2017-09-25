import sys, pygame, random
import field, graphics, expose

scale = 30
x_size, y_size = 10, 10
win_size = x_size * scale, y_size * scale
mines_amount = 10
game_is_over = False
mines_flagged = 0
flagged = 0

fields = [[field.Field(False) for j in range(x_size)] for i in range(y_size)]

for i in range(mines_amount):
    y = random.randint(0, y_size - 1)
    x = random.randint(0, x_size - 1)
    while fields[y][x].mine:
        y = random.randint(0, y_size - 1)
        x = random.randint(0, x_size - 1)
    fields[y][x].mine = True

fields.insert(0, [field.Field(False) for i in range(x_size)])
fields.append([field.Field(False) for i in range(x_size)])

for i in fields:
    i.insert(0, field.Field(False))
    i.append(field.Field(False))

for i in range(1, y_size + 1):
    for j in range(1, x_size + 1):
        count = 0
        if fields[i][j].mine is False:
            if fields[i-1][j-1].mine: count += 1
            if fields[i-1][j].mine: count += 1
            if fields[i-1][j+1].mine: count += 1
            if fields[i][j-1].mine: count += 1
            if fields[i][j+1].mine: count += 1
            if fields[i+1][j-1].mine: count += 1
            if fields[i+1][j].mine: count += 1
            if fields[i+1][j+1].mine: count += 1
        fields[i][j].neighbours = count

fields.pop(0)
fields.pop()
for i in fields:
    i.pop(0)
    i.pop()

win = pygame.display.set_mode(win_size)

#main game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #fields[event.pos[1] // scale][event.pos[0] // scale].exposed = True
                fields.insert(0, [field.Field(False) for i in range(x_size)])
                fields.append([field.Field(False) for i in range(x_size)])
                for i in fields:
                    i.insert(0, field.Field(False))
                    i.append(field.Field(False))

                expose.expose(fields, event.pos[0] // scale + 1, event.pos[1] // scale + 1)

                fields.pop(0)
                fields.pop()
                for i in fields:
                    i.pop(0)
                    i.pop()

                if fields[event.pos[1] // scale][event.pos[0] // scale].mine and not fields[event.pos[1] // scale][event.pos[0] // scale].flagged:
                    game_is_over = True

            elif event.button == 3:
                if fields[event.pos[1] // scale][event.pos[0] // scale].flagged is False and fields[event.pos[1] // scale][event.pos[0] // scale].exposed is False:
                    fields[event.pos[1] // scale][event.pos[0] // scale].flagged = True
                    flagged += 1
                    if fields[event.pos[1] // scale][event.pos[0] // scale].mine:
                        mines_flagged += 1
                elif fields[event.pos[1] // scale][event.pos[0] // scale].exposed is False:
                    fields[event.pos[1] // scale][event.pos[0] // scale].flagged = False
                    flagged -= 1
                    if fields[event.pos[1] // scale][event.pos[0] // scale].mine:
                        mines_flagged -= 1

    graphics.draw(fields, scale, win)
    if game_is_over:
        graphics.gameOver(win, win_size)
    elif mines_flagged == flagged and flagged == mines_amount:
        graphics.gameWon(win, win_size)
    else:
        graphics.mineCount(win, win_size, flagged, mines_amount)
    pygame.display.flip()
