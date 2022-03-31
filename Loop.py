import keyboard

def loop(view, chara, map):
    running = True
    fps = 100
    counter_fps = 0
    while running == True:
        movement_key = ""
        if keyboard.is_pressed('w'):
            movement_key = 'back'
        elif keyboard.is_pressed('d'):
            movement_key = 'right'
        elif keyboard.is_pressed('s'):
            movement_key = 'front'
        elif keyboard.is_pressed('a'):
            movement_key = 'left'
        elif keyboard.is_pressed('esc'):
            running = False



        view.update_screen(map, chara)
        counter_fps+=1
        if counter_fps > fps:
            view.print_on_scren()
            counter_fps = 0
            chara.move(movement_key, map)

    view.update_map(map)
    map.saveMap()

























