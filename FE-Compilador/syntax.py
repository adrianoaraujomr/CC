#!/usr/bin/python3

from lex import Token
from my_tree import *

# gram       = nterm -> [derivations]
grammar = {
    "I": [[("rwd", "programa"), ("nterm", "B")]],
    "B": [[("rwd", "inicio"), ("nterm", "D"), ("nterm", "C"), ("rwd", "fim")]],
    "D": [[("nterm", "T"), ("idt", "idt"), ("pnt", ";")], []],
    "T": [[("rwd", "int")], [("rwd", "char")], [("rwd", "real")]],
    "C": [[("rwd", "se"), ("nterm", "CO"), ("rwd", "entao"), ("nterm", "B"), ("nterm", "C")], [("rwd", "enquanto"), ("nterm", "CO"), ("nterm", "B"), ("nterm", "C")], [("nterm", "E"), ("nterm", "C")], []],
    "CO": [[("pnt", "("), ("nterm", "X"), ("nterm", "R"), ("nterm", "X"), ("pnt", ")")]],
    "E": [[("nterm", "A"), ("pnt", ";")]],
    "A": [[("idt", "idt"), ("opt", "="), ("nterm", "M")]],
    "M": [[("pnt", "("), ("nterm", "M11"), ("pnt", ")")], [("nterm", "X")]],
    "M11": [[("nterm", "M21"), ("nterm", "M12")]],
    "M12": [[("opt", "+"), ("nterm", "M21"), ("nterm", "M12")], [("opt", "-"), ("nterm", "M21"), ("nterm", "M12")], []],
    "M21": [[("nterm", "M"), ("nterm", "M22")]],
    "M22": [[("opt", "*"), ("nterm", "M"), ("nterm", "M22")], [("opt", "/"), ("nterm", "M"), ("nterm", "M22")], []],
    "X": [[("idt", "idt")], [("cst", "cst")]],
    "R": [[("rlp", "==")], [("rlp", "<>")], [("rlp", "<=")], [("rlp", ">=")], [("rlp", "<")], [("rlp", ">")]]
}

term = {
    "programa": " ",
    "inicio": " ",
    "fim": " ",
    "idt": " ",
    "int": " ",
    "char": " ",
    "real": " ",
    "se": " ",
    "entao": " ",
    "enquanto": " ",
    "=": " ",
    "cst": " ",
    "+": " ",
    "-": " ",
    "*": " ",
    "/": " ",
    "==": " ",
    "<>": " ",
    ">=": " ",
    "<=": " ",
    ">": " ",
    "<": " ",
    "(": " ",
    ")": " ",
    ";": " ",
    "$": " ",
}

tabSintaxe = []


def print_table_line(nterm, tabSintaxe):
    aux = []
    print("|", nterm, "|", end="")
    for k in term.keys():
        #		print(term[k],"[",k,"]|",end="")
        if term[k] != " ":
            aux.append(term[k])
        else:
            aux.append('0')
        print(term[k] + "|", end="")
        term[k] = " "
    tabSintaxe.append(aux)
    print()


def print_sintaxe_table(tabSintaxe):
    print("\nSyntax Table :\n")
    for i in tabSintaxe:
        print(i)


def print_grammar():
    for nterm in grammar.keys():
        print(nterm, end=" -> ")
        for derv in grammar[nterm]:
            for alfa in derv:
                print(alfa[1], end=" ")
            print("", end=" | ")
        print()


def first(nterm):
    if nterm not in grammar.keys():
        return [nterm]
    else:
        res = []
        for derv in grammar[nterm]:
            if not derv:
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
    if nterm not in grammar.keys():
        return res
    elif nterm == "I":
        res.append("$")
    for gkeys in grammar.keys():
        for derv in grammar[gkeys]:
            for j in range(0, len(derv)):
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
        for i in grammar[k]:
            if count == (index - 1):
                return i
            count += 1


class ListTokens():
    def __init__(self, tokens):
        self.current = 0
        self.tk_list = tokens

    def name(self):
        return self.tk_list[self.current].name

    def attribute(self):
        if self.tk_list[self.current].name == "idt":
            return "idt"
        elif self.tk_list[self.current].name == "cst":
            return "cst"

        return self.tk_list[self.current].attribute

    def next(self):
        if self.current < len(self.tk_list):
            if self.tk_list[self.current].name == 'idt' or self.tk_list[self.current].name == 'cst':
                token = self.tk_list[self.current].name
            else:
                token = self.tk_list[self.current].attribute
            self.current += 1
            return token
        #print(self.tk_list[self.current - 1].attribute,"->",self.tk_list[self.current].attribute)


class ACPredictible():

    def run(self, tokens):
        print("\nSyntax Analyzer :\n")
        self.token = ListTokens(tokens)
        create_table()

        stack = []
        stack.append("I")
        proxToken = self.token.next()
        tree = SyntaxTree()
        errors = Errors()

        print("\nProducoes aplicadas :\n")
        while stack:
            top = stack[-1]
            if isTerminal(top):
                if top == proxToken:
                    stack.pop()
                    proxToken = self.token.next()
                else:
                    # No codigo-fonte, se tirar o ; do int a;
                    # Ele vai dizer que era esperado ; mas foi encontrado idt(o a da próxima linha)
                    print("Era esperado {} mas foi encontrado {}".format(
                        top, proxToken))
                    return
            else:
                nextProd = tabSintaxe[list(grammar).index(
                    top)][list(term).index(proxToken)]
                if nextProd == '0':
                    errors.errorsHandle(top, proxToken)
                    return
                else:
                    #					print(nextProd)
                    #					print(findNonTerminalByIndex(int(nextProd)))
                    # Printar Arvore Aqui!
                    letter = stack.pop()
                    prod = findNonTerminalByIndex(int(nextProd))

                    print(letter, prod)
                    tree.add_prod(letter, production=prod)
                    if prod != []:
                        for derv in reversed(prod):
                            stack.append(derv[1])
        if proxToken != '$':
            print("Simbolo de final de cadeia esperado!")
        else:
            print("\nArvore pre ordem :\n")
            tree.pre_ordem()
            print("Cadeia Aceita")


class Errors:
    def errorsHandle(self, stackTop, proxToken):
        if stackTop == "I" and proxToken != "programa":
            print("Era esperado 'programa' mas foi achado", proxToken)
            return

        if stackTop == "B" and proxToken != "inicio":
            print("Era esperado 'inicio' mas foi achado", proxToken)
            return

        if stackTop == "D" and (proxToken != "fim" or proxToken != "idt" or proxToken != "int"
                                or proxToken != "char" or proxToken != "real" or proxToken != "se"
                                or proxToken != "enquanto" or proxToken != "$"):

            print("Era esperado 'fim','identificador','tipo','se','enquanto' ou final de cadeia mas foi achado", proxToken)
            return

        if stackTop == "T" and (proxToken != "int"
                                or proxToken != "char" or proxToken != "real"):

            print("Era esperado 'tipo: int, char ou real' mas foi achado", proxToken)
            return

        if stackTop == "C" and (proxToken != "fim" or proxToken != "idt" or proxToken != "se" \
                                or proxToken != "enquanto"):

            print(
                "Era esperado 'fim','identificador','se' ou 'enquanto' mas foi achado", proxToken)
            return

        if stackTop == "CO" and proxToken != "(":

            print("Era esperado '(' mas foi achado", proxToken)
            return

        if stackTop == "E" and proxToken != "idt":

            print("Era esperado 'identificador' mas foi achado", proxToken)
            return

        if stackTop == "A" and proxToken != "idt":

            print("Era esperado 'identificador' mas foi achado", proxToken)
            return

        if stackTop == "M" and (proxToken != "idt" or proxToken != "cst"
                                or proxToken != "("):

            print(
                "Era esperado 'identificador','constante' ou '(' mas foi achado", proxToken)
            return

        if stackTop == "M11" and (proxToken != "idt" or proxToken != "cst"
                                  or proxToken != "("):

            print(
                "Era esperado 'identificador','constante' ou '(' mas foi achado", proxToken)
            return

        if stackTop == "M12" and (proxToken != "+" or proxToken != "-"
                                  or proxToken != ")"):

            print("Era esperado '+','-' ou ')' mas foi achado", proxToken)
            return

        if stackTop == "M21" and (proxToken != "idt" or proxToken != "cst"
                                  or proxToken != "("):

            print(
                "Era esperado 'identificador','constante' ou '(' mas foi achado", proxToken)
            return

        if stackTop == "M22" and (proxToken != "+" or proxToken != "-"
                                  or proxToken != "*" or proxToken != "/" or proxToken != ")"):

            print("Era esperado '+','-','*','/' ou ')' mas foi achado", proxToken)
            return

        if stackTop == "X" and (proxToken != "idt" or proxToken != "cst"):

            print(
                "Era esperado 'identificador' ou 'constante' mas foi achado", proxToken)
            return

        if stackTop == "R" and (proxToken != "==" or proxToken != "<>"
                                or proxToken != ">=" or proxToken != "<=" or proxToken != ">" or proxToken != "<"):

            print(
                "Era esperado '==','<>','>=','<=','<' ou '>' mas foi achado", proxToken)
            return


# def derivation():
#	for der in gram[nterm]:
#		for gsimbol in der:
#
