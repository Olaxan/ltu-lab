import types

class CommandParser:

	def __init__(self, *args, **kwargs):
		
		self.com = []
		return super().__init__(*args, **kwargs)

	def add_command(self, com : str, abb : str = None, help : str = None, *args, **kwargs):
		self.com.append(Command(com, abb, help, args, kwargs))

	def evaluate(self, commands : list):

class Command:

	def __init__(self, com : str, abb : str = None, help : str = None, *args, **kwargs):
		self.com = com
		self.abb = abb
		self.help = help
		return super().__init__(*args, **kwargs)
