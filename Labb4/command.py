class Command:

	def __init__(self, name, type, func = None, *subCom):
		self.parent = None
		self.name = name
		self.type = type
		self.func = func
		self.subCom = subCom

		for item in subCom:
			item.parent = self
		
	def resolve():
		if parent == None:
			func()
		else:
			parent.resolve(