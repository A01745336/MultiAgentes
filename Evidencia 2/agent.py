from mesa import Agent
import random


class Car(Agent):
    """
    Agent that moves randomly.
    Attributes:
        unique_id: Agent's ID
        direction: Randomly chosen direction chosen from one of eight
        directions
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
        self.destiny = random.choice(self.destinos)
        self.revasar = False

    def setDirection(self):
        # Descubrir forma de manejar
        ...

    def revase(self):
        """
        The agent can pass other cars
        """
        if(self.estado == 0 and self.pos[0] == 0):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] - 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 0 and self.pos[0] == 1):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] - 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 1 and self.pos[1] == 0):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] + 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 1 and self.pos[1] == 1):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] - 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 2 and self.pos[0] == 22):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] + 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 2 and self.pos[0] == 23):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] + 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 3 and self.pos[1] == 24):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] - 1)
            self.model.grid.move_agent(self, nuevaPosicion)
        elif(self.estado == 3 and self.pos[1] == 23):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] + 1)
            self.model.grid.move_agent(self, nuevaPosicion)

    def moverBajando(self):
        """
        The function moverBajando() takes in a self parameter and returns a
        new position for the agent
        """
        nuevaPosicion = (self.pos[0], self.pos[1] - 1)
        self.model.grid.move_agent(self, nuevaPosicion)

    def moverDerecha(self):
        """
        The function moverDerecha() takes in an agent and moves it one space
        to the right
        """
        nuevaPosicion = (self.pos[0] + 1, self.pos[1])
        self.model.grid.move_agent(self, nuevaPosicion)

    def moverSubiendo(self):
        """
        The function moverSubiendo() takes the agent's current position and
        moves it up one space
        """
        nuevaPosicion = (self.pos[0], self.pos[1] + 1)
        self.model.grid.move_agent(self, nuevaPosicion)

    def moverIzquierda(self):
        """
        The function moverIzquierda() takes in a self parameter and returns a
        new position for the agent
        """
        nuevaPosicion = (self.pos[0] - 1, self.pos[1])
        self.model.grid.move_agent(self, nuevaPosicion)

    def setDestiny(self):
        """
        The function setDestiny() is a method of the class car. It sets the
        destiny of the car to a random choice from the list of destinations
        """
        self.destiny = random.choice(self.destinos)

    def seleccionRuta(self):
        """
        If the car is in the top left corner, it can only go right. If it's in
        the bottom right corner, it can only go up. If it's in the top right
        corner, it can only go down. If it's in the bottom left corner, it can
        only go left. If it's in the top row, it can only go right. If it's in
        the bottom row, it can only go left. If it's in the left column, it can
        only go down. If it's in the right column, it can only go up. If it's
        in the middle, it can go in any direction
        """
        if(self.pos[0] == 0):
            if(self.pos[1] != 0):
                self.estado = 0
            elif(self.pos[1] == 0):
                self.estado = 1

        elif(self.pos[0] == 1):
            if(self.pos[1] >= 2 and self.pos[1] <= 23):
                self.estado = 0
            elif(self.pos[1] == 1):
                self.estado = 1

        elif(self.pos[0] == 23):
            if(self.pos[1] != 24):
                self.estado = 2
            elif(self.pos[1] == 24):
                self.estado = 3

        elif(self.pos[0] == 22):
            if(self.pos[1] != 24):
                self.estado = 2
            elif(self.pos[1] == 23 or self.pos[1] == 24):
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
            if(self.pos[0] <= 21 and self.pos[0] > 17):
                self.estado = 3
            elif(self.pos[0] <= 12 and self.pos[0] > 2):
                self.estado = 3

        elif(self.pos[1] == 8 or self.pos[1] == 9):
            if(self.pos[0] <= 21 and self.pos[0] > 17):
                self.estado = 1
            elif(self.pos[0] <= 12 and self.pos[0] > 2):
                self.estado = 1

    def empezarManejo(self):
        """
        If the agent is in a parking lot, it will move to the first road it
        finds.
        """
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

    def darVuelta(self):
        """
        If the car is in one of the positions listed, there is a 35% chance
        that the car will change
        direction.
        """
        self.vuelta = random.randint(1, 101)
        if(self.pos == (1, 9) or self.pos == (17, 8) or self.pos == (1, 8)
           or self.pos == (16, 1)):
            if(self.vuelta <= 35):
                self.estado = 1
        elif(self.pos == (13, 18) or self.pos == (13, 12) or self.pos ==
             (16, 11) or self.pos == (14, 12) or self.pos == (13, 17) or
             self.pos == (22, 12) or self.pos == (22, 11)):
            if(self.vuelta <= 35):
                self.estado = 3
        elif(self.pos == (6, 8) or self.pos == (7, 8) or self.pos == (13, 8)
             or self.pos == (14, 23) or self.pos == (13, 23) or self.pos ==
             (14, 8) or self.pos == (13, 9) or self.pos == (14, 9) or
             self.pos == (1, 9)):
            if(self.vuelta <= 35):
                self.estado = 0
        elif(self.pos == (17, 12) or self.pos == (16, 1) or self.pos == (17, 1)
             or self.pos == (6, 12) or self.pos == (7, 12) or
             self.pos == (16, 11)):
            if(self.vuelta <= 35):
                self.estado = 2

    def detener(self):
        """
        If the car is in the same cell as a traffic light, and there are no
        other cars in the cell, then return the state of the traffic light
        :return: The state of the traffic light.
        """
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
            if type(j) == Traffic_Light and len(cellmates) <= 2:
                return j.state
            elif type(j) == Car:
                return True

    def posibilidadRevase(self):
        """
        If the car is on the edge of the grid, it checks if the cell next to
        it is empty. If it is, it sets the car's revasar attribute to True.
        """
        cell1 = ()
        nuevaPosicion = ()
        if(self.estado == 0 and self.pos[0] == 0):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] - 1)
            cell1 = (self.pos[0], self.pos[1] - 1)
        elif(self.estado == 0 and self.pos[0] == 1):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] - 1)
            cell1 = (self.pos[0], self.pos[1] - 1)
        elif(self.estado == 1 and self.pos[1] == 0):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] + 1)
            cell1 = (self.pos[0] + 1, self.pos[1])
        elif(self.estado == 1 and self.pos[1] == 1):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] - 1)
            cell1 = (self.pos[0] + 1, self.pos[1])
        elif(self.estado == 2 and self.pos[0] == 22):
            nuevaPosicion = (self.pos[0] + 1, self.pos[1] + 1)
            cell1 = (self.pos[0], self.pos[1] + 1)
        elif(self.estado == 2 and self.pos[0] == 23):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] + 1)
            cell1 = (self.pos[0], self.pos[1] + 1)
        elif(self.estado == 3 and self.pos[1] == 24):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] - 1)
            cell1 = (self.pos[0] - 1, self.pos[1])
        elif(self.estado == 3 and self.pos[1] == 23):
            nuevaPosicion = (self.pos[0] - 1, self.pos[1] + 1)
            cell1 = (self.pos[0] - 1, self.pos[1])

        cellmates = self.model.grid.get_cell_list_contents(cell1)
        for j in cellmates:
            if type(j) == Car and len(cellmates) <= 2:
                self.revasar = True

    def manejar(self):
        """
        The function checks if the car can stop, if it can't, it checks if it
        can turn, if it can't, it checks if it can go forward, if it can't, it
        checks if it can go backwards, if it can't, it checks if it can go
        forward again, if it can't, it checks if it can go backwards again, if
        it can't, it checks if it can go forward again, if it can't, it checks
        if it can go backwards again, if it can't, it checks if it can go
        forward again, if it can't, it checks if it can go backwards again, if
        it can't, it checks if it can go forward again, if it can't, it checks
        if it can go backwards again, if it can't, it checks if it can go
        forward again, if it can't, it checks if it can go backwards again,
        if it can't, it checks if it can
        """
        self.darVuelta()
        posibleDetenecion = self.detener()
        if not posibleDetenecion:
            self.posibilidadRevase()
            if(self.estado == 0):
                self.moverBajando()
            elif(self.estado == 1):
                self.moverDerecha()
            elif(self.estado == 2):
                self.moverSubiendo()
            elif(self.estado == 3):
                self.moverIzquierda()
            if(self.revasar is True):
                self.revase()
        self.darVuelta()
        self.revasar = False

    def revisarDestino(self):
        """
        If the agent is next to its destination, it moves to that destination
        """
        destinoPosible = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False,
            radius=1)
        for i in destinoPosible:
            if i == self.destiny:
                self.model.grid.move_agent(self, i)

    def step(self) -> None:
        """
        The function step() is called every time step of the simulation
        """
        # self.selecionCarril()
        if (self.model.schedule.steps < 2):
            self.empezarManejo()
        else:
            self.seleccionRuta()
            if(self.pos == (0, 23)):
                self.estado = 0
            self.manejar()
            self.revisarDestino()


class Traffic_Light(Agent):
    """
    Traffic light. Where the traffic lights are in the grid.
    """
    def __init__(self, unique_id, model, state=False, time_to_change=10):
        super().__init__(unique_id, model)
        self.state = state
        self.timeToChange = time_to_change
        self.carros = 0
        self.direccion = None
        self.mismoSemaforo = None
        self.semaforoCruce = ()
        self.totalCarros = 0

    def step(self):
        """
        If the number of cars in the street is greater than the number of
        cars in the crossing, the traffic light in the street turns red
        and the traffic light in the crossing turns green
        """

        if self.direccion is None:
            self.direccion = self.direccionCalle()

        if self.mismoSemaforo is None:
            self.mismoSemaforo = self.get_partner()

        if self.semaforoCruce == ():
            self.semaforoCruce = self.get_opposing_traffic_lights()

        self.carros = self.numCarros(5)
        self.totalCarros = self.carros + \
                           self.numCarrosVecino()

        if self.totalCarros > self.numCarrosCruce():
            self.state = False
            self.mismoSemaforo.state = False
            for agent in self.semaforoCruce:
                agent.state = True

        elif self.totalCarros == self.numCarrosCruce():
            pass

    def direccionCalle(self):
        """
        If the agent is on a road, return the direction of the road
        :return: The direction of the road that the agent is on.
        """
        semaforoDireccion = self.posicionVecino()
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Road):
                if (semaforoDireccion in ("Up", "Down")) and (
                        agent.direction in ("Left", "Right")):
                    return agent.direction
                elif (semaforoDireccion in ("Left", "Right")) and (
                        agent.direction in ("Up", "Down")):
                    return agent.direction
        return None

    def numCarrosCruce(self):
        """
        It returns the number of cars in the intersection
        :return: The number of cars in the intersection.
        """
        carrosCruce = 0
        for agent in self.semaforoCruce:
            carrosCruce += agent.carros
        return carrosCruce

    def numCarrosVecino(self):
        """
        It returns the number of cars in the cell next to the traffic light
        :return: The number of cars in the neighborhood of the traffic light.
        """
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Traffic_Light):
                return agent.carros

    def posicionVecino(self):
        """
        It returns the position of the traffic light relative to the car
        :return: The position of the traffic light in relation to the car.
        """
        mismoSemaforoPos = ()
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Traffic_Light):
                mismoSemaforoPos = agent.pos

        if self.pos[0] - mismoSemaforoPos[0] > 0:
            return "Left"
        elif self.pos[0] - mismoSemaforoPos[0] < 0:
            return "Right"
        elif self.pos[1] - mismoSemaforoPos[1] > 0:
            return "Down"
        elif self.pos[1] - mismoSemaforoPos[1] < 0:
            return "Up"

    def numCarros(self, numPosiciones):
        """
        It returns the number of cars in the street in front of the car
        :param numPosiciones: The number of positions to check for cars
        :return: The number of cars in the street
        """
        carros = 0
        numCalles = numPosiciones
        step = (25, 25)
        for x in range(0, numPosiciones + 1):
            if self.direccion == "Up":
                step = (self.pos[0], self.pos[1] - x)
            elif self.direccion == "Down":
                step = (self.pos[0], self.pos[1] + x)
            elif self.direccion == "Left":
                step = (self.pos[0] + x, self.pos[1])
            elif self.direccion == "Right":
                step = (self.pos[0] - x, self.pos[1])

            if self.model.grid.out_of_bounds(step):
                carros += 0
            else:
                cellmates = self.model.grid.get_cell_list_contents([
                    step])
                for agent in cellmates:
                    if isinstance(agent, Car):
                        carros += 1
            numCalles -= 1
        return carros

    def get_opposing_traffic_lights(self):
        """
        Gets the two traffic lights opposing self
        Returns:
            list: list with the two opposing traffic lights
        """
        opposing_traffic_lights = []
        for agent in self.model.grid.iter_neighbors(self.pos, moore=True,
                                                    radius=3):
            if isinstance(agent, Traffic_Light) and agent != self.mismoSemaforo:
                opposing_traffic_lights.append(agent)
        return opposing_traffic_lights

    def get_partner(self):
        """
        Gets the traffic light next to self
        Returns:
            Traffic_Light: agent instance of partner
        """
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Traffic_Light):
                return agent


class Destination(Agent):
    """
    Destination agent. Where each car should go.
    """
    def __init__(self, unique_id, model):
        """
        The function __init__() is a constructor that is called when an object
        of a class is instantiated

        :param unique_id: The unique ID of the agent
        :param model: The model that the agent is a part of
        """
        super().__init__(unique_id, model)

    def step(self):
        """
        It does nothing.
        """
        pass


class Obstacle(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid.
    """
    def __init__(self, unique_id, model):
        """
        The function __init__() is a constructor that is called when an object
        of a class is instantiated

        :param unique_id: The unique ID of the agent
        :param model: The model that the agent is a part of
        """
        super().__init__(unique_id, model)

    def step(self):
        """
        It does nothing.
        """
        pass


class Road(Agent):
    """
    Road agent. Determines where the cars can move, and in which direction.
    """
    def __init__(self, unique_id, model, direction="Left"):
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
        """
        It does nothing.
        """
        pass
