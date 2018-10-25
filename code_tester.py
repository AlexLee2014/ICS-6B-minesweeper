'''
Created on Oct 24, 2018

@author: me
'''
from game_code import Field

game_field = Field.field(8, 9, 20)

print("stating board")
game_field._display_field_list()

print("hidden board")
game_field._display_field_list_ui()

print("select cell 4, 5")
game_field._select_first(4, 5)
game_field._display_field_list_ui()
