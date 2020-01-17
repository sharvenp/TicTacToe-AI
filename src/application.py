
from view import View
from model import Model

from human_player import HumanPlayer
from agent_player import AgentPlayer

if __name__ == '__main__':


	model = Model()

	p1 = HumanPlayer(model)
	p2 = HumanPlayer(model)

	v = View(p1, p2)

	model.add_observer(v)

	v.launch()