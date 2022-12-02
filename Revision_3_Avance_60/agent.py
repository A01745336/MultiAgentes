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
             or self.pos == (6, 12) or self.pos == (7, 12) or self.pos == (16, 11)):
            if(self.vuelta <= 35):
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
            if type(j) == Traffic_Light and len(cellmates) <= 2:
                return j.state
            elif type(j) == Car:
                return True

    def posibilidadRevase(self):
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
        destinoPosible = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False,
            radius=1)
        for i in destinoPosible:
            if i == self.destiny:
                self.model.grid.move_agent(self, i)

    def step(self) -> None:
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

        if self.direccion is None:
            self.direccion = self.get_direction_of_cars()

        if self.mismoSemaforo is None:
            self.mismoSemaforo = self.get_partner()

        if self.semaforoCruce == ():
            self.semaforoCruce = self.get_opposing_traffic_lights()

        # Will get the number of cars that are in the next 3 positions
        self.carros = self.get_number_of_cars(5)
        # Get partner's and add it to self to get the total number of cars
        # in that street
        self.totalCarros = self.carros + \
                          self.get_number_cars_from_partner()

        # If the number of cars is greater than the opposing two traffic
        # lights,
        # turn green and turn red the two opposing traffic lights
        if self.totalCarros > self.get_opposing_traffic_lights_cars():
            self.state = False
            self.mismoSemaforo.state = False
            for agent in self.semaforoCruce:
                agent.state = True

        elif self.totalCarros == self.get_opposing_traffic_lights_cars():
            pass

    def get_opposing_traffic_lights(self):
        """
        Gets the two traffic lights opposing self
        Returns:
            list: list with the two opposing traffic lights
        """
        semaforoCruce = []
        for agent in self.model.grid.iter_neighbors(self.pos, moore=True,
                                                    radius=3):
            if isinstance(agent, Traffic_Light) and agent != self.mismoSemaforo:
                semaforoCruce.append(agent)
        return semaforoCruce

    def get_opposing_traffic_lights_cars(self):
        """
        Gets the number of cars following both traffic lights
        Returns:
            int: Sum of both traffic light cars
        """
        carrosCruce = 0
        for agent in self.semaforoCruce:
            carrosCruce += agent.carros
        return carrosCruce

    def get_partner(self):
        """
        Gets the traffic light next to self
        Returns:
            Traffic_Light: agent instance of partner
        """
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Traffic_Light):
                return agent

    def get_number_cars_from_partner(self):
        """
        Gets the number of cars of the traffic light next to self
        Returns:
            int: number of cars following partner traffic light
        """
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Traffic_Light):
                return agent.carros

    def get_number_of_cars(self, numPosiciones):
        """
        Gets the number of cars following x positions of the traffic light
        Args:
            number_positions (int): The amount of cells to check
        Returns:
            int: number of cars
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

    def get_direction_of_cars(self):
        """
        Returns where the cars are coming from according to the direction
        of the road
        Returns:
            string: direction of the road where the cars are coming from
            (Up, Down, Left, Right)
        """
        semaforoDireccion = self.get_partner_position()
        for agent in self.model.grid.iter_neighbors(self.pos, moore=False):
            if isinstance(agent, Road):
                if (semaforoDireccion in ("Up", "Down")) and (
                        agent.direction in ("Left", "Right")):
                    return agent.direction
                elif (semaforoDireccion in ("Left", "Right")) and (
                        agent.direction in ("Up", "Down")):
                    return agent.direction
        return None

    def get_partner_position(self):
        """
        Get if the partner is above, below, left or right of self
        Returns:
            string: direction of the partner (Up, Down, Left, Right)
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
