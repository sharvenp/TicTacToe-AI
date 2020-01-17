
class Observable:

	def __init__(self):
		self.observers = []

	def notify_observers(self):

		for o in self.observers:
			o.update(self)