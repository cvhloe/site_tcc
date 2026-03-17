# Resultados básicos

## Grupos

**Definição:** Seja $G$ um conjunto não vazio junto a uma operação $\ast$ fechada sobre $G$, isto é $\ast:G\times G\rightarrow G$ é uma função. Dizemos que $(G,\ast)$ tem estrutura de grupo se $\ast$ satisfaz a associatividade, a existência de uma identidade e a existência de um elemento inverso. Caso essas propriedades sejam satisfeitas e além delas $\ast$ for comutativo chamamos de grupo abeliano ou comutativo.

**Teorema:**
Considere um grupo finito $G$ e um subgrupo $H$ de $G$. A ordem de um subgrupo de um grupo finito é sempre um divisor da ordem do grupo $G$.

**Corolário:**
Se um grupo $G$ tem ordem prima, então $G$ é cíclico.

**Corolário:**
Se $G$ é um grupo finito e  $x \in G$, então $x^{|G|}=e$.

---

## Estrutura e relações entre grupos

### Homomorfismos e o Teorema do Isomorfismo

**Definição:** Sejam $G, G'$ grupos e uma função $\varphi:G\rightarrow G'$. Dizemos que $\varphi$ é um homomorfismo se:


$$\varphi(xy)=\varphi(x)\varphi(y) \;\;\; \forall x,y \in G $$


O *kernel* $K$ de $\varphi$ é o conjunto de elementos de $G$ que são levados na identidade de $G'$, ou seja, $K=\{x\in G \mid \varphi(x)= e' \}$.
Se $\varphi$ é uma bijeção, chamamos $\varphi$ de um isomorfismo.

Segue da definição que um homomorfismo $\varphi$ é injetor se, e somente se, o *kernel* de $\varphi$ é somente a identidade.

Um subgrupo $H$ de um grupo $G$ é dito normal se $aHa^{-1}=H$, para todo $a\in G$. Tome $H$ um subgrupo normal de $G$ e a função $\varphi:G\rightarrow G/ H$ definida por $\varphi(x) = xH$. $\varphi$ é um homomorfismo, pois:


$$\varphi(xy)=xyH=(xH)(yH)=\varphi(x)\varphi(y)\;\;\;\; \forall x,y \in G$$

A imagem desse homomorfismo é $G/H$ e seu *kernel* é $H$.

**Teorema (Teorema de isomorfismo):**
O *kernel* $K$ de um homomorfismo $\varphi:G\rightarrow G'$ é um subgrupo normal de $G$ e sua correspondência $xK\rightarrow \varphi(x)$ é um isomorfismo de grupos, isto é, temos uma aplicação

$$\begin{aligned}
G/K &\longrightarrow \text{Im}(\varphi) \\
xK &\longmapsto \varphi(x)
\end{aligned}$$

que é um isomorfismo.

---

**Exemplo:**
Um tabuleiro de xadrez possui quatro simetrias planas: a identidade $e$, a rotação $r$ de ângulo $\pi$ em torno de seu centro, e as reflexões $q_1, q_2$ em suas duas diagonais. Esses elementos formam um grupo sob a operação de composição, cuja tabela de multiplicação é dada pela Tabela 1.

|  | $e$ | $r$ | $q_1$ | $q_2$ |
| --- | --- | --- | --- | --- |
| **$e$** | $e$ | $r$ | $q_1$ | $q_2$ |
| **$r$** | $r$ | $e$ | $q_2$ | $q_1$ |
| **$q_1$** | $q_1$ | $q_2$ | $e$ | $r$ |
| **$q_2$** | $q_2$ | $q_1$ | $r$ | $e$ |

*Tabela 1: Tabela de multiplicação da rotação e reflexões*

É fácil verificar que a multiplicação módulo oito entre os números $1, 3, 5, 7$ também forma um grupo. Segue a tabela abaixo:

|  | $1$ | $3$ | $5$ | $7$ |
| --- | --- | --- | --- | --- |
| **$1$** | $1$ | $3$ | $5$ | $7$ |
| **$3$** | $3$ | $1$ | $7$ | $5$ |
| **$5$** | $5$ | $7$ | $1$ | $3$ |
| **$7$** | $7$ | $5$ | $3$ | $1$ |

*Tabela 2: Tabela de multiplicação módulo oito*

Há uma semelhança aparente entre essas tabelas se ignorarmos suas origens.
Em cada caso, o grupo tem quatro elementos, e esses elementos parecem se combinar da mesma maneira. A única diferença está em como os elementos foram rotulados em cada tabela.

Denotemos o primeiro grupo por $G$, o segundo por $G'$, e consideremos a correspondência

$$e \mapsto 1, \quad r \mapsto 3, \quad q_1 \mapsto 5, \quad q_2 \mapsto 7.$$

Dizemos que os elementos se combinam da mesma forma, no sentido de que se $x \mapsto x'$ e $y \mapsto y'$, então $xy \mapsto x'y'$. Essa correspondência é chamada de isomorfismo entre $G$ e $G'$. É uma bijeção que preserva a multiplicação de $G$ para $G'$. Informalmente, podemos considerar que $G$ e $G'$ são "o mesmo grupo".

A bijeção $\varphi$ de $G$ em $G'$ garante que os conjuntos subjacentes de $G$ e $G'$ têm o mesmo tamanho. Além disso, se $\varphi(xy) = \varphi(x)\varphi(y)$, não importa se primeiro combinamos dois elementos em $G$ e depois aplicamos $\varphi$, ou se aplicamos $\varphi$ separadamente a cada elemento e depois os combinamos em $G'$ o resultado é o mesmo.

Note que a função inversa $\varphi^{-1}: G' \to G$ também é um isomorfismo, de modo que a definição é simétrica em $G$ e $G'$.