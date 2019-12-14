#!/usr/bin/python3

class SyntaxTree :
	def __init__(self):
		self.data     = None
		self.children = []

	def add_prod(self,stack_top,production = None):
		# None None -> data child
		# data None -> None child
		# data chid -> pass
		if not self.data: # Cria raiz e filhos
			self.data = stack_top
			if not self.children and production: # Se vai ter filhos
				for p in production:
					aux = SyntaxTree()
					if p[0] == "nterm":
						aux.add_prod(p[1])
					else:
						aux.add_prod(p[0])
					self.children.append(aux)
			return True
		else:
			if self.data != stack_top: # Procurando onde adicionar nova producoes
				if self.children:
					for child in self.children:
						if(child.add_prod(stack_top,production=production)):
							return True
				return False
			else:
				print(production)
				for p in production:
					aux = SyntaxTree()
					if p[0] == "nterm":
						aux.add_prod(p[1])
					else:
						aux.add_prod(p[0])
					self.children.append(aux)
				return True 

	def pre_ordem(self):
		print(self.data)
		if self.children:
			for child in self.children:
				child.pre_ordem()

	def add_child(self, obj):
		self.children.append(obj)
