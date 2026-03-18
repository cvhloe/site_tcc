## O Grupo Simétrico $S_n$
O grupo $S_n$ é um grupo de permutações de elementos. Mais precisamente, seja $A$ um conjunto finito $\{1, 2, \dots, n\}$. Se tomarmos todas as funções bijetoras de $A$ em $A$, o que elas fazem é permutar os elementos. A composição de uma função bijetora é ainda uma função bijetora. O número de bijeção de $n$ elementos é $n!$.

Com essas operações temos um grupo que é chamado de grupo das permutações, ou ainda grupo simétrico $S_n$. $S_n$ tem $n!$ elementos, onde $n! = n(n-1)(n-2)\dots(3)(2)(1)$. 

O grupo $S_n$ possui um teorema importante, o Teorema de Cayley, que afirma que, se $G$ é um grupo, então $G$ é isomorfo a um subgrupo de $S_G$. Além desse teorema, temos que, se $G$ é um grupo finito de ordem $n$, então $G$ é isomorfo a um subgrupo de $S_n$.

O grupo $S_n$ pode ser obtido fazendo todas as possíveis combinações com os elementos $(1\,2)$ e $(1\,2\,\dots\,n)$. Resumidamente é o que diz o corolário a seguir:

**Corolário:**
Os ciclos $(1\,2)$ e $(1\,2\,\dots\,n)$ geram o grupo $S_n$.

*Demonstração:*
Seja $t = (1\,2)$ e $a = (1\,2\,\dots\,n)$, e seja $G = \langle a, t \rangle$ o grupo gerado por $a$ e $t$. Primeiro, mostramos que $G$ contém todas as transposições adjacentes. Através da conjugação de $t$ por potências de $a$, obtemos:
$$a t a^{-1} = (2\,3)$$
$$a^2 t a^{-2} = a(2\,3)a^{-1} = (3\,4)$$
e, em geral, para $k = 1, 2, \dots, n-2$,
$$a^k t a^{-k} = (k+1, k+2).$$
Assim, $G$ contém as transposições $(2,3), (3,4), \dots, (n-1, n)$. Como $G$ já contém $t=(1,2)$, concluímos que $G$ contém todas as transposições adjacentes. Pode ser provado que o conjunto de transposições adjacentes geram $S_n$, e todas elas pertencem a $G$, segue que $G$ deve ser o próprio $S_n$. $\blacksquare$

## O Grupo Alternado $A_n$

O grupo alternado, denotado por $A_n$, é subgrupo do grupo simétrico $S_n$ do conjunto $\{1,2,3,\dots,n\}$ que contém as permutações de ordem par. Uma permutação par é uma permutação que, quando escrita como um produto de transposições, usa um número par de transposições. Pode ser provado que este número par é uma invariante.

**Teorema:**
As permutações pares em $S_n$ formam um subgrupo de ordem $n!/2$, chamado de grupo alternado $A_n$ de grau $n$.

**Teorema:**
Para $n \geq 3$, os $3-$ciclos geram o $A_n$.

*Demonstração:*
Cada $3-$ciclos é uma permutação par, dado um elemento de $A_n$ usamos o corolário para escrever como um produto de pares de transposição da forma $(1a)$. Tome essas transposições em pares adjacentes e combine esses pares usando $(1a)(1b)=(1ba)$. Nosso elemento é agora um produto de $3-$ciclos. $\blacksquare$

## O Grupo Diedral $D_n$
Também temos o grupo diedral $D_n$, grupo não abeliano das simetrias de um polígono regular de $n$ lados. Por exemplo, se $n=3$ temos um triângulo, que tem um total de seis rotações simétricas, sendo três rotações ($r$) e três reflexões ($s$). Temos então: $D_3 = \{e,r,r^2,s,rs,r^2s\}$.


<div class="alvo-cayley"></div>

|        | $e$    | $r$    | $r^2$  | $s$    | $rs$   | $r^2s$ |
|--------|--------|--------|--------|--------|--------|--------|
| $e$    | $e$    | $r$    | $r^2$  | $s$    | $rs$   | $r^2s$ |
| $r$    | $r$    | $r^2$  | $e$    | $rs$   | $r^2s$ | $s$    |
| $r^2$  | $r^2$  | $e$    | $r$    | $r^2s$ | $s$    | $rs$   |
| $s$    | $s$    | $r^2s$ | $rs$   | $e$    | $r^2$  | $r$    |
| $rs$   | $rs$   | $s$    | $r^2s$ | $r$    | $e$    | $r^2$  |
| $r^2s$ | $r^2s$ | $rs$   | $s$    | $r^2$  | $r$    | $e$    |


*Tabela: Tabela do grupo $D_3$*

## Grupos Ortogonais $O_n$ e $SO_n$
Uma matriz $A_{n \times n}$ é ortogonal se satisfaz:
$$A^t A = I,$$
onde $I$ é a matriz identidade e $A^t$ é a matriz transposta de $A$. Isso significa que as colunas de $A$ formam uma base ortonormal de $\mathbb{R}^n$. O mesmo vale para as linhas. Como $\det(A^t A) = (\det A)^2$, o determinante de uma matriz ortogonal é sempre $\pm 1$.

O conjunto de todas as matrizes ortogonais $n \times n$ formam um subgrupo do grupo linear geral, denotado por $GL_n(\mathbb{R})$. Esse subgrupo é chamado de grupo ortogonal $O_n$. O subconjunto de $O_n$ formado pelas matrizes com determinante igual a $1$ é chamado de grupo ortogonal especial $SO_n$.

**Proposição:**
Seja $A \in O_n$ e $f_A : \mathbb{R}^n \to \mathbb{R}^n$ a transformação linear dada por $f_A(x) = Ax$. Então $f_A$ é uma isometria, isto é,
$$||f_A(x) - f_A(y)|| = ||x-y||, \quad \forall x,y \in \mathbb{R}^n.$$

*Demonstração:*
Calculando $||f_A(x)||^2$, temos: 
$$||f_A(x)||^2 = f_A(x)\cdot f_A(x) = (Ax)^t(Ax) = x^tA^tAx = x^tx = ||x||^2 \Rightarrow ||f_A(x)|| = ||x||$$
Logo seu comprimento é preservado. Também, $||f_A(x) - f_A(y)|| = ||f_A(x-y)|| = ||x-y||$, mostra que $f_A$ preserva a distância entre dois pontos. Note que a ortogonalidade também é preservada. $\blacksquare$

**Teorema:**
Seja $A \in SO_3$. Então $A$ é uma rotação em $\mathbb{R}^3$ em torno de um eixo que passa pela origem, isto é, existe um vetor $v \in \mathbb{R}^3 \setminus \{0\}$ tal que $Av = v$ e a restrição de $A$ ao plano ortogonal a $v$ é uma rotação plana.

*Demonstração:*
Seja $A \in SO_3$. Como $A \in O_3$, temos que $A^T A = I$, ou seja, $A$ é uma matriz ortogonal. O polinômio característico de $A$, pelo Teorema Fundamental da Álgebra, possui pelo menos uma raiz real. Como $A \in SO_3$, então $\det A = \lambda_1 \lambda_2 \lambda_3 = 1$. O autovalor real é necessariamente $\lambda_1 = 1$.
Seja $v \in \mathbb{R}^3$ um autovetor associado ao autovalor $1$, então $Av = v$. Na base $\{v, v_1, v_2\}$, a matriz $A$ representa uma rotação plana de $SO_2$ sobre o plano ortogonal. Assim, toda matriz de $SO_3$ representa uma rotação em $\mathbb{R}^3$ em torno de um eixo que passa pela origem. $\blacksquare$

## Grupos de Simetria dos Sólidos Platônicos

Existem exatamente cinco sólidos platônicos no espaço euclidiano tridimensional. Seus grupos de simetria atuam de forma transitiva sobre vértices, arestas e faces.
<div class="alvo-platonico"></div>

| Sólido Platônico | Vértices (V) | Arestas (A) | Faces (F) |     Forma da Face    |
|------------------|:------------:|:-----------:|:---------:|:--------------------:|
| Tetraedro        |       4      |      6      |     4     | Triângulo equilátero |
| Cubo             |       8      |      12     |     6     |       Quadrado       |
| Octaedro         |       6      |      12     |     8     | Triângulo equilátero |
| Dodecaedro       |      20      |      30     |     12    |   Pentágono regular  |
| Icosaedro        |      12      |      30     |     20    | Triângulo equilátero |
*Tabela: Características dos Sólidos Platônicos*

**Definição (Sólidos Duais):**
O poliedro dual de um sólido regular é outro poliedro que pode ser construído conectando os centros de cada face do sólido original, inscrevendo este novo poliedro dual dentro do original.

**Lema:**
Se dois sólidos são duais, então eles possuem o mesmo grupo de simetria.

*Demonstração:*
Seja $g$ uma simetria (isometria) que mapeia o poliedro $P$ em si mesmo. Tal transformação $g$ permuta as faces de $P$, e portanto também os seus centros, que correspondem aos vértices de $P^*$. Portanto, toda simetria de $P$ é também uma simetria de $P^*$. Como o dual do dual é o poliedro original, ambos compartilham exatamente o mesmo grupo. $\blacksquare$

### Tetraedro
Existem 12 simetrias de rotação para o tetraedro regular. O conjunto dessas simetrias forma um grupo isomorfo ao grupo alternado $A_4$. Definimos o homomorfismo $\varphi: G \to S_4$, associando cada rotação a uma permutação dos vértices $\{1, 2, 3, 4\}$.

### Cubo e Octaedro
O cubo tem 24 simetrias rotacionais. Numerando as 4 diagonais principais do cubo, podemos associar cada rotação a uma permutação dessas diagonais, gerando um homomorfismo $\varphi: G \rightarrow S_4$. Como o cubo e o octaedro são duais, ambos compartilham o mesmo grupo de rotações $S_4$.

### Dodecaedro e Icosaedro
O dodecaedro possui 60 simetrias rotacionais (24 de faces, 20 de vértices, 15 de arestas, mais a identidade). Inscrevendo cinco cubos no interior do dodecaedro, cada rotação permuta esses cinco cubos. Isso nos dá o isomorfismo $\varphi: G \to A_5$. Sendo duais, o icosaedro compartilha este mesmo grupo $A_5$.

## Classificação de Grupos de Ordem 4
Para um grupo de ordem 4, o Teorema de Lagrange indica que seus elementos podem ter ordem 1, 2 ou 4. Se todo elemento não identidade de um grupo $G$ tem ordem 2, então $G$ é o grupo de Klein $V_4$, que é isomorfo ao grupo diedral $D_2$.
