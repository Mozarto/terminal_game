class Character:

    sprite_adress = r"D:\dev\terminal_game\Assets\Character.txt"
    movement_speed = 5



    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.sprite_front = self.read(self.sprite_adress, 'front')
        self.sprite_right = self.read(self.sprite_adress, 'right')
        self.sprite_left = self.read(self.sprite_adress, 'left')
        self.sprite_back = self.read(self.sprite_adress, 'back')
        self.hitbox = [len(self.sprite_back), len(self.sprite_back[0])]
        self.current_sprite = self.sprite_front


    def read(self, file, sprite):
        rr = []  # Array for saving lines
        with open(file, 'rt') as fl:
            lines = fl.read()
            lines = lines[(lines.find(sprite + ' {') + len(sprite) + 3):(lines.find('} ' + sprite) - 1)]
        r2 = lines.split('\n')
        for i in r2:
            rr.append(list(i))
        return rr


    def move(self, direction, map):
        if direction == 'left' and (self.pos[1] - self.movement_speed) > 0:
            self.pos[1] -= self.movement_speed
            self.current_sprite = self.sprite_left
        elif direction == 'back' and (self.pos[0] - self.movement_speed) > 0:
            self.pos[0] -= self.movement_speed
            self.current_sprite = self.sprite_back
        elif direction == 'right' and (self.pos[1] + self.movement_speed) < map.width:
            self.pos[1] += self.movement_speed
            self.current_sprite = self.sprite_right
        elif direction == 'front' and (self.pos[0] + self.movement_speed) < map.height:
            self.pos[0] += self.movement_speed
            self.current_sprite = self.sprite_front
