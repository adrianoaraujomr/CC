#!/usr/bin/python3

from lex import Token

# gram       = nterm -> [derivations]
grammar = {
"I" : [[("rwd","programa"),("nterm","B")]],
"B" : [[("rwd","inicio"),("nterm","D"),("nterm","C"),("rwd","fim")]],
"D" : [[("nterm","T"),("idt","idt"),("pnt",";")],[]],
"T" : [[("rwd","int")],[("rwd","char")],[("rwd","real")]],
"C" : [[("rwd","se"),("nterm","CO"),("rwd","entao"),("nterm","B"),("nterm","C")],[("rwd","enquanto"),("nterm","CO"),("nterm","B"),("nterm","C")],[("nterm","E"),("nterm","C")],[]],
"CO": [[("pnt","("),("nterm","X"),("nterm","R"),("nterm","X"),("pnt",")")]],
"E" : [[("nterm","A"),("pnt",";")],[("nterm","M"),("pnt",";")]],
"A" : [[("idt","idt"),("opt","="),("nterm","X"),("pnt",";")]],
"M" : [[("idt","idt"),("nterm","O"),("nterm","M")],[("nterm","X")]],
"O" : [[("opt","+")],[("opt","-")],[("opt","*")],[("opt","/")]],
"X" : [[("idt","idt")],[("cst","cst")]],
"R" : [[("rlp","==")],[("rlp","<>")],[("rlp","<=")],[("rlp",">=")],[("rlp","<")],[("rlp",">")]]
}
# derivation = [(term,x),(term,y),(nterm,A),...]

def print_grammar():
	for nterm in grammar.keys():
		print(nterm,end=" -> ")
		for derv in grammar[nterm]:
			for alfa in derv :
				print(alfa[1],end=" ")
			print("",end=" | ")
		print()

# Seems like its working
def first(nterm):
	if nterm not in grammar.keys():
		return [nterm]
	else:
		res = []
		for derv in grammar[nterm]:
			if   not derv:
				res.append(())
			for alfa in derv:
				if alfa[0] != "nterm":
					res.append(alfa)
					break
				else:
					aux = first(alfa[1])
					if () in x:
						res += aux	
				# check if the 0 have void if yes go to 1
					res += aux
		return res


def follow(nterm):
	res = []
	if nterm not in grammar.keys():
		return res
	elif: nterm == "I":
		res.append(("$","$"))
	else:
		res = []
		for nterm in grammar.keys():
			for derv in grammar[nterm]:
				for j in len(derv):
					if derv[j][1] == nterm:
						if j != len(derv):
							res += first(derv[j + 1][1])
						if () in res or j == len(derv):
							res += follow(nterm)
							
	return res

class ListTokens():
	def __init__(self,tokens):
		self.current = 0
		self.tk_list = tokens

	def name(self):
		return self.tk_list[self.current].name

	def attribute(self):
		return self.tk_list[self.current].attribute

	def next(self):
		self.current += 1
		print(self.tk_list[self.current - 1].attribute,"->",self.tk_list[self.current].attribute)

class ACPredictible():
	def proc_I(self):
		if self.token.attribute() == "programa":
			self.token.next()
			self.proc_B()
			print(self.token.attribute)
			return True
		return False
		print("Error I")

	def proc_B(self):
		if self.token.attribute() == "inicio":
			self.token.next()
			self.proc_D()
	#		self.proc_C()
			if self.token.attribute() == "fim":
				token.next()
				return True
		print("Error B")
		return False

	def proc_D(self):
		self.proc_T()
		if self.token.name() == "idt":
			self.token.next()
			if self.token.attribute() == ";":
				self.token.next()
				return True
		return True

	def proc_T(self):
		if self.token.attribute() == "int":
			self.token.next()
			return True
		if self.token.attribute() == "char":
			self.token.next()
			return True
		if self.token.attribute() == "real":
			self.token.next()
			return True
		print("Error T")
		return False

#	def proc_C():

	def proc_CO():
		if self.token.attribute() == "(":
			self.token.next()
			self.proc_X()
			self.proc_R()
			self.proc_X()
			if self.token.attribute() == ")":
				self.token.next()
				return True
		return False

#	def proc_E():

	def proc_A(self):
		if self.token.name() == "idt":
			self.token.next()
			if self.token.attribute() == "=":
				self.token.next()
				self.prox_X()
				if self.token.attribute() == ";":
					self.token.next()
					return True

	def proc_M(self):
		if self.token.name() == "idt":
			self.token.next()
			self.proc_O()
			self.proc_M()
			return True
		else:
			self.proc_X()
			return True
		return False

	def prox_X(self):
		if self.token.name() == "idt":
			self.token.next()
			return True
		if self.token.name() == "cst":
			self.token.next()
			return True
		return False

	def proc_O(self):
		if self.token.attribute() == "+":
			self.token.next()
			return True
		if self.token.attribute() == "-":
			self.token.next()
			return True
		if self.token.attribute() == "*":
			self.token.next()
			return True
		if self.token.attribute() == "/":
			self.token.next()
			return True
		return False

	def proc_R(self):
		if self.token.attribute() == "==":
			self.token.next()
			return True
		if self.token.attribute() == "<>":
			self.token.next()
			return True
		if self.token.attribute() == ">=":
			self.token.next()
			return True
		if self.token.attribute() == "<=":
			self.token.next()
			return True
		if self.token.attribute() == ">":
			self.token.next()
			return True
		if self.token.attribute() == "<":
			self.token.next()
			return True
		return False

	def run(self,tokens):
		self.token = ListTokens(tokens)
		self.proc_I()

#def derivation():
#	for der in gram[nterm]:
#		for gsimbol in der:
#			
