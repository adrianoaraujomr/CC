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
# Change the exit to fit with the proc
def first(nterm):
	if nterm not in grammar.keys():
		return [nterm]
#		for xterm in grammar.keys():
#			for derv in grammar[xterm]:
#				for alfa in derv :
#					if alfa[1] == nterm:
#						return [alfa]
	else:
		res = []
		for derv in grammar[nterm]:
			if   not derv:
				res.append(None)
			for alfa in derv:
				if alfa[0] != "nterm":
					res.append(alfa[1])
#					res.append(alfa)
					break
				else:
					aux = first(alfa[1])
					if None in aux:
						res += aux
					else:
						res += aux
						break
		return list(set(res))


# Change the exit to fit with the proc
# Deal with duplicates
def follow(nterm):
	res = []
	if    nterm not in grammar.keys():
		return res
	elif nterm == "I":
		res.append("$")
#		res.append(("$","$"))
	for gkeys in grammar.keys():
#		print(gkeys)
		for derv in grammar[gkeys]:
#			print(derv)
			for j in range(0,len(derv)):
#				print(derv[j],j,nterm)
				if derv[j][1] == nterm:
					if j == len(derv) - 1:
						if gkeys != nterm:
							res += follow(gkeys)
					else:
						res += first(derv[j + 1][1])
						if None in res or j == len(derv):
							res += follow(gkeys)
#					print(res)							
	try:
		res.remove(None)
	except:
		pass
	return res

class ListTokens():
	def __init__(self,tokens):
		self.current = 0
		self.tk_list = tokens

	def name(self):
		return self.tk_list[self.current].name

	def attribute(self):
		if   self.tk_list[self.current].name == "idt":
			return "idt"
		elif self.tk_list[self.current].name == "cst":
			return "cst"

		return self.tk_list[self.current].attribute

	def next(self):
		if self.current < len(self.tk_list) - 1:
			self.current += 1
		print(self.tk_list[self.current - 1].attribute,"->",self.tk_list[self.current].attribute)

class ACPredictible():
	def proc_I(self):
		print("I",self.token.attribute())
		if self.token.attribute() == "programa":
			self.token.next()
			self.proc_B()
			return True
		print("Error procedure I")
		return False

	def proc_B(self):
		print("B",self.token.attribute())
		if self.token.attribute() == "inicio":
			self.token.next()
			self.proc_D()
			self.proc_C()
			if self.token.attribute() == "fim":
				self.token.next()
				return True
		print(self.token.attribute())
		print("Error procedure B")
		return False

	def proc_D(self):
		print("D",self.token.attribute())
		if self.token.attribute() in first("T"):
			self.proc_T()
			if self.token.name() == "idt":
				self.token.next()
				if self.token.attribute() == ";":
					self.token.next()
					self.proc_D()
					return True
				print("Error procedure D")
				return False
		return True

	def proc_T(self):
		print("T",self.token.attribute())
		if self.token.attribute() == "int":
			self.token.next()
			return True
		if self.token.attribute() == "char":
			self.token.next()
			return True
		if self.token.attribute() == "real":
			self.token.next()
			return True
		print("Error procedure T")
		return False

	def proc_C(self):
		print("C",self.token.attribute())
		if self.token.attribute() == "se":
			self.token.next()
			self.proc_CO()
			if self.token.attribute() == "entao":
				self.token.next()
				self.proc_B()
				self.proc_C()
				return True
			else:
				print("Error procedure C")
				return False
		if self.token.attribute() == "enquanto":
			self.token.next()
			self.proc_CO()
			self.proc_B()
			self.proc_C()
			return True
		if self.token.attribute() in first("E"):
			self.proc_E()
			self.proc_C()
			return True

		return True


	def proc_CO(self):
		print("CO",self.token.attribute())
		if self.token.attribute() == "(":
			self.token.next()
			self.proc_X()
			self.proc_R()
			self.proc_X()
			if self.token.attribute() == ")":
				self.token.next()
				return True
		print("Error procedure CO")
		return False

	def proc_E(self):
		print("E",self.token.attribute())
		if self.token.attribute() in first("A"):
			self.proc_A()
			if self.token.attribute() == ";":
				self.token.next()
				return True
			print("Error procedure E")
			return False
		if self.token.attribute() in first("M"):
			self.proc_M()
			if self.token.attribute() == ";":
				self.token.next()
				return True
			print("Error procedure E")
			return False

		print("Error procedure E")
		return False

	def proc_A(self):
		print("A",self.token.attribute())
		if self.token.name() == "idt":
			self.token.next()
			if self.token.attribute() == "=":
				self.token.next()
				self.prox_X()
#				if self.token.attribute() == ";":
#					self.token.next()
				return True
		print("Error procedure A")
		return False


	def proc_M(self):
		print("M",self.token.attribute())
		if self.token.name() == "idt":
			self.token.next()
			self.proc_O()
			self.proc_M()
			return True
		else:
			self.proc_X()
			return True
		print("Error procedure M")
		return False

	def prox_X(self):
		print("X",self.token.attribute())
		if self.token.name() == "idt":
			self.token.next()
			return True
		if self.token.name() == "cst":
			self.token.next()
			return True
		print("Error procedure X")
		return False

	def proc_O(self):
		print("O",self.token.attribute())
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
		print("Error procedure O")
		return False

	def proc_R(self):
		print("R",self.token.attribute())
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
		print("Error procedure R")
		return False

	def run(self,tokens):
		print("\nSyntax Analyzer :\n")
		self.token = ListTokens(tokens)
		self.proc_I()

#def derivation():
#	for der in gram[nterm]:
#		for gsimbol in der:
#			
