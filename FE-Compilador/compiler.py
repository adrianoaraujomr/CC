#!/usr/bin/python3

from lex import *

class FrontEnd():
	def __init__(self,source_code):
		self.lex = Tokenizer(source_code)

	def run(self):
		# 1 - Lexical Analyzer
		tks = self.lex.run()
		return tks

		# 2 - Syntatic Analyzer
		# 3 - Semantic Analyzer
		# 4 - IR Generator
