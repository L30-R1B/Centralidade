# Análise de Redes com Centralidades e Relatório em PDF

Este projeto realiza a análise de uma rede usando várias medidas de centralidade (grau, closeness, betweenness e PageRank) e gera um relatório em PDF com os resultados. A rede de exemplo utilizada é o grafo do clube de karatê de Zachary, mas você pode substituir por qualquer outra rede.

## Funcionalidades

1. **Carregar uma Rede:** Utiliza o grafo do clube de karatê de Zachary como exemplo.
2. **Calcular Centralidades:**
    - Grau
    - Closeness
    - Betweenness
    - PageRank
3. **Ordenar e Rankear os Vértices:** Os vértices são ordenados e rankeados de acordo com cada centralidade.
4. **Plotar a Rede:** A rede é plotada com o tamanho dos vértices proporcional à centralidade de grau.
5. **Gerar Relatório em PDF:** Um relatório em PDF é gerado com os rankings dos vértices para cada centralidade.

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

- `networkx`
- `matplotlib`
- `fpdf`
- `scipy`

Você pode instalá-las usando o comando:

```sh
pip install networkx matplotlib fpdf scipy
