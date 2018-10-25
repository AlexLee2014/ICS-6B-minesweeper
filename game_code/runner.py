from game_code import Field

game_field = Field.field(8, 9, 15)

print("stating board")
game_field._display_field_list()

print("hidden board")
game_field._display_field_list_ui()