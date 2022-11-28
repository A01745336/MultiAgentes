from mesa import Agent
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
        #Lista de las ubicaciones de los estacionamientos
        self.destinos = [(21, 9), (4,5), (4, 12), (5, 21),
                         (7, 10), (14, 18), (15, 2), (15, 5),
                         (15, 12), (14, 3), (20, 12), (20, 18),
                         (22, 3), (22, 21)]
        self.destiny = None
        self.vuelta = 0

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
                    if type(j) == Road:
                        self.model.grid.move_agent(self, i)
    # def selecionCarril(self):
    #    if(self.selecionCarril == 0 and cambioCarril >= 50):
    #        self.carril = 1
    #    elif(self.selecionCarril == 1 and cambioCarril >= 0):
    #        self.carril = 0

    def darVuelta(self):
        if(self.pos == (1, 9)):
            probabilidadVuelta = random.randint(1, 101)
            if(probabilidadVuelta >= 35):
                self.estado = 1
    
    def manejar(self):
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

    def step(self) -> None:
        # self.selecionCarril()
        if (self.model.schedule.steps == 2):
            self.empezarManejo()
        else:
            self.seleccionRuta()
            self.manejar()
            self.darVuelta()


class Traffic_Light(Agent):
    """
    Traffic light. Where the traffic lights are in the grid.
    """
    def __init__(self, unique_id, model, state = False, timeToChange = 10):
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

    def step(self):
        """ 
        To change the state (green or red) of the traffic light in case you consider the time to change of each traffic light.
        """
        # if self.model.schedule.steps % self.timeToChange == 0:
        #     self.state = not self.state
        pass

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
