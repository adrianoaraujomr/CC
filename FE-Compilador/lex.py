#!/usr/bin/python3

import sys

class Token():
	def __init__(self,ttype,attribute,line,col):
		self.attribute = attribute
		self.line      = line
		self.col       = col
		self.name      = ttype
		# cnst  = constante
		# ident = identificador
		# relop = operador relacional
		# rword = palavra reservada
		# pont  = pontuação
		# op    = operador

	def print_value(self):
		print(self.name,self.attribute,self.line,self.col)


# Simbol table
class SBTable():
	def __init__(self):
		self.st    = [] # simbol table
	
	def add_element(self,value):
		for i in range(0,len(self.st)):
			if self.st[i] == value:
				return i
		self.st.append(value)
		return (len(self.st) - 1)


# Transition table
class STDiagram():
	def __init__(self,afd):
		fd         = open(afd,"r")
		lines      = fd.readlines()
		self.tt    = [] # transition table
		self.final = {} # final states


		for l in lines:
			aux = {}
			l   = l.strip("\n")
			l   = l.split(",")
			i   = 1

			for j in range(39,46):
				aux[chr(j)] = int(l[i])
				i += 1
			for j in range(48,58):
				aux[chr(j)] = int(l[i])
				i += 1
			for j in range(59,63):
				aux[chr(j)] = int(l[i])
				i += 1
			for j in range(91,94):
				aux[chr(j)] = int(l[i])
				i += 1
			for j in range(97,123):
				aux[chr(j)] = int(l[i])
				i += 1
			self.tt.append(aux)
			if l[i] != "0":
				self.final[str(len(self.tt) - 1)] = l[i]

	def move(self,state,head):
		return self.tt[state][head]

	def state_type(self,state):
		return self.final[str(state)]

	def is_final(self,state):
		if str(state) in self.final.keys():
			return True
		return False


# Lexical Analyzer
class Tokenizer():
	def __init__(self,file_name):
		self.source_code      = file_name
		self.buffer           = []
		self.transition_table = STDiagram("./Tables/t_afd.csv")
		self.symbol_table     = SBTable()

	def create_token(self,state,value,line,col):
		if self.transition_table.state_type(state) == "idt":
			index = self.symbol_table.add_element(value)
			tk    = Token(self.transition_table.state_type(state),index,line,col)
		else:
			tk = Token(self.transition_table.state_type(state),value,line,col)
		return tk

	def run(self):
		tokens      = []
		fd          = open(self.source_code,"r")
		self.buffer = fd.read()

		start = None
		end   = None
		state = 0
		line  = 1
		col   = 1

		print("Lexemas achados : ","\n")

		for i in range(len(self.buffer) - 1): # Percorre buffer
		# Setar "ponteiros"
			head = self.buffer[i]
			prox = self.buffer[i+1]

		# Tratar " ", "\t" e "\n"
			if head == "\n":
				line += 1
				col   = 1
				continue
			if head == " " or head == "\t":
				col += 1
				continue
			if start == None:
				start = i

		# Usar diagrama para determinar estados
			state     = self.transition_table.move(state,head)
			if self.transition_table.is_final(state):
				end = i
			if prox == " " or prox == "\t" or prox == "\n":
				new_state = -1
			else:
				new_state = self.transition_table.move(state,prox)

		# Reconheceu o mais longo
			if new_state == -1:
				if end != None: # state hit final at some point
					col_start = col - (end - start)
					lexema = self.create_token(state,self.buffer[start:end + 1].replace(" ","").replace("\n","").replace("\t",""),line,col_start)
					lexema.print_value()
					tokens.append(lexema)
					state  = 0
					start  = None
					end    = None
				else :
					print("Error at",line,col)

			col += 1

		return tokens
