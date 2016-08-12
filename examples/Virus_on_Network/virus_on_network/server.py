from mesa.visualization.modules import Network
from mesa.visualization.ModularVisualization import ModularServer

from virus_on_network.model import VirusModel


def portrayal(agent):
    """ This is how agents are displayed. """

    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "Filled": "true"}

    if agent:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
    return portrayal


width = 900
height = 500
num_agents = 40

network = Network(portrayal, width, height)
server = ModularServer(VirusModel, [network], "Network Example",
                       num_agents, width, height)

server.max_steps = 0
server.port = 8888
