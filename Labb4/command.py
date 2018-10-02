class Command:

	def __init__(self, name, inType:type, func = None, *subCom):
		self.parent = None
		self.name = name
		self.inType = inType
		self.func = func
		self.subCom = subCom

		for item in subCom:
			item.parent = self

	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		return (self.name == other)
		
	#Resolve: Try to feed command values into parent command's provided function.
	def resolve(*args):
		if parent == None:
			func(args)
		else:
			parent.resolve(args)

	def evaluate(commands:list, user:list):

		valid = []
		if user[0] in commands and len(user) > 1:

			user.append(None) #Until I can figure out a better program flow, None serves as a null terminator for the command parser.
			curr = []

			for sub in user:
				if sub in list(commands) + commands[user[0]] + [None]:
					if len(curr) > 0:
						valid.append(curr.copy())
						curr.clear()
				curr.append(sub)
			print(valid)