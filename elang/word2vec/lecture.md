## Word Vectors
$$w^{bca} = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix},  
w^{uob} = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix},
...,
 w^{dbs} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
$$

where every word is an $\mathbb{R}^{|V|\times1}$ vector, $|V|$ being the size of our vocabulary.

$$(W^{uob})^T \cdot (W^{dbs})$$