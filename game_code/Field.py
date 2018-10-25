'''
Created on Oct 24, 2018

@author: me
'''
from Crypto.Random.random import randint
class field:
    '''
    takes:
    y = integer height of field - 1
    x = integer length of field - 1
    bombs = number of bombs to plant
    
    returns:
    nothing
    '''
    def __init__(self, y, x, bombs):
        self.field_height = y
        self.field_length = x
        self.field_list = []
        self.field_list_ui = []
        self._new_field(x, y)
        self._lay_bombs(bombs)
        self._enumerate_cells()
    '''
    the functions below are only used in init
    '''
    
    '''
    takes:
    y = integer height of field - 1
    x = integer length of field - 1
    
    returns:
    nothing
    
    modifies: field_list and field_list_ui
    
    new field only sets field_list and field_list_ui as lists of correct length
    '''
    def _new_field(self, x, y):
        for y in range(0, self.field_height):
            self.field_list.append([])
            for x in range(0, self.field_length):
                self.field_list[y].append(0)
        for y in range(0, self.field_height):
            self.field_list_ui.append([])
            for x in range(0, self.field_length):
                self.field_list_ui[y].append("-")
    
    '''
    takes:
    number of bombs to put on the field

    returns:
    nothing
    
    modifies:
    field_list
    
    fills in the field with exactly "bomb" bombs randomly
    '''
    def _lay_bombs(self, bombs):
        bomb_count = 0
        while bomb_count < bombs:
            x = randint(0, self.field_length-2)
            y = randint(0, self.field_height-2)
            if self.field_list[y][x] == 0:
                self.field_list[y][x] = "B"
                bomb_count += 1
    
    '''
    takes:
    number of bombs to put on the field
    x coordinate to not lay bomb on
    y coordinate to not lay bomb on
    
    returns:
    nothing
    
    modifies:
    field_list
    
    only used in _select_first to relay a bomb, it should not be used anywhere else
    '''
    def _relay_bombs(self, bombs, y_avoid, x_avoid):
        bomb_count = 0
        while bomb_count < bombs:
            x = randint(0, self.field_height-2)
            y = randint(0, self.field_height-2)
            if self.field_list[y][x] == 0:
                if x != x_avoid:
                    if y != y_avoid:
                        self.field_list[y][x] = "B"
                        bomb_count += 1
     
    '''
    takes:
    nothing
    
    returns:
    nothing
    
    modifies:
    field_list_ui
    
    fills in each cell not containing a bomb with the number of bombs among its neighbors.
    This includes the top, left, right, bottom, and all diagonals. 
    '''       
    def _enumerate_cells(self):
        #first, we enumerate all the corners, in cases where B is in the corner
        #corner (0, 0)
        if self.field_list[0][0] == "B":
            if self.field_list[1][0] != "B":
                self.field_list[1][0] += 1
            if self.field_list[0][1] != "B":
                self.field_list[0][1] += 1
            if self.field_list[1][1] != "B":
                self.field_list[1][1] += 1
        #corner (field_height, 0)
        if self.field_list[self.field_height-1][0] == "B":
            if self.field_list[self.field_height-2][0] != "B":
                self.field_list[self.field_height-2][0] += 1
            if self.field_list[self.field_height-1][1] != "B":
                self.field_list[self.field_height-1][1] += 1
            if self.field_list[self.field_height-2][1] != "B":
                self.field_list[self.field_height-2][1] += 1
        #corner (0, field_length-1)
        if self.field_list[0][self.field_length-1] == "B":
            if self.field_list[1][self.field_length-1] != "B":
                self.field_list[1][self.field_length-1] += 1
            if self.field_list[0][self.field_length-2] != "B":
                self.field_list[0][self.field_length-2] += 1
            if self.field_list[1][self.field_length-2] != "B":
                self.field_list[1][self.field_length-2] += 1
        #corner (field_height, field_length-1)
        if self.field_list[self.field_height-1][self.field_length-1] == "B":
            if self.field_list[self.field_height-2][self.field_length-1] != "B":
                self.field_list[self.field_height-2][self.field_length-1] += 1
            if self.field_list[self.field_height-1][self.field_length-2] != "B":
                self.field_list[self.field_height-1][self.field_length-2] += 1
            if self.field_list[self.field_height-2][self.field_length-2] != "B":
                self.field_list[self.field_height-2][self.field_length-2] += 1
        #next, we will go voer the cases where B is in the top row, bottom row, leftmost collumn, and rightmost collumn
        
        #for x will go over the top and bottom rows
        for x in range(1, self.field_length-1):
            #first, check for bottom row (where y is 0)
            if self.field_list[0][x] == "B":
                #add one to the cells above it
                if self.field_list[1][x-1] != "B":
                    self.field_list[1][x-1] +=1
                if self.field_list[1][x] != "B":
                    self.field_list[1][x] +=1
                if self.field_list[1][x+1] != "B":
                    self.field_list[1][x+1] +=1
                #add one to the cells to the side
                if self.field_list[0][x+1] != "B":
                    self.field_list[0][x+1] +=1
                if self.field_list[0][x-1] != "B":
                    self.field_list[0][x-1] +=1
            
            #next, check for top row (where y is 0)
            if self.field_list[self.field_height-1][x] == "B":
                if self.field_list[self.field_height-2][x-1] != "B":
                    self.field_list[self.field_height-2][x-1] +=1
                if self.field_list[self.field_height-2][x] != "B":
                    self.field_list[self.field_height-2][x] +=1
                if self.field_list[self.field_height-2][x+1] != "B":
                    self.field_list[self.field_height-2][x+1] +=1
                #add one to the cells to the side
                if self.field_list[self.field_height-1][x+1] != "B":
                    self.field_list[self.field_height-1][x+1] +=1
                if self.field_list[self.field_height-1][x-1] != "B":
                    self.field_list[self.field_height-1][x-1] +=1
                
        #for y will go over the leftmost and rightmost columns
        for y in range(1, self.field_height-1):
            #first, check for leftmost row (where x is 0)
            if self.field_list[y][0] == "B":
                if self.field_list[y-1][1] != "B":
                    self.field_list[y-1][1] +=1
                if self.field_list[y][1] != "B":
                    self.field_list[y][1] +=1
                if self.field_list[y+1][1] != "B":
                    self.field_list[y+1][1] +=1

                #add one to the cells above and below
                if self.field_list[y+1][0] != "B":
                    self.field_list[y+1][0] +=1
                if self.field_list[y-1][0] != "B":
                    self.field_list[y-1][0] +=1
            
            #next, check for rightmost column (where x is the field length - 2)
            if self.field_list[y][self.field_length-1] == "B":
                if self.field_list[y-1][self.field_length-2] != "B":
                    self.field_list[y-1][self.field_length-2] +=1
                if self.field_list[y][self.field_length-2] != "B":
                    self.field_list[y][self.field_length-2] +=1
                if self.field_list[y+1][self.field_length-2] != "B":
                    self.field_list[y+1][self.field_length-2] +=1
                #add one to the cells above and below
                if self.field_list[y-1][self.field_length-1] != "B":
                    self.field_list[y-1][self.field_length-1] +=1
                if self.field_list[y+1][self.field_length-1] != "B":
                    self.field_list[y+1][self.field_length-1] +=1
            
            
        #last, check over all the remaining squares
        #for these, all squares are guranteed to have boxes to it's left and right and top and bottom
        for y in range(1, self.field_height-2):
            for x in range(1, self.field_length-2):
                #here, if a bomb is found, there are eight cells to check
                print("cell y, x has been checked:", y, x)
                if self.field_list[y][x] == "B":
                    #top
                    if self.field_list[y+1][x] != "B":
                        self.field_list[y+1][x] +=1
                    #top right
                    if self.field_list[y+1][x+1] != "B":
                        self.field_list[y+1][x+1] +=1
                    #right
                    if self.field_list[y][x+1] != "B":
                        self.field_list[y][x+1] +=1
                    #bottom right
                    if self.field_list[y-1][x+1] != "B":
                        self.field_list[y-1][x+1] +=1
                    #bottom
                    if self.field_list[y-1][x] != "B":
                        self.field_list[y-1][x] +=1
                    #bottom left
                    if self.field_list[y-1][x-1] != "B":
                        self.field_list[y-1][x-1] +=1
                    #left
                    if self.field_list[y][x-1] != "B":
                        self.field_list[y][x-1] +=1
                    #top left
                    if self.field_list[y+1][x-1] != "B":
                        self.field_list[y+1][x-1] +=1
                        
    '''
    takes:
    first cell selection coordinates y and x
    
    returns:
    True if cell selected is invalid
    
    modified
    self.game_field_ui
    
    used for first selection. If the first selection is on a cell with a bomb, the bomb will be removed
    and another one will be placed randomly. Then, select_cell is called like a normal cell selection.
    '''
    def _select_first(self, y, x):
        if self._valid_cell(y, x):
            if self.field_list[y][x] == "B":
                self._relay_bombs(1, y, x)
            self.select_cell(y, x)
        else:
            return True
                        
    '''
    display field list displays the acutal information, not to be used in gameplay
    display field list ui is what will be used. It hides all the cells the uder has not unlocked
    '''
    def _display_field_list(self):
        print(" ", end = "")
        print(" ", end = "")
        print(" ", end ="")
        for x in range(0, self.field_length):
            print(" ", end = "")
            print(x, end = "")
            print(" ", end ="")
        print("")
        for y in range (0, self.field_height):
            print(" ", end = "")
            print(y, end = "")
            print(" ", end ="")
            for x in range (0, self.field_length):
                print(" ", end = "")
                print(self.field_list[y][x], end = "")
                print(" ", end = "")
            print("")       
            
    def _display_field_list_ui(self):
        print(" ", end = "")
        print(" ", end = "")
        print(" ", end ="")
        for x in range(0, self.field_length):
            print(" ", end = "")
            print(x, end = "")
            print(" ", end ="")
        print("")
        for y in range (0, self.field_height):
            print(" ", end = "")
            print(y, end = "")
            print(" ", end ="")
            for x in range (0, self.field_length):
                print(" ", end = "")
                print(self.field_list_ui[y][x], end = "")
                print(" ", end = "")
            print("")
    
    '''
    takes:
    coordinates of cell selected in y and x
    
    returns:
    True if cell is invalid
    
    modifies:
    self.game_field_ui
    
    function allows user to select a cell by inputing the x and y
    it changes field_list_ui, and only reads field_list
    it also can return False if there is a bomb on the cell
    '''
    def select_cell(self, y, x):
        if self._valid_cell(y, x):
            if self._valid_cell(y, x):
                if self.field_list[y][x] != "B":
                    self.field_list_ui[y][x] = self.field_list[y][x]
                    for i in self._return_neighbors(y, x):
                        if self.field_list[i[0]][i[1]] != "B":
                            self.select_cell(i[0], i[1])
        else:
            return True         
    '''
    these functions only help select_cell, and should not be acessed outside of it
    '''
    
    '''
    takes:
    cell coordinate in y and x
    
    returns:
    a list of lists, each nested list 2 numbers long representing the neighbors of the selected cell
    
    modifies:
    nothing
    
    the point of this function is to handle cells on the edge, where some neighbors are not included
    (eg, leftmost cell has no left neighbors)
    '''   
    def _return_neighbors(self, y, x):
        if y== 0:
            if x == 0:
                return [[0, 1],[1,1],[1, 0]]
            if x>0 and x<self.field_length-1:
                return [[0,x+1],[0,x-1],[1,x+1],[1,x],[1,x-1]]
            if x == self.field_length-1:
                return [[0, self.field_length-2],[1, self.field_length-1],[1,self.field_length-2]]
        if y>0 and y<self.field_height-1:
            if x == 0:
                return [[y+1, 0],[y+1,1],[y, 1], [y-1, 1], [y-1, 0]]
            if x>0 and x<self.field_length-1:
                return [[y+1,x],[y+1,x+1],[y,x+1],[y-1,x+1],[y-1,x],[y-1,x-1],[y-1,x],[y-1,x+1]]
            if x == self.field_length-1:
                return [[y+1,self.field_length-1],[y+1,self.field_length-2],[y,self.field_length-2],[y-1,self.field_length-1],[y-1,self.field_length-2]]
        if y == self.field_height-1:
            if x == 0:
                return [[self.field_height-2, 1],[self.field_height-1,1],[self.field_height-1, 0]]
            if x>0 and x<self.field_length-1:
                return [[self.field_height-2,x+1],[self.field_height-2,x-1],[self.field_height-1,x+1],[self.field_height-1,x],[self.field_height-1,x-1]]
            if x == self.field_length-1:
                return [[self.field_height-2, self.field_length-2],[self.field_height-1, self.field_length-1],[self.field_height-1,self.field_length-2]]
    
    '''
    the following functions relate with flagging
    '''
    '''
    take:
    flag coordinates in y and x
    
    return:
    nothing
    
    modify:
    self.field_list_ui
    
    plants a flag if the cell is not selected and exists
    '''
    def flag(self, y, x):
        if self._valid_cell(y, x):
            self.field_list_ui[y][x] = "F"
        else:
            print("this is not a valid cell to flag")
    
    '''
    take:
    flag coordinates in y and x
    
    return:
    nothing
    
    modify:
    self.field_list_ui
    
    removes a flag if the cell is flagged
    '''
    def unflag(self, x, y):
        if x < self.field_length-1:
            if y < self.field_height-1:
                if self.field_list_ui[y][x] == "F":
                    self.field_list_ui[y][x] = "-"
        else:
            print("this is not a valid cell to unflag")
    '''
    the following functions help runner run the game using all the above
    '''
    '''
    take:
    nothing
    
    return:
    False if, for every cell that is "-" on the self.field_list_ui (not selected), self.field_list is a bomb
    True if this is false for any one cell
    
    modify:
    self.field_list_ui
    
    check if every cell that has not been selected has a bomb.
    If this is true for all cells, then all non-bomb cells have been selected, and the game is over.
    If this is false for any one cell, then some cell that has not been selected does not contain a bomb,
    and the play still need to click it
    '''
    def check_status(self):
        game_over = False
        for y in range(0, self.field_height-1):
            for x in range(0, self.field_length-1):
                if self.field_list_ui[y][x] == "-":
                    if self.field_list[y][x] != "B":
                        game_over = False
                else:
                    game_over = True
        return game_over
        return True
    
    '''
    takes:
    cell coordinate in y and x
    
    returns:
    True if cell is in the range of field, and has not already been revealed
    
    modifies:
    nothing
    '''        
    def _valid_cell(self, y, x):
        if (str(x) in "1234567890") and (str(y) in "12345679890"):
            if x<self.field_length:
                if y<self.field_height:
                    if self.field_list_ui[y][x] == "-":
                        return True
    
    def return_solution(self):
        return self.field_list
            
            
            
            
            
            
            