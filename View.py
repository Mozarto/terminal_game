import sys
import os

class View:


    def __init__(self, width, height, chara_pos):
        self.width = width
        self.height = height
        self.pos = self.define_pos(chara_pos)
        self.chara_pos = self.trasnlate_pos(chara_pos)
        self.screen = self.create_screen()


    def print_on_scren(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        print('')
        for lines in range(len(self.screen)):
            for char in range(len(self.screen[lines])):
                sys.stdout.write(self.screen[lines][char])
            sys.stdout.write('\n')

    def create_screen(self):
        screen = []
        for lines in range(self.height):
            screen.append([])
            for char in range(self.width):
                screen[lines].append('.') #serve pra mesma coisa q o else lá na frente, deixar a borda do mapa pontilhada
        return screen

    def update_screen(self, map, chara):
        self.screen = self.create_screen()
        self.pos = self.define_pos(chara.pos)


        for lines in range(len(self.screen)):
            for char in range(len(self.screen[lines])):
                if (self.pos[0]+lines > 0) or (self.pos[1] + char > 0):
                    if self.pos[0] + lines < len(map.map) and self.pos[1] + char < len(map.map[0]):
                        self.screen[lines][char] = map.map[self.pos[0]+lines][self.pos[1]+char]
                    #else:
                        #self.screen[lines][char] = "."

        self.coordinate_ui(chara.pos)



        for lines in range(len(chara.current_sprite)):
            for char in range(len(chara.current_sprite[lines])):
                self.screen[self.chara_pos[0]+lines][self.chara_pos[1]+char] = chara.current_sprite[lines][char]

        self.update_map(map)



    def define_pos(self, char_pos):
        return [int(char_pos[0]-(self.height-5)/2), int(char_pos[1]-(self.width-5)/2)]

    def trasnlate_pos(self, map_chara_pos):
        return [int(map_chara_pos[0] - self.pos[0]), int(map_chara_pos[1] - self.pos[1])]

    def update_map(self, map):
        """for object in range(len(self.screen)):
            # line
            for line in range(len(self.screen)):
                # char
                for char in range(len(self.screen[0])):
                    if self.pos[0] + line < len(map.map) and self.pos[1] + char < len(map.map[0]):
                        map.map[self.pos[0] + line][self.pos[1] + char] = self.screen[line][char]"""
        #As informações do mapa devem mudar, depois a aparência. Desse jeito só muda a aparência
        pass

    def coordinate_ui(self, pos):
        cor_string = list("[x: "+str(pos[1])+", y: "+str(pos[0])+"]")
        for i in range(len(cor_string)):
            self.screen[self.height-1][self.width-len(cor_string)+i] = cor_string[i]