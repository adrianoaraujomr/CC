#!/usr/bin/python3

class Token():
	def __init__(self,ttype,attribute,line,col):
		self.ttype     = ttype
		self.attribute = attribute
		self.line      = line
		self.col       = col

class STDiagram():
	def __init__(self,afd):
		

class Tokenizer():
	def __init__(self,file_name):
		self.source_code = file_name
		self.buffer      = []

	def run(self):
		fd          = open(self.source_code,"r")
		self.buffer = fd.read()

		line = 0
		col  = 0

		for i in self.buffer:
		# Ignorar espaços tabs e new lines
			if i == " " or i == "\t":
				continue
			elif i == '\n':
				line += 1
				col   = 0
				continue
		# Usar diagrama para determinar estados
			print(i," [",line,";",col,"]")
			col += 1


