import types

class CommandParser:

	def __init__(self, *args, **kwargs):
		self.com = []
		return super().__init__(*args, **kwargs)

	def add_command(self, long : str, abb : str = None, desc : str = None, func : types.FunctionType = None):
		self.com.append(self.__Command(long, abb, desc, func))

	def command_exists(self, command, allowAbb = True):
		for c in self.com:
			if c.long == command or c.abb == command:
				return True
		return False

	def evaluate(self, commands : list):
		if self.command_exists(commands[0]):
			


	class __Command:

		def __init__(self, long : str, abb : str = None, desc : str = None, func : types.FunctionType = None, *args, **kwargs):
			self.long = long
			self.abb = abb
			self.desc = desc
			self.func = func
			self.subcom = []
			return super().__init__(*args, **kwargs)