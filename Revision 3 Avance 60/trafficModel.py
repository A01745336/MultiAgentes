import mesa
import random


class Carro(mesa.Agent):
    def __init__(self, unique_id: str, model: mesa.Model) -> None:
        super().__init__(unique_id, model)
        self.estado = None
        self.direccion = None
        self.carril = None
        self.destinos = [(2, 15), (3, 19), (3, 22), (5, 4),
                         (5, 15), (10, 7), (12, 4), (12, 15),
                         (12, 20), (18, 14), (18, 20), (19, 2),
                         (21, 5), (21, 22)]
        self. destiny = None
        self.vuelta = False
        # global vuelta = random.randint(1, 101)
        # global cambioCarril = random.randint(1, 101)

    def setDirection(self):
        # Descubrir forma de manejar
        ...

    def moverBajando(self):
        nuevaPosicion = (self.pos[0], self.pos[1] - 1)
        self.model.grid.move_agent(self, nuevaPosicion)
        # self.movimientos += 1

    def moverDerecha(self):
        nuevaPosicion = (self.pos[0] + 1, self.pos[1])
        self.model.grid.move_agent(self, nuevaPosicion)

    def moverSubiendo(self):
        nuevaPosicion = (self.pos[0], self.pos[1] + 1)
        self.model.grid.move_agent(self, nuevaPosicion)

    def moverIzquierda(self):
        nuevaPosicion = (self.pos[0] - 1, self.pos[1])
        self.model.grid.move_agent(self, nuevaPosicion)

    def setDestiny(self):
        self.destiny = random.choice(self.destinos)

    def seleccionRuta(self):
        if(self.pos[0] == 0):
            if(self.pos[1] != 0):
                self.estado = 0
            elif(self.pos[1] == 0):
                self.estado = 1

        elif(self.pos[0] == 1):
            if(self.pos[1] != 1):
                self.estado = 0
            elif(self.pos[1] == 1):
                self.estado = 1

        elif(self.pos[0] == 22):
            if(self.pos[1] != 23):
                self.estado = 2
            elif(self.pos[1] == 23):
                self.estado = 3

        elif(self.pos[0] == 23):
            if(self.pos[1] != 24):
                self.estado = 2
            elif(self.pos[1] == 24):
                self.estado = 3

        elif(self.pos[0] == 6 or self.pos[0] == 7):
            if(self.pos[1] > 12 and self.pos[1] <= 16):
                self.estado = 2
            elif(self.pos[1] <= 7 and self.pos[1] > 2):
                self.estado = 0

        elif(self.pos[0] == 13 or self.pos[0] == 14):
            if(self.pos[1] <= 22 and self.pos[1] > 13):
                self.estado = 0
            elif(self.pos[1] <= 7 and self.pos[1] > 2):
                self.estado = 0

        elif(self.pos[0] == 16 or self.pos[0] == 17):
            if(self.pos[1] <= 22 and self.pos[1] > 13):
                self.estado = 2
            elif(self.pos[1] <= 7 and self.pos[1] > 2):
                self.estado = 2

        if(self.pos[1] == 23):
            if(self.pos[0] != 1):
                self.estado = 3

        elif(self.pos[1] == 1):
            if(self.pos[0] != 22):
                self.estado = 1

        elif(self.pos[1] == 17 or self.pos[1] == 18):
            if(self.pos[0] <= 12 and self.pos[0] > 2):
                self.estado = 3

        elif(self.pos[1] == 11 or self.pos[1] == 12):
            if(self.pos[0] <= 21 and self.pos[0] > 2):
                self.estado = 3

        elif(self.pos[1] == 8 or self.pos[1] == 9):
            if(self.pos[0] >= 2 and self.pos[0] < 21):
                self.estado = 3

    def empezarManejo(self):
        if (self.pos in self.model.parkings):
            salidasPosibles = self.model.grid.get_neighborhood(
                self.pos,
                moore=False,
                include_center=False,
                radius=1)
            for i in salidasPosibles:
                cellmates = self.model.grid.get_cell_list_contents(i)
                for j in cellmates:
                    if type(j) == Roads:
                        self.model.grid.move_agent(self, i)
    # def selecionCarril(self):
    #    if(self.selecionCarril == 0 and cambioCarril >= 50):
    #        self.carril = 1
    #    elif(self.selecionCarril == 1 and cambioCarril >= 0):
    #        self.carril = 0

    def step(self) -> None:
        # self.selecionCarril()
        self.empezarManejo()
        self.seleccionRuta()
        if(self.estado == 0):
            self.moverBajando()
        elif(self.estado == 1):
            self.moverDerecha()
        elif(self.estado == 2):
            self.moverSubiendo()
        elif(self.estado == 3):
            self.moverIzquierda()
        elif(self.estado == 4):
            self.model.grid.move_agent(self, self.pos)


class Semaforo(mesa.Agent):
    def __init__(self, unique_id: str, model: mesa.Model) -> None:
        super().__init__(unique_id, model)


class Parking(mesa.Agent):
    def __init__(self, unique_id: str, model: mesa.Model) -> None:
        super().__init__(unique_id, model)


class Roads(mesa.Agent):
    def __init__(self, unique_id: int, model: mesa.Model) -> None:
        super().__init__(unique_id, model)


class Edificios(mesa.Agent):
    def __init__(self, unique_id: int, model: mesa.Model) -> None:
        super().__init__(unique_id, model)


class TrafficModel(mesa.Model):
    def __init__(self, carros, semaforos, time, width, height) -> None:
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.cells = width * height
        self.parkings: list[tuple] = [(2, 15), (3, 19), (3, 22), (5, 4),
                                      (5, 15), (10, 7), (12, 4), (12, 15),
                                      (12, 20), (18, 14), (18, 20), (19, 2),
                                      (21, 5), (21, 22)]
        self.roads: list[tuple] = []
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.time = time
        self.running = True
        self.current_id = 0
        self.cars = carros
        self.lights = semaforos

        salida = self.parkings.copy()

        for i in range(len(self.parkings)):
            x = self.parkings[i][0]
            y = self.parkings[i][1]
            parking = Parking("Parking " + str(i), self)
            self.schedule.add(parking)
            self.grid.place_agent(parking, (x, y))

        for x in range(2):
            for y in range(25):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
        for x in range(22, 24):
            for y in range(25):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
        for y in range(2):
            for x in range(2, 23):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
        for y in range(23, 25):
            for x in range(2, 23):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)

        for x in range(2, 15):
            for y in range(17, 19):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)

        for x in range(2, 23):
            for y in range(11, 13):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
            for y in range(8, 10):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)

        for x in range(6, 8):
            for y in range(13, 17):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
            for y in range(2, 8):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)

        for x in range(13, 15):
            for y in range(19, 23):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
            for y in range(13, 17):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
            for y in range(2, 8):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)

        for x in range(16, 18):
            for y in range(13, 23):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)
            for y in range(2, 8):
                pos = (x, y)
                self.roads.append(pos)
                road = Roads(self.next_id(), self)
                self.schedule.add(road)
                self.grid.place_agent(road, pos)

        for x in range(13, 15):
            pos = (x, 10)
            self.roads.append(pos)
            road = Roads(self.next_id(), self)
            self.schedule.add(road)
            self.grid.place_agent(road, (x, 10))
        for x in range(16, 18):
            pos = (x, 10)
            self.roads.append(pos)
            road = Roads(self.next_id(), self)
            self.schedule.add(road)
            self.grid.place_agent(road, (x, 10))

        for x in range(width):
            for y in range(height):
                pos = (x, y)
                if(pos not in self.roads and pos not in self.parkings):
                    build = Edificios(self.next_id(), self)
                    self.schedule.add(build)
                    self.grid.place_agent(build, pos)

        while(len(salida) > 0):
            lugarSalida = random.choice(salida)
            auto = Carro("Carro " + str(self.next_id()), self)
            self.schedule.add(auto)
            self.grid.place_agent(auto, lugarSalida)
            salida.remove(lugarSalida)

    def step(self) -> None:
        self.schedule.step()
