import Character
import Map
import View
import Loop

def main():
    type_game = ''
    while not (type_game.lower() == 'n' or type_game.lower() == 'l'):
        type_game = input("New Game [N]\nLoad Game[L]\n")
    if type_game.lower() == 'n':
        new_game()
    elif type_game.lower() == 'l':
        load_game()


def new_game():
    name_character = input("Name your character:")
    map = Map.Map()
    chara = Character.Character(name_character, [int((map.height - 5)/2), int((map.width - 5)/2)])
    view = View.View(105, 35, chara.pos)
    view.update_screen(map, chara)
    Loop.loop(view, chara, map)



def load_game():
    pass


main()