from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agent import *
import random
import json


class RandomModel(Model):
    """
    Creates a new model with random agents.
    Args:
        N: Number of agents in the simulation
    """
    def __init__(self, N):

        dataDictionary = json.load(open("mapDictionary.json"))

        self.traffic_lights = []

        with open('Base.txt') as baseFile:
            lines = baseFile.readlines()
            self.width = len(lines[0]) - 1
            self.height = len(lines)
            self.parkings: list[tuple] = [(2, 15), (3, 19), (3, 22), (5, 4),
                                          (5, 15), (10, 7), (12, 4), (12, 15),
                                          (12, 20), (18, 14), (18, 20), (19, 2),
                                          (21, 5), (21, 22)]
            self.grid = MultiGrid(self.width, self.height, torus=False) 
            self.schedule = RandomActivation(self)

            for r, row in enumerate(lines):
                for c, col in enumerate(row):
                    if col in ["v", "^", ">", "<"]:
                        agent = Road(f"r_{r*self.width+c}", self, dataDictionary[col])
                        self.grid.place_agent(agent, (c, self.height - r - 1))

                    elif col in ["S", "s"]:
                        agent = Traffic_Light(f"tl_{r*self.width+c}", self, False if col == "S" else True, int(dataDictionary[col]))
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        self.schedule.add(agent)
                        self.traffic_lights.append(agent)

                    elif col == "#":
                        agent = Obstacle(f"ob_{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))

                    elif col == "D":
                        agent = Destination(f"d_{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))

        self.cars = N
        self.running = True
        self.current_id = 0

        salida = self.parkings.copy()
        while(len(salida) > 0):
            lugarSalida = random.choice(salida)
            auto = Car("Carro " + str(self.next_id()), self)
            self.schedule.add(auto)
            self.grid.place_agent(auto, lugarSalida)
            salida.remove(lugarSalida)

    def step(self):
        '''Advance the model by one step.'''
        if self.schedule.steps % 10 == 0:
            for agent in self.traffic_lights:
                agent.state = not agent.state
        self.schedule.step()
