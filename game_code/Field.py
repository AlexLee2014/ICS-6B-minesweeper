'''
Created on Oct 24, 2018

@author: me
'''
from Crypto.Random.random import randint
class field:
    def __init__(self, x, y, bombs):
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
    def _new_field(self, x, y):
        for y in range(0, self.field_height):
            self.field_list.append([])
            for x in range(0, self.field_length):
                self.field_list[y].append(0)
        for y in range(0, self.field_height):
            self.field_list_ui.append([])
            for x in range(0, self.field_length):
                self.field_list_ui[y].append("-")
    
    def _lay_bombs(self, bombs):
        bomb_count = 0
        while bomb_count < bombs:
            x = randint(0, self.field_height-2)
            y = randint(0, self.field_height-2)
            if self.field_list[y][x] == 0:
                self.field_list[y][x] = "B"
                bomb_count += 1       
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
    display field list displays the acutal information, not to be used in gmaeplay
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
    function allows user to select a cell by inputing the x and y
    it changes field_list_ui, and only reads field_list
    it also can return False if there is a bomb on the cell
    '''
    def select_cell(self, x, y):
        if self.field_list[y][x] != "B":
            self.field_list_ui[y][x] = self.field_list[y][x]
            
        else:
            return False         
            
            
            