#!/usr/bin/python3

import sys

class Token():
	def __init__(self,ttype,attribute,line,col):
		self.name      = ttype
		# cnst  = constante
		# ident = identificador
		# relop = operador relacional
		# rword = palavra reservada
		# pont  = pontuação
		# op    = operador
		self.attribute = attribute
		self.line      = line
		self.col       = col

class STDiagram():
	def __init__(self,afd):
		fd         = open(afd,"r")
		lines      = fd.readlines()
		self.tt    = [] # transition table
		self.final = [] # final states

		for l in lines:
			aux = {}
			l   = l.strip("\n")
			l   = l.split(";")
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
			if int(l[i]) == 1:
				self.final.append(len(self.tt) - 1)
		print(self.final)

	def is_final(self,state):
		if state in self.final:
			return True
		return False

class Tokenizer():
	def __init__(self,file_name):
		self.source_code      = file_name
		self.buffer           = []
		self.transition_table = STDiagram("./Tables/t_afd.csv")

	def run(self):
		fd          = open(self.source_code,"r")
		self.buffer = fd.read()

		start = None
		end   = None
		state = 0
		line  = 0
		col   = 0

		for i in range(len(self.buffer) - 1):
		# Setar "ponteiros"
			head = self.buffer[i]
			prox = self.buffer[i+1]
#			print(head,"and",prox)
# ----------------------------------------------------------------------------------------------------------------------------------------------------
			if start == None and head != " " and head != "\t" and head != "\n":
				start = i
			if head == " " or head == "\t":
				if start != None:
					if self.transition_table.is_final(state):
						end = i
						print("1",self.buffer[start:end + 1].replace(" ","").replace("\n","").replace("\t",""))
						state  = 0
						start  = None
						end    = None 
					else:
						print("1 Error at",line,col)
						break
				else:
					continue
			elif head == '\n':
				if start != None:
					if self.transition_table.is_final(state):
						end = i
						print("2",self.buffer[start:end + 1].replace(" ","").replace("\n","").replace("\t",""))
						state  = 0
						start  = None
						end    = None
					else:
						print("2 Error at",line,col)
						break
					line += 1
					col   = 0
				else:
					continue
# ----------------------------------------------------------------------------------------------------------------------------------------------------
		# Usar diagrama para determinar estados
#			print(state,end=" -> ")
			state     = self.transition_table.tt[state][head]
#			print(state)
			if self.transition_table.is_final(state):
				end = i
			if prox == " " or prox == "\t" or prox == "\n":
				new_state = -1
			else:
				new_state = self.transition_table.tt[state][prox]
#			print(prox,"+",state,"=",new_state)

			# Reconheceu o mais longo
			if new_state == -1:
				if end != None: # state hit final at some point
					print("3",self.buffer[start:end + 1].replace(" ","").replace("\n","").replace("\t",""))
					state  = 0
					start  = None
					end    = None
#					lexema = Token("",self.buffer[start:head + 1],line,col)
				else :
					print("3 Error at",line,col)
					
			col += 1



