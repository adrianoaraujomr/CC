#!/usr/bin/python3

#from compiler import *
from lex import *

path = "../Codes/soma.pt"

lex = Tokenizer(path)
tks = lex.run()
print(tks)
