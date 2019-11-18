# Tokens

* Palavras Reservadas : programa, inicio, fim, int, se, enquanto, entao, faca, para, char, real
* Identificador
* Constante : char, int, real
* Pontuação : '(' , ')' , ';' , '[' , ']'
* Operadores : +, -, *, /
* Operadores Relacionais : >, <, >=, <=, ==, <>

# Expressões Regulares

## Padrões Base
* letra  = (a|b|...|z|A|B|...Z)
* digito = (0|1|...|9)
* numero = (+|-)? digito digito*
* float  = (+|-)? digito digito* (, digito digito*)?
* string = 'letra*'

## Padrões Tokens

* Palavras Reservadas &rightarrow; p(rograma|ara) | in(icio|t) | f(im|aca) |  en(quanto|tao) | se | char | real 
* Identificador &rightarrow; letra letra*
* Operadores Relacionais &rightarrow;  =(=)? | <(>|=)? | >(=)? 
* Operadores &rightarrow;  + | - | * | / 
* Pontuacao &rightarrow; ( | ) | [ | ] | ;  
* Constante &rightarrow; numero | string | float 

# Diagramas

## AFD

![AFD](./Diagramas/afd_v3.jpg)

## AFND

![AFND](./Diagramas/afnd_v2.jpg)

## Palavras Reservadas

![Reserved Words](./Diagramas/rword.png)

## Constantes

![Const](./Diagramas/const.png)

## Operadores Relacionais

![Relop](./Diagramas/relop.png)

## Pontuação

![Pont](./Diagramas/pont.png)

## Operadores

![Op](./Diagramas/op.png)

## Identificadores

![Id](./Diagramas/id.png)
