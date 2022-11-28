from mesa import Agent
from roadfuntionality import *
import random


class Car(Agent):
    """
    Agent that moves randomly.
    Attributes:
        unique_id: Agent's ID
        direction: Randomly chosen direction chosen from one of eight directions
    """
    def __init__(self, unique_id, model):
        """
        Creates a new random agent.
        Args:
            unique_id: The agent's ID
            model: Model reference for the agent
        """
        super().__init__(unique_id, model)
        self.estado = None
        self.direccion = None
        self.carril = None
        self.destinos = [(2, 15), (3, 19), (3, 22), (5, 4),
                         (5, 15), (10, 7), (12, 4), (12, 15),
                         (12, 20), (18, 14), (18, 20), (19, 2),
                         (21, 5), (21, 22)]
        self.destiny = None
        self.vuelta = 0
        self.posInicial = None

    def setDirection(self):
        # Descubrir forma de manejar
        ...

    def moverBajando(self):
        nuevaPosicion = (self.pos[0], self.pos[1] - 1)
        self.model.grid.move_agent(self, nuevaPosicion)

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
                self.estado = 1

    def obtenerRutaObtima(self):
        rutaOptima = shortest_path()

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
                    if type(j) == Road:
                        self.model.grid.move_agent(self, i)
    # def selecionCarril(self):
    #    if(self.selecionCarril == 0 and cambioCarril >= 50):
    #        self.carril = 1
    #    elif(self.selecionCarril == 1 and cambioCarril >= 0):
    #        self.carril = 0

    def darVuelta(self):
        if(self.pos == (1, 9) or self.pos == (17, 8)):
            probabilidadVuelta = random.randint(1, 101)
            if(probabilidadVuelta >= 35):
                self.estado = 1
        elif(self.pos == (13, 18) or self.pos == (13, 12) or self.pos == (16, 11)):
            probabilidadVuelta = random.randint(1, 101)
            if(probabilidadVuelta >= 35):
                self.estado = 3
        elif(self.pos == (6, 8) or self.pos == (13, 8) or self.pos == (14, 23)):
            probabilidadVuelta = random.randint(1, 101)
            if(probabilidadVuelta >= 35):
                self.estado = 0
        elif(self.pos == (17, 12) or self.pos == (16, 1)):
            probabilidadVuelta = random.randint(1, 101)
            if(probabilidadVuelta >= 35):
                self.estado = 2

    def detener(self):
        if(self.estado == 0):
            cell = (self.pos[0], self.pos[1] - 1)
        elif(self.estado == 1):
            cell = (self.pos[0] + 1, self.pos[1])
        elif(self.estado == 2):
            cell = (self.pos[0], self.pos[1] + 1)
        elif(self.estado == 3):
            cell = (self.pos[0] - 1, self.pos[1])

        cellmates = self.model.grid.get_cell_list_contents(cell)
        for j in cellmates:
            if type(j) == Traffic_Light:
                return j.state
            elif type(j) == Car:
                return True

    def manejar(self):
        self.darVuelta()
        posibleDetenecion = self.detener()
        if not posibleDetenecion:
            if(self.estado == 0):
                self.moverBajando()
            elif(self.estado == 1):
                self.moverDerecha()
            elif(self.estado == 2):
                self.moverSubiendo()
            elif(self.estado == 3):
                self.moverIzquierda()
        elif(self.estado == 5):
            self.model.grid.move_agent(self, self.pos)

    def step(self) -> None:
        # self.selecionCarril()
        if (self.model.schedule.steps < 2):
            self.empezarManejo()
        else:
            self.seleccionRuta()
            self.manejar()
            self.darVuelta()


class Traffic_Light(Agent):
    """
    Traffic light. Where the traffic lights are in the grid.
    """
    def __init__(self, unique_id, model, state=False, timeToChange=10):
        super().__init__(unique_id, model)
        """
        Creates a new Traffic light.
        Args:
            unique_id: The agent's ID
            model: Model reference for the agent
            state: Whether the traffic light is green or red
            timeToChange: After how many step should the traffic light change color 
        """
        self.state = state
        self.timeToChange = timeToChange
        self.mismoSemaforo = None
        self.semaforoCruce = None
        self.semaforosX = []
        self.semaforosY = []
        self.carros = 0

    def step(self):
        """
        To change the state (green or red) of the traffic light in case you consider the time to change of each traffic light.
        """
        if(self.pos[0] == 0 or self.pos[0] == 1 or self.pos[0] == 6 or
           self.pos[0] == 7 or self.pos[0] == 13 or self.pos[0] == 14 or
           self.pos[0] == 16 or self.pos[0] == 17 or self.pos[0] == 22 or
           self.pos[0] == 23):
            self.semaforosX.append(self)
        else:
            self.semaforosY.append(self)

        if self.mismoSemaforo is None:
            posibleSemaforo = self.model.grid.get_neighborhood(
                self.pos,
                moore=False,
                include_center=False,
                radius=1)
            for i in posibleSemaforo:
                cellmates = self.model.grid.get_cell_list_contents(i)
                for j in cellmates:
                    if type(j) == Traffic_Light:
                        self.mismoSemaforo = j
        if self.semaforoCruce is None:
            posibleSemaforo = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False,
                radius=1)
            for i in posibleSemaforo:
                cellmates = self.model.grid.get_cell_list_contents(i)
                for j in cellmates:
                    if type(j) == Traffic_Light and j != self.mismoSemaforo:
                        self.semaforoCruce = j
        
        # if self.state is False:
        #     print(f'Carros antes de contar {self.carros}')
        #     self.contarCarros()
        #     print(f'Carros despues de contar {self.carros}')

    def contarCarros(self):
        if self.mismoSemaforo is None:
            posibleSemaforo = self.model.grid.get_neighborhood(
                self.pos,
                moore=False,
                include_center=False,
                radius=3)
            if posibleSemaforo.pos[0] == self.pos[0] and self in self.semaforosX:
                for i in posibleSemaforo:
                    cellmates = self.model.grid.get_cell_list_contents(i)
                    for j in cellmates:
                        if type(j) == Car:
                            self.carros += 1
            elif posibleSemaforo.pos[1] == self.pos[1] and self in self.semaforosY:
                for i in posibleSemaforo:
                    cellmates = self.model.grid.get_cell_list_contents(i)
                    for j in cellmates:
                        if type(j) == Car:
                            self.carros += 1

class Destination(Agent):
    """
    Destination agent. Where each car should go.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        pass


class Obstacle(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        pass


class Road(Agent):
    """
    Road agent. Determines where the cars can move, and in which direction.
    """
    def __init__(self, unique_id, model, direction= "Left"):
        """
        Creates a new road.
        Args:
            unique_id: The agent's ID
            model: Model reference for the agent
            direction: Direction where the cars can move
        """
        super().__init__(unique_id, model)
        self.direction = direction

    def step(self):
        pass
