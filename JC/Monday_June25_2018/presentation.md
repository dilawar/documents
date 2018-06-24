---
title: Attractor dynamics in networks with learning rules inferred from _in vivo_ data
subtitle: NBJC
author: Dilawar Singh
institute: NCBS Bangalore
email: dilawars@ncbs.res.in
fontfamily: libertine
theme : metropolis
mainfont: Fira Sans
header-includes:
    - \usepackage{tikz}
---

# Attractor networks

## Association in Hopfield networks

- Popular framework to create associations

::::::::::::::::: {.columns}

:::: {.column width=40%}

![Recurrent Neural Net](figures/tikz_hopfield.pdf)

:::: {.column width=40%}

\begin{tikzpicture}[scale=1, every node/.style={} ]
    \node[circle, draw] (neuron) {$\sum x_i w_i$};    
\end{tikzpicture}	

::::::::::::::::::::::

# Another column
