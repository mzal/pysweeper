def expose(board, x, y):
    if not board[y][x].flagged:
        board[y][x].exposed = True
    #debug  print(x, y, sep='\t')
    if x == 0 or x == len(board[0]) - 1 or y == 0 or y == len(board) - 1 or board[y][x].mine:
        return 0
    
    if board[y][x].neighbours == 0:
        if board[y-1][x-1].exposed is False: expose(board, x-1, y-1)
        if board[y-1][x].exposed is False: expose(board, x, y-1)
        if board[y-1][x+1].exposed is False: expose(board, x+1, y-1)
        if board[y][x-1].exposed is False: expose(board, x-1, y)
        if board[y][x+1].exposed is False: expose(board, x+1, y)
        if board[y+1][x-1].exposed is False: expose(board, x-1, y+1)
        if board[y+1][x].exposed is False: expose(board, x, y+1)
        if board[y+1][x+1].exposed is False: expose(board, x+1, y+1)

    return 0
