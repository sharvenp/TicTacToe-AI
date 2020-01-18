
from view import TicTacToeView
from model import TicTacToe

from human_player import HumanPlayer
from agent_player import AgentPlayer

if __name__ == '__main__':


	model = TicTacToe()

	p1 = HumanPlayer(model)
	p2 = HumanPlayer(model)

	v = TicTacToeView(p1, p2)

	model.add_observer(v)

	v.launch()