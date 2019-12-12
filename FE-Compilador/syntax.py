#!/usr/bin/python3

from lex import Token

# gram       = nterm -> [derivations]
grammar = {
"I"   : [[("rwd","programa"),("nterm","B")]],
"B"   : [[("rwd","inicio"),("nterm","D"),("nterm","C"),("rwd","fim")]],
"D"   : [[("nterm","T"),("idt","idt"),("pnt",";")],[]],
"T"   : [[("rwd","int")],[("rwd","char")],[("rwd","real")]],
"C"   : [[("rwd","se"),("nterm","CO"),("rwd","entao"),("nterm","B"),("nterm","C")],[("rwd","enquanto"),("nterm","CO"),("nterm","B"),("nterm","C")],[("nterm","E"),("nterm","C")],[]],
"CO"  : [[("pnt","("),("nterm","X"),("nterm","R"),("nterm","X"),("pnt",")")]],
"E"   : [[("nterm","A"),("pnt",";")]],
"A"   : [[("idt","idt"),("opt","="),("nterm","M")]],
"M"   : [[("pnt","("),("nterm","M11"),("pnt",")")],[("nterm","X")]],
"M11" : [[("nterm","M21"),("nterm","M12")]],
"M12" : [[("opt","+"),("nterm","M21"),("nterm","M12")],[("opt","-"),("nterm","M21"),("nterm","M12")],[]],
"M21" : [[("nterm","M"),("nterm","M22")]],
"M22" : [[("opt","*"),("nterm","M"),("nterm","M22")],[("opt","/"),("nterm","M"),("nterm","M22")],[]],
"X"   : [[("idt","idt")],[("cst","cst")]],
"R"   : [[("rlp","==")],[("rlp","<>")],[("rlp","<=")],[("rlp",">=")],[("rlp","<")],[("rlp",">")]]
}

term = {
"programa" : " ", 
"inicio"   : " ",
"fim"      : " ",
"idt"      : " ",
"int"      : " ",
"char"     : " ",
"real"     : " ",
"se"       : " ",
"entao"    : " ",
"enquanto" : " ",
"="        : " ",
"cst"      : " ",
"+"        : " ",
"-"        : " ",
"*"        : " ",
"/"        : " ",
"=="       : " ",
"<>"       : " ",
">="       : " ",
"<="       : " ",
">"        : " ",
"<"        : " ",
"("        : " ",
")"        : " ",
";"        : " ",
"$"        : " ",
}

tabSintaxe = []

def print_table_line(nterm, tabSintaxe) :
	aux = []
	print("|",nterm,"|",end="")
	for k in term.keys():
#		print(term[k],"[",k,"]|",end="")
		if term[k] != " ":
			aux.append(term[k])
		else:
			aux.append('0')
		print(term[k] + "|",end="")
		term[k] = " "
	tabSintaxe.append(aux)
	print()

def print_sintaxe_table(tabSintaxe):
	for i in tabSintaxe:
		print(i)

def print_grammar():
	for nterm in grammar.keys():
		print(nterm,end=" -> ")
		for derv in grammar[nterm]:
			for alfa in derv :
				print(alfa[1],end=" ")
			print("",end=" | ")
		print()

def first(nterm):
	if nterm not in grammar.keys():
		return [nterm]
	else:
		res = []
		for derv in grammar[nterm]:
			if   not derv:
				res.append(None)
			for alfa in derv:
				if alfa[0] != "nterm":
					res.append(alfa[1])
					break
				else:
					aux = first(alfa[1])
					if None in aux:
						res += aux
					else:
						res += aux
						break
		return list(set(res))

def follow(nterm):
	res = []
	if    nterm not in grammar.keys():
		return res
	elif nterm == "I":
		res.append("$")
	for gkeys in grammar.keys():
		for derv in grammar[gkeys]:
			for j in range(0,len(derv)):
				if derv[j][1] == nterm:
					if j == len(derv) - 1:
						if gkeys != nterm:
							for k in follow(gkeys):
								if k not in res:
									res.append(k)
					else:
						for k in first(derv[j + 1][1]):
							if k not in res:
								res.append(k)
						if None in res or j == len(derv):
							for k in follow(gkeys):
								if k not in res:
									res.append(k)
	try:
		res.remove(None)
	except:
		pass
	return res

def create_table():
	producao = 1

	for nterm in grammar.keys():
		for derv in grammar[nterm]:
			if derv:
				for corpoProd in first(derv[0][1]):
#					print(corpoProd)
					term[corpoProd] = str(producao)
			else:
				for corpoProd in follow(nterm):
#					print(corpoProd)
					term[corpoProd] = str(producao)
			producao += 1
		print_table_line(nterm, tabSintaxe)
	print_sintaxe_table(tabSintaxe)

def isTerminal(caracter):
	for k in term.keys():
		if caracter == k:
			return True
	return False

def findNonTerminalByIndex(index):
	count = 0
	for k in grammar.keys():
		if count == (index - 1):
			return grammar[k]
		count += 1


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
			token = self.tk_list[self.current].attribute
			self.current += 1
			return token
		#print(self.tk_list[self.current - 1].attribute,"->",self.tk_list[self.current].attribute)

class ACPredictible():

	def run(self,tokens):
		print("\nSyntax Analyzer :\n")
		self.token = ListTokens(tokens)
		create_table()

		stack = []
		stack.append("I")
		proxToken = self.token.next()

		while stack:
			top = stack[-1]
			if isTerminal(top):
				if top == proxToken:
					stack.pop()
					proxToken = self.token.next()
				else:
					print("Error 1!")
					break
			else:
				nextProd = tabSintaxe[list(grammar).index(top)][list(term).index(proxToken)]
				if nextProd == '0':
					print("Error 2!")
					break
				else:
					#Printar Arvore Aqui!
					stack.pop()
					prod = findNonTerminalByIndex(int(nextProd))
					print(prod)
					for derv in prod:
						if derv:
							for terminals in reversed(derv):
								stack.append(terminals[1])
		if proxToken != '$':
			print("Error 3!")
		else:
			print("Cadeia Aceita") 
		


				
		

#def derivation():
#	for der in gram[nterm]:
#		for gsimbol in der:
#			
