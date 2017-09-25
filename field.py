class Field:
    def __init__(self, mine):
        self.mine = mine    #False for empty field, True for mine
        self.exposed = False
        self.flagged = False
        self.neighbours = 0
        