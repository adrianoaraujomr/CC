#!/usr/bin/python3

from lex import Token

# gram       = nterm -> [derivations]
#grammar = {
#"I" : [("rwd","programa"),("nterm","B")],
#"B" : [("rwd","inicio"),("nterm","D"),("nterm","C"),("rwd","fim")],
#"D" : [("nterm","T"),("idt","X"),("pnt",";")],
#"T" : [("rwd","int"),("rwd","char"),("rwd","real")],
#"C" : [],
#"CO": [],
#"E" : [],
#"A" : [],
#"M" : [],
#"O" : [("opt","+"),("opt","-"),("opt","*"),("opt","/")],
#}
# derivation = [(term,x),(term,y),(nterm,A),...]

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

	def proc_C():

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

	def proc_E():

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
