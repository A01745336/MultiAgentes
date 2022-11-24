from trafficModel import *
from mesa.visualization.modules import ChartModule
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portayal(agent):
    """
    It returns a dictionary that describes how the agent should be drawn

    :param agent: the agent to be portrayed
    :return: a dictionary with the color, shape, radius and layer of the agent.
    """
    portayal = {"Filled": "true"}

    if (type(agent) == Parking):
        portayal["Shape"] = "rect"
        portayal["w"] = 1
        portayal["h"] = 1
        portayal["Layer"] = 0
        portayal["Color"] = "orange"

    elif (type(agent) == Roads):
        portayal["Color"] = "black"
        portayal["Shape"] = "rect"
        portayal["w"] = 1
        portayal["h"] = 1
        portayal["Layer"] = 0

    elif (type(agent) == Carro):
        portayal["Color"] = "green"
        portayal["Shape"] = "circle"
        portayal["r"] = 0.8
        portayal["Layer"] = 1

    else:
        portayal["Color"] = "blue"
        portayal["Shape"] = "rect"
        portayal["w"] = 1
        portayal["h"] = 1
        portayal["Layer"] = 0

    return portayal


grid = CanvasGrid(agent_portayal, 24, 25, 500, 500)


server = ModularServer(TrafficModel,
                       [grid],
                       "Traffic Model",
                       {"carros": 5, "semaforos": 5,
                        "time": 580, "width": 24, "height": 25})
server.port = 8521
server.launch()
