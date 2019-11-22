#!/usr/bin/python3

from compiler import *
#from lex import *

path = "../Codes/soma.pt"

cc  = FrontEnd(path)
tks = cc.run()
