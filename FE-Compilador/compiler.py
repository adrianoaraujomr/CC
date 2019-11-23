#!/usr/bin/python3

from lex    import *
from syntax import *

class FrontEnd():
	def __init__(self,source_code):
		self.lex    = Tokenizer(source_code)
		self.syntax = ACPredictible()

	def run(self):
		# 1 - Lexical Analyzer
		tks = self.lex.run()
#		# 2 - Syntatic Analyzer
		tre = self.syntax.run(tks)
		# 3 - Semantic Analyzer
		# 4 - IR Generator
