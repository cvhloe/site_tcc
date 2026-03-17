# Ações de grupos

Uma definição importante para a demonstração de um dos teoremas é a definição de ação de grupo.

**Definição:**
Seja $G$ um grupo e $X$ um conjunto. Dizemos que $G$ atua em $X$ se existe uma função $\ast: G \times X \rightarrow X$, tal que para todo $g_1, g_2 \in G$ e $x \in X$, temos:
1. $ex = x$, onde $e$ é o elemento identidade de $G$;
2. $(g_1 g_2) x = g_1 (g_2 x)$.

Quando essas condições são satisfeitas, dizemos que existe uma ação de $G$ sobre $X$.

**Definição:**
Dada uma ação de $G$ em $X$ e um ponto $x\in X$, o conjunto de todas as imagens $g(x)$, enquanto $g$ varia em $G$, é chamado órbita de $x$ e é denotado por $G(x)$.

## O Teorema da Órbita-Estabilizador

Seja $G$ um grupo que atua em um conjunto $X$. Para um ponto $x \in X$, o estabilizador $G_x = \{ g \in G \mid g(x) = x \}$ é um subgrupo de $G$, e existe uma bijeção entre a órbita $Gx$ e o conjunto quociente $G / G_x$. 

Primeiro, a identidade está em $G_x$, ele é fechado para multiplicação e possui inverso, satisfazendo os critérios de subgrupo. Definimos a função:
$$\varphi : G / G_x \longrightarrow Gx, \quad \varphi(g G_x) = g(x),$$
e podemos provar que ela é uma bijeção (injetora e sobrejetora).

**Teorema:**
O teorema da órbita-estabilizador diz que para cada $x\in X$, a aplicação $g(x)\rightarrow gG_x$ é uma bijeção entre $G(x)$ e um conjunto da classe a esquerda de $G_x$ em $G$.

**Corolário:**
Se $G$ é finito, o tamanho de cada órbita é um divisor da ordem de $G$.
$$|G(x)|=\frac{|G|}{|G_x|}$$

## Teorema da Contagem de Órbitas

**Teorema:**
Suponha uma ação de grupo finito de $G$ em um conjunto $X$. Seja $X^g$ o subconjunto de $X$ dos pontos fixos à esquerda pelo elemento $g\in G$. O teorema da contagem de órbitas diz que o número de órbitas distintas é dado por: 
$$\frac{1}{|G|}\sum_{g\in G} |X^g|\text{, }$$
ou seja, a média do número de pontos fixados à esquerda por um elemento de $G$.