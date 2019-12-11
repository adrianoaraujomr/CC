### Alunos

* Adriano Araújo
* Gabriel Haddad	

# Gramática
* I &rightarrow; programa B
* B &rightarrow; inicio D C fim
* D &rightarrow; T ident ; D | £
* T &rightarrow; int |  char | real
* C &rightarrow; se Ç entao B C | enquanto Ç B C | E C | £
* Ç &rightarrow; ( X R X )
* E &rightarrow; A ;
* A &rightarrow; ident = M ;
* M &rightarrow; X O M | X
* O &rightarrow; + | - | * | /
* X &rightarrow; ident | const
* R &rightarrow; == | <> | >= | <= | > | <

# Tabela de Precedência e Associatividade de operadores

| Operadores | Precedência | Associatividade |
|:----------:|:-----------:|:---------------:|
| + e -      | menor       | esquerda        |
| * e \      | maior       | esquerda        |

* M &rightarrow; X O M | X

*Alteração da gramatica para precedência e associatividade*

* M1 &rightarrow; M1 + M2 | M1 - M2 | M2
* M2 &rightarrow; M2 * M  | M2 / M  | M
* M  &rightarrow; (M1) | X

*Remoção de recursão à esqueda*

* M11 &rightarrow; M21 M12
* M12 &rightarrow; + M21 M12 | - M21 M12 | £
* M21 &rightarrow; M M22
* M22 &rightarrow; * M M22 | / M M22 | £
* M   &rightarrow; (M11) | X

# Tabela de análise sintática

|   |programa|inicio|fim|ident|int|char|real|se|entao|enquanto|= |const|+ |- | *|\ |==|<>|>=|<=|> |< |( | ) |; |$ |
|:--|:-------|:-----|:--|:----|:--|:---|:---|:-|:----|:-------|:-|:----|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:--|:-|:-|
| I |1       |      |   |     |   |    |    |  |     |        |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| B |        |2     |   |     |   |    |    |  |     |        |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| D |        |      |4  |4    |3  |3   |3   |4 |     |4       |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |4 |
| T |        |      |   |     |5  |6   |7   |  |     |        |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| C |        |      |11 |10   |   |    |    |8 |     |9       |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| CO|        |      |   |     |   |    |    |  |     |        |  |     |  |  |  |  |  |  |  |  |  |  |12|   |  |  |
| E |        |      |   |13   |   |    |    |  |     |        |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| A |        |      |   |14   |   |    |    |  |     |        |  |     |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| M |        |      |   |16   |   |    |    |  |     |        |  |16   |  |  |  |  |  |  |  |  |  |  |15|   |  |  |
|M11|        |      |   |17   |   |    |    |  |     |        |  |17   |  |  |  |  |  |  |  |  |  |  |17|   |  |  |
|M12|        |      |   |     |   |    |    |  |     |        |  |     |18|19|  |  |  |  |  |  |  |  |  |20 |  |  |
|M21|        |      |   |21   |   |    |    |  |     |        |  |21   |  |  |  |  |  |  |  |  |  |  |21|   |  |  |
|M22|        |      |   |     |   |    |    |  |     |        |  |     |24|24|22|23|  |  |  |  |  |  |  |24 |  |  |
| X |        |      |   |25   |   |    |    |  |     |        |  |26   |  |  |  |  |  |  |  |  |  |  |  |   |  |  |
| R |        |      |   |     |   |    |    |  |     |        |  |     |  |  |  |  |27|28|30|29|32|31|  |   |  |  |



#### Produções

|Número | Produção                      |
|:-----:|:------------------------------|
|1      | I &rightarrow; programa B     |
|2      | B &rightarrow; inicio D C fim |
|3      | D &rightarrow; T ident ; D    |
|4      | D &rightarrow; £              |
|5      | T &rightarrow; int            |
|6      | T &rightarrow; char           |
|7      | T &rightarrow; real           |
|8      | C &rightarrow; se Ç entao B C |
|9      | C &rightarrow; enquanto Ç B C |
|10     | C &rightarrow; E C            |
|11     | C &rightarrow; £              |
|12     | Ç &rightarrow; ( X R X )      |
|13     | E &rightarrow; A ;            |
|14     | A &rightarrow; ident = M      |
|15     | M &rightarrow; X              |
|16     | M &rightarrow; (M11)          |
|17     |M11&rightarrow; M21 M12        |
|18     |M12&rightarrow; + M21 M12      |
|19     |M12&rightarrow; - M21 M12      |
|20     |M12&rightarrow; £              |
|21     |M21&rightarrow; M M22          |
|22     |M22&rightarrow; * M M22        |
|23     |M22&rightarrow; / M M22        |
|24     |M22&rightarrow; £              |
|25     | X &rightarrow; ident          |
|26     | X &rightarrow; const          |
|27     | R &rightarrow; ==             |
|28     | R &rightarrow; <>             |
|29     | R &rightarrow; >=             |
|30     | R &rightarrow; <=             |
|31     | R &rightarrow; >              |
|32     | R &rightarrow; <              |

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
