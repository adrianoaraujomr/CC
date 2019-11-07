#!/usr/bin/python3

class Token():
	def __init__(self,ttype,attribute,line,col):
		self.ttype     = ttype
		self.attribute = attribute
		self.line      = line
		self.col       = col

class STDiagram():
	def __init__(self,afd):
		fd      = open(afd,"r")
		lines   = fd.readlines()
		self.tt = [] # transition table
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
#		print(self.tt[0])
#		print(self.tt[0]['0'])
#		print(self.tt[0]['-'])


class Tokenizer():
	def __init__(self,file_name):
		self.source_code      = file_name
		self.buffer           = []
		self.transition_table = STDiagram("./Tables/t_afd.csv")

	def run(self):
		fd          = open(self.source_code,"r")
		self.buffer = fd.read()

		state = 0
		line  = 0
		col   = 0

		for i in self.buffer:
		# Ignorar espaços tabs e new lines
			if i == " " or i == "\t":
				continue
			elif i == '\n':
				line += 1
				col   = 0
				continue
		# Usar diagrama para determinar estados
			new_state = self.transition_table[state][i]
			print(state,"|",new_state,"|",i)
			print(i," [",line,";",col,"]")
			col += 1



