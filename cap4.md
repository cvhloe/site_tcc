# Teoremas principais

**Teorema:**
Um grupo finito de $O_2$ é cíclico ou diedral.

*Demonstração:*
Tome um subgrupo não-trivial $G$ de $O_2$. Suponha que $G$ está contido em $SO_2$. Então cada elemento de $G$ representa uma rotação no plano.
Vamos tomar $A_\theta$ a matriz que representa as rotações anti-horárias, tal que $0\leq\theta<2\pi$, e vamos escolher $A_\varphi\in G$ tal que $\varphi$ é positivo e suficientemente pequeno.

Dado $A_\theta\in G$, fazemos $\theta/\varphi$ e obtemos $\theta=k\varphi+\psi$, onde $k\in \mathbb{Z}$ e $0\leq\psi<\varphi$. Temos então: 
$$A_\theta=A_{k\varphi+\psi}=(A_\varphi)^kA_\psi$$ 
e 
$$A_\psi = (A_\varphi)^{-k}A_\theta$$

Como $A_\theta$ e $A_\varphi$ estão em $G$, $A_\psi$ também está em $G$. Como $\varphi$ é o menor ângulo positivo de $G$ e $\psi <\varphi$, então $\psi=0$. Caso contrário, $A_\psi$ seria um elemento de $G$ com ângulo positivo menor que $\varphi$, contradizendo a minimalidade de $\varphi$. Então $\theta=k\varphi$, ou seja, $A_\theta = (A_\varphi)^k$, logo todo elemento de $G$ é uma potência de $A_\varphi$ então $G$ é cíclico e gerado por $A_\varphi$.

Se $G$ não esta contido em $SO_2$, definimos $H=G \cap SO_2$. Como $H$ é subgrupo de $G$ e pela primeira parte do teorema $G$ é cíclico, então $H$ é cíclico. Vamos tomar $A$ como gerador de $H$ e $B$ um elemento de $G\setminus H$. Temos que $G$ contém elementos com determinante $-1$. Vamos definir o homomorfismo de grupos: 
$$\det: G \rightarrow \{-1,1\}.$$

Como $G\nsubseteq SO_2$, então $\det$ é uma aplicação sobrejetiva, definimos: 
$$H = \ker\left(\det|_H\right) = \{ g \in G \mid \det(g) = 1 \} $$

Portanto, como $H$ é o *kernel* da aplicação $\det$, logo é subgrupo normal de $G$. Visto que a imagem da função é $\{-1,1\}$, temos $G/H \simeq \{-1,1\}$, ou seja, $G$ tem índice 2. Quando $A=I$, $G = H \cup B H=\{I,B\}$ e $\det(B)=-1$ logo é um grupo cíclico de ordem 2.

Temos que $B$ não pertence a $SO_2$ então ele representa uma reflexão no plano, portanto $B^2=I$. Quando $A\neq I$ seus elementos são rotações de ordem $n$, então $G$ é dada por: 
$$G=\{I,A,A^2,\cdots,A^{n-1},B,AB,A^2B,\cdots,A^{n-1}B\}$$

Então temos: 
$$A^n = I,\quad B^2 = I,\quad BA = A^{-1}B$$

As correspondências 
\begin{align*}
    A\mapsto r \quad (\text{rotação}), \quad B\mapsto s \quad (\text{reflexão})
\end{align*}    
determinam um isomorfismo entre $G$ e o grupo diedral $D_n$. $\blacksquare$

---

**Teorema:**
Um subgrupo finito de $SO_3$ é isomorfo a um grupo cíclico, a um grupo diedral ou ao grupo de simetria rotacional dos sólidos de Platão.

*Demonstração:*
Seja $G$ um subgrupo finito de $SO_3$. Cada elemento de $G$, exceto a identidade, representa uma rotação em $\mathbb{R}^3$ em torno de um eixo que passa pela origem. Seja $X$ o conjunto de todos os polos de todos elementos de $G \setminus \{e\}$.
Suponha que $x\in X$ e $g \in G$. Seja $x$ um polo de algum elemento $h \in G$, ou seja, $h(x) = x$. Temos então, 
$$(ghg^{-1})(g(x))=g(h(x))=g(x).$$ 
Isso mostra que $g(x)$ é um polo e fixado pela esquerda por $ghg^{-1}$, logo $g(x)\in X$. Assim, a aplicação $g \mapsto g(x)$ define uma ação de $G$ sobre o conjunto $X$ dos polos.

Vamos aplicar o teorema de contagem de órbitas à ação de $G$ em $X$ para a demonstração e mostrar que $X$ possui uma configuração de pontos bem estruturada. Seja $N$ o número de órbitas distintas, escolhendo um polo de cada órbitas denotamos esse polos por $x_1, x_2,\cdots,x_N$.

Todo elemento de $G\setminus \{e\}$ fixa exatamente $2$ polos, enquanto a identidade fixa todos eles, pelo teorema de contagem temos:
\begin{align*}
    N &= \frac{1}{|G|} \left( 2(|G|-1) + |X|\right)
\end{align*}

Temos que $|X|=\sum\limits_{i=1}^N|G(x_i)|$, pois $X$ é uma união disjunta das $N$ órbitas da ação $G$ sobre os polos. Como $x_1, x_2, \ldots, x_N$ são representantes de órbitas distintas, cada $G(x_i)$ é a órbita de $x_i$, ou seja, o conjunto de todos os polos que são levados a partir de $x_i$ pela ação de elementos de $G$. Então:
$$|X|=\left| \bigcup_{i=1}^N G(x_i) \right| = \sum_{i=1}^N |G(x_i)|$$

Portanto, reescrevendo a fórmula, temos: 
\begin{align*}
    N &=\frac{1}{|G|} \left( 2(|G|-1) + \sum_{i=1}^N|G(x_i)|\right)
\end{align*}

Rearranjando:
\begin{align*}
    2 \left( 1 - \frac{1}{|G|)} \right) &= N - \frac{1}{|G|} \sum_{i=1}^N |G(x_i)|\\
    &=N-\sum_{i=1}^N \frac{1}{|G_{x_i}|} \quad\quad\quad\quad (\ast) \\
    &=\sum_{i=1}^N \left( 1- \frac{1}{|G_{x_i}|} \right)
\end{align*}

Logo, o lado esquerdo está entre 1 e 2, então: 
\begin{align*}
    1\leq&2 \left( 1 - \frac{1}{|G|)} \right)<2 
\end{align*}

E cada $|G_{x_i}|\geq 2$, pois contém a identidade e pelo menos uma rotação.
\begin{align*}
    \frac{1}{2} &\leq 1 - \frac{1}{|G_{x_i}|}<1
\end{align*}
para $1\leq i\leq N$. Portanto, $N = 2$ ou $N = 3$.

Quando $N=2$, temos que $(\ast)$ é $2=|G(x_1)|+|G(x_2)|$, tendo somente dois polos. Como cada polo tem seu antípoda, que é também um polo, neste caso temos então que $x_1$ e $x_2$ estão no mesmo eixo de rotação, logo todos elementos de $G$ são rotações do mesmo eixo $L$. Se pensarmos no plano que passa pela origem e que é perpendicular à $L$, as rotações de $SO_3$, são então rotações deste plano. Logo $G$ é um subgrupo cíclico.

Para $N=3$ temos que $1+\frac{1}{|G|} = \left(\frac{1}{|G_{x_1}|}+\frac{1}{|G_{x_2}|}+\frac{1}{|G_{x_3}|}\right)$ e tomando $x_1=x,x_2=y,x_3=z$, temos que 
$$1+\frac{2}{|G|} = \left(\frac{1}{|G_{x}|}+\frac{1}{|G_{y}|}+\frac{1}{|G_{z}|}\right)>1\quad\quad (\ast\ast)$$ 

Por ser maior que $1$ temos $4$ possibilidades:
1. $\frac{1}{2},\frac{1}{2},\frac{1}{n}\quad n\geq2$;
2. $\frac{1}{2},\frac{1}{3},\frac{1}{2}$;
3. $\frac{1}{2},\frac{1}{3},\frac{1}{4}$;
4. $\frac{1}{2},\frac{1}{3},\frac{1}{5}$;

**Caso (i):** Vamos supor o caso $(i)$ com $n=2$, isto é, $|G_x|=|G_y|=|G_z|=2$
Neste caso, substituindo em 
$$2\left(1-\frac{1}{|G|}\right)=3-\left(\frac{1}{|G_x|}+\frac{1}{|G_y|}+\frac{1}{|G_z|}\right)$$
obtemos $|G|=4$. Como todo elemento de $G$ está em algum dos grupos $G_x$, $G_y$ ou $G_z$, segue que todo elemento de $G$ tem ordem $2$. Logo $G$ é o grupo de *Klein* e, portanto, é isomorfo a um grupo diedral. $\blacksquare$

*(A demonstração geométrica dos casos ii, iii e iv segue a mesma lógica descrita nos fundamentos do TCC, resultando nos grupos do Tetraedro, Octaedro e Icosaedro. Caso queira ler com mais detalhes as demonstrações acessar o Trabalho no repositório).*