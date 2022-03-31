import random

class Map:
    width = 995
    height = 505
    indexForObjectPlacement = int((width + height) /(2 * 2))
    contents = []
    map = []
    length_of_grass = 6
    entities =[]
    entities_old = []

    def __init__(self):
        self.createMap()

    def random(self, range):
        return int(random.random()*range)

    def createMap(self):
        self.createGrass()
        self.putMoveableObjects()

        #line
        for i in range(self.height):
            self.map.append([])
            #char
            for j in range(self.width):
                line = ""
                self.map[i].append(" ")

        self.putObjects()


    def readMap(self, file):
        rr = []  # Array for saving lines
        with open(file, 'rt') as fl:
            lines = fl.read()
        r2 = lines.split('\n')
        for i in r2:
            rr.append(list(i))
        return rr




    def putObjects(self):
        for object in range(len(self.contents)):
            #line
            for line in range(self.contents[object].hitbox[0]):
                #char
                for char in range(self.contents[object].hitbox[1]):
                   self.map[self.contents[object].pos[0]+line][self.contents[object].pos[1]+char] = \
                        self.contents[object].sprite[line][char]



    def hitboxCHecking(self, object):
        pass



    def createGrass(self):
        for i in range(self.indexForObjectPlacement):
            sprite = self.read(r'D:\dev\terminal_game\Assets\Contents.txt', "grass_"+str(self.random(self.length_of_grass)))
            self.contents.append(Grass(("g"+str(i)), sprite, [self.height, self.width]))



    def saveMap(self):
        map = self.colapse()
        with open(r'D:\dev\terminal_game\Maps\test.txt', 'w') as f:
            f.write(map)

    def read(self, name, sprite):
        rr = []  # Array for saving lines
        with open(name, 'rt') as fl:
            lines = fl.read()
            lines = lines[(lines.find(sprite + ' {') + len(sprite) + 3):(lines.find('} ' + sprite) - 1)]
        r2 = lines.split('\n')
        for i in r2:
            rr.append(list(i))
        return rr


    def colapse(self):
        final_string = ""
        for line in self.map:
            for char in line:
                final_string+=char
            final_string+="\n"
        return final_string

    def putMoveableObjects(self):
        if self.entities_old != []:
            #erasing previous position
            for object in range(len(self.entities_old)):
                # line
                for line in range(self.entities_old[object].hitbox[0]):
                    #char
                    for char in range(self.entities_old[object].hitbox[1]):
                        self.map[self.entities[object].pos[0] + line][self.entities[object].pos[1] + char] = " "

        #inputing new position
        for object in range(len(self.entities)):
            #line
            for line in range(self.entities[object].hitbox[0]):
                #char
                for char in range(self.entities[object].hitbox[1]):
                    self.map[self.entities[object].pos[0]+line][self.entities[object].pos[1]+char] = \
                        self.entities[object].sprite[line][char]

            self.entities_old[object] = self.entities_[object]




class Grass:
    def __init__(self, id, sprite, map):
        self.id = id
        self.sprite = sprite
        self.hitbox = [len(sprite), len(sprite[0])] #quant de listas, quant de char por lista
        self.pos = self.calculate_pos(map)

    def calculate_pos(self, map):
        return [self.random(0, map[0]-self.hitbox[0]), self.random(0, map[1]-self.hitbox[1])]


    def random(self, rangeDown, rangeUp):
        return int(random.random()*rangeUp+rangeDown)



