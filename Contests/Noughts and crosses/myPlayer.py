def myPlayer(board):
    rows = board.getRows() # this contains a multi-dimensional array, formatted [['','',''],['','',''],['','','']]
    fields = board.getFields() # this returns an array, formatted ['','','','','','','','','']

    # If a place contains the name of your function, then it is owned by you
    # If it contains an empty string - "" - then you can take it
    # If it contains any other string then it is owned by the other player

    # To take a place, either return its absolute position or an array containing its row and column.
    # e.g. to take the middle left place you could either return 4 or [1, 0]
    # Remember that array start counting at 0, not 1!

    for number, place in enumerate(fields):
        if place == 'myPlayer': # find the first place we own
            num = number + 1 # num is now the next space
            while fields[num - 1] != "": # find the next empty place - remember that arrays count from 0 not 1, unlike the positions in the grid which are 1 to 9
                num += 1
            return num # take that place using the absolute position

    # if we don't own any places yet (i.e. this is the first round)
    # the for loop will run all the way through without returning

    for row_num, row in enumerate(rows):
        for col_num, col in enumerate(row):
            if col == "": # find the first free space
                return [row_num, col_num] # take that space using an array containing row and column

game.add(myPlayer) # register your function as a player, required