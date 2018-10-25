from game_code import Field

'''
Field takes all input as int
to make sure that python does not 
error when trying to convert an
invalid input into an int,
this function will be used to check
the input.

Field can handle if the input
in out of range.
'''
def is_int(input_string):
    out = True
    for i in str(input_string):
        if i not in "1234567890":
            return False
    return out


'''
set up field with dimensions and bomb count
loop untill a valid bomb count is entered
'''
field_setting = True
while field_setting:
    field_height_in = input("input a field height")
    field_length_in = input("input a field length")
    bomb_count_in = input("input a bomb count")
    #check if the input are all integers
    if is_int(field_length_in) and is_int(field_height_in) and is_int(bomb_count_in):
        #check if the number of bombs is valid
        if int(bomb_count_in) < int(field_height_in) * int(field_length_in):
            field_setting = False
        else:
            print("too many bombs for the field!")
    else:
        print("not valid dimensions")
game_field = Field.field(int(field_height_in), int(field_length_in), int(bomb_count_in))
game_field._display_field_list_ui()


'''
compute first cell selection
loop untill a valid cell is selected
'''
first_selecting = True
while first_selecting:
    first_y = input("select a y coordinate")
    first_x = input("select an x coordinate")
    #check if input if int
    if is_int(first_y) and is_int(first_x):
        #check if the dimensions are not out of range
        if game_field._select_first(int(first_y), int(first_x)):
            print("not valid coordinate")
        else:
            first_selecting = False
            game_field._display_field_list_ui()
    else:
        print("not valid coordinates")

'''
game main loop
'''
game_running = True

while game_running:
    
    game_running != game_field.check_status()