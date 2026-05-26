# Relatório do Projeto: Aplicação para Resolução de Categorias de Problemas com Grafos

**Disciplina:** Teoria dos Grafos (Turma 6G)

**Período:** 2026/1

**Universidade:** Universidade Presbiteriana Mackenzie

**Professor:** Prof. Dr. Ivan Carlos Alcântara de Oliveira

**Aluno:** Milton Almeida Leoncio

**RA:** 10416764

---

## 1. Introdução

Este relatório documenta o desenvolvimento da Parte 3 do projeto da disciplina de Teoria dos Grafos, que visa resolver uma categoria de problemas do mundo real utilizando conceitos e técnicas estudados na disciplina. O projeto implementa uma aplicação prática de otimização logística de entrega de encomendas em uma área metropolitana, modelando o problema como um grafo ponderado direcionado com mais de 70 vértices e 180 arestas.

---

## 2. Definição do Problema

### 2.1 Descrição do Problema Real

O problema abordado é a **otimização logística de entrega de encomendas em uma área metropolitana**. Uma empresa de entregas enfrenta o desafio de planejar rotas eficientes para seus entregadores, que devem coletar e entregar pacotes em diversos pontos da cidade. Os objetivos principais são:

- Minimizar o tempo total de entrega

- Minimizar a distância percorrida

- Maximizar a eficiência da frota de entregadores

- Identificar gargalos na infraestrutura viária

### 2.2 Cenário Detalhado

O cenário contempla:

- **Depósito Central:** Ponto único de partida e retorno de todos os entregadores

- **Pontos de Coleta:** 26 locais onde os entregadores devem buscar encomendas

- **Pontos de Entrega:** 36 locais onde os entregadores devem deixar encomendas

- **Cruzamentos e Pontos Estratégicos:** 11 vértices intermediários para representar a malha viária

- **Centros de Distribuição:** 4 pontos de distribuição secundários

- **Frota:** Entregadores homogêneos com capacidade limitada e tempo máximo de jornada

### 2.3 Modelagem como Grafo

O problema é modelado como um **grafo ponderado direcionado** G = (V, E):

- **Vértices (V):** Representam pontos de interesse (depósito, coletas, entregas, cruzamentos)

- **Arestas (E):** Representam trechos de ruas e avenidas com pesos (tempo, distância ou custo)

- **Quantidade:** 73 vértices e 219 arestas

- **Análise Estrutural:** A aplicação realiza verificações de conexidade, classificação euleriana e coloração de vértices para entender a topologia da rede logística.

---

## 3. Técnicas de Teoria dos Grafos Aplicadas

### 3.1 Algoritmo de Dijkstra (Caminhos Mínimos)

**Objetivo:** Encontrar a rota mais rápida ou mais curta entre quaisquer dois pontos na rede.

**Aplicação:**

- Calcular o tempo mínimo para ir do depósito a um ponto de coleta

- Determinar a rota mais curta entre dois pontos de entrega

- Estimar custos de segmentos de rota

**Complexidade:** O((V + E) \log V) com heap binário

**Implementação:** A implementação utiliza uma fila de prioridade (heap) para selecionar eficientemente o vértice com menor distância acumulada em cada iteração.

### 3.2 Heurística do Vizinho Mais Próximo (Problema do Caixeiro Viajante)

**Objetivo:** Otimizar a sequência de visitas a múltiplos pontos, minimizando o tempo ou distância total.

**Aplicação:**

- Determinar a ordem ideal de coleta de encomendas

- Planejar a sequência de entregas para um entregador

- Reduzir o tempo de jornada

**Complexidade:** O(n^2 \cdot (V + E) \log V) onde n é o número de pontos a visitar

**Funcionamento:**

1. Inicia no ponto de origem (depósito)

1. A cada passo, move-se para o ponto não visitado mais próximo

1. Repete até visitar todos os pontos

1. Retorna ao ponto de origem

**Limitações:** A heurística não garante a solução ótima, mas fornece uma solução aproximada em tempo polinomial.

### 3.3 Algoritmo de Ford-Fulkerson (Fluxo Máximo)

**Objetivo:** Determinar a capacidade máxima da rede de entrega em pontos críticos.

**Aplicação:**

- Analisar o número máximo de encomendas que podem passar por uma região

- Identificar gargalos na infraestrutura viária

- Avaliar a capacidade de processamento de centros de distribuição

**Complexidade:** O(E \cdot f^*) onde f^* é o fluxo máximo

**Funcionamento:**

1. Inicializa o fluxo como zero

1. Busca caminhos aumentantes no grafo residual

1. Incrementa o fluxo ao longo de cada caminho encontrado

1. Repete até que não haja mais caminhos aumentantes

**Teorema Fundamental:** O fluxo máximo é igual à capacidade do corte mínimo (Teorema de Ford-Fulkerson).

### 3.4 Análise Estrutural (Requisito 2 do Projeto)

A aplicação implementa funcionalidades para descobrir características fundamentais do problema modelado:

- **Grau dos Vértices:** Calcula graus de entrada e saída para identificar os pontos mais conectados da rede (hubs logísticos).

- **Verificação Euleriana:** Analisa se a malha viária permite um percurso que visite todas as ruas exatamente uma vez sem repetição (Caminho/Ciclo Euleriano).

- **Coloração de Vértices:** Utiliza uma heurística sequencial para particionar os pontos de entrega em conjuntos independentes. Isso é útil para agendar entregas simultâneas sem conflitos de recursos ou proximidade excessiva.

- **Teste de Conexidade:** Garante que todos os pontos da cidade são atingíveis a partir do depósito central.

---

## 4. Estrutura da Implementação

### 4.1 Arquivos do Projeto

```
projeto_teoria_grafos/
├── grafo.txt                    # Arquivo de dados do grafo
├── aplicacao_entrega.py         # Aplicação principal
├── definicao_e_modelagem.md     # Documentação da modelagem
├── RELATORIO_PROJETO.md         # Este relatório
└── README.md                    # Instruções de uso
```

### 4.2 Classe Principal: GrafoEntrega

A classe `GrafoEntrega` encapsula toda a lógica de manipulação do grafo e implementação dos algoritmos:

**Atributos:**

- `vertices`: Conjunto de vértices do grafo

- `arestas`: Dicionário de adjacências (lista de vizinhos com pesos)

- `capacidades`: Dicionário de capacidades das arestas

**Métodos Principais:**

- `carregar_de_arquivo()`: Carrega o grafo a partir de um arquivo

- `dijkstra()`: Implementa o algoritmo de Dijkstra

- `vizinho_mais_proximo()`: Implementa a heurística do vizinho mais próximo

- `ford_fulkerson()`: Implementa o algoritmo de Ford-Fulkerson

- `obter_estatisticas()`: Retorna estatísticas do grafo

- `listar_vertices()`: Lista todos os vértices

### 4.3 Formato do Arquivo de Dados (grafo.txt)

O arquivo segue um formato estruturado em duas seções:

```
VERTICES
deposito_central
coleta_norte_1
coleta_norte_2
...

ARESTAS
deposito_central coleta_norte_1 15
deposito_central coleta_norte_2 18
...
```

Cada aresta é definida por: `origem destino peso`

---

## 5. Resultados e Análise

### 5.1 Características do Grafo

| Métrica | Valor |
| --- | --- |
| Número de vértices | 73 |
| Número de arestas | 219 |
| Grau médio | 3.00 |
| Grau máximo | 17 |
| Densidade | 0.041 |

### 5.2 Exemplos de Execução

#### Exemplo 1: Caminho Mínimo (Dijkstra)

**Entrada:**

- Origem: `deposito_central`

- Destino: `entrega_norte_1`

**Saída:**

- Distância mínima: 27

- Caminho: `deposito_central → coleta_norte_1 → entrega_norte_1`

#### Exemplo 2: Rota Otimizada (Vizinho Mais Próximo)

**Entrada:**

- Origem: `deposito_central`

- Pontos a visitar: `coleta_norte_1, coleta_norte_2, entrega_norte_1, entrega_norte_2`

**Saída:**

- Custo total: 68

- Rota: `deposito_central → coleta_norte_1 → coleta_norte_2 → entrega_norte_1 → entrega_norte_2 → deposito_central`

#### Exemplo 3: Fluxo Máximo (Ford-Fulkerson)

**Entrada:**

- Origem (fonte): `deposito_central`

- Destino (sumidouro): `entrega_norte_1`

**Saída:**

- Fluxo máximo: 27

---

## 6. Instruções de Uso

### 6.1 Requisitos

- Python 3.7 ou superior

- Nenhuma dependência externa (apenas bibliotecas padrão)

### 6.2 Execução da Aplicação

```bash
python3 aplicacao_entrega.py
```

### 6.3 Menu de Opções

A aplicação oferece um menu interativo com as seguintes opções:

1. **Carregar grafo do arquivo:** Carrega os dados do grafo a partir de um arquivo

1. **Exibir estatísticas e Análise Estrutural:** Mostra informações sobre o grafo, incluindo graus, conexidade e classificação euleriana.

1. **Encontrar caminho mínimo:** Executa o algoritmo de Dijkstra.

1. **Otimizar rota de entrega:** Executa a heurística do vizinho mais próximo para o PCV.

1. **Calcular fluxo máximo:** Executa o algoritmo de Ford-Fulkerson.

1. **Realizar Coloração de Vértices:** Calcula o número cromático e as partições de cores.

1. **Listar vértices:** Exibe todos os vértices do grafo.

1. **Sair:** Encerra a aplicação.

---

## 7. Análise Teórica

### 7.1 Complexidade Computacional

| Algoritmo | Complexidade | Observações |
| --- | --- | --- |
| Dijkstra | O((V + E) \log V) | Com heap binário |
| Vizinho Mais Próximo | O(n^2 \cdot (V + E) \log V) | Onde $n$ é o número de pontos |
| Ford-Fulkerson | O(E \cdot f^*) | Onde f^* é o fluxo máximo |

### 7.2 Justificativa das Técnicas

**Por que Dijkstra?**

- Encontra caminhos mínimos em grafos com pesos não-negativos

- Essencial para determinar rotas mais rápidas ou curtas

- Complexidade aceitável para grafos de tamanho moderado

**Por que Vizinho Mais Próximo?**

- O Problema do Caixeiro Viajante é NP-Difícil

- A heurística fornece soluções aproximadas em tempo polinomial

- Adequada para aplicações práticas onde a solução ótima é computacionalmente intratável

**Por que Ford-Fulkerson?**

- Analisa a capacidade da rede em pontos críticos

- Identifica gargalos na infraestrutura

- Fundamental para planejamento de capacidade

---

## 8. Possíveis Extensões

O projeto pode ser estendido com as seguintes melhorias:

1. **Algoritmo A*:** Para busca mais eficiente com heurísticas admissíveis

1. **Algoritmo de Christofides:** Para melhor aproximação do PCV

1. **Fluxo com Custo Mínimo:** Usando algoritmo de Bellman-Ford

1. **Visualização Gráfica:** Usando bibliotecas como NetworkX e Matplotlib

1. **Análise de Conectividade:** Verificação de grafos h-conexos

1. **Coloração de Grafos:** Para alocação de horários de entrega

1. **Emparelhamentos:** Para alocação ótima de entregadores a rotas

---

## 9. Conclusões

O projeto implementa com sucesso uma aplicação prática de Teoria dos Grafos para otimização logística. As três técnicas aplicadas (Dijkstra, Vizinho Mais Próximo e Ford-Fulkerson) cobrem diferentes aspectos do problema:

- **Dijkstra** resolve o problema de roteamento ponto-a-ponto

- **Vizinho Mais Próximo** otimiza rotas com múltiplos pontos

- **Ford-Fulkerson** analisa a capacidade da rede

A implementação demonstra a relevância prática da Teoria dos Grafos na solução de problemas reais de otimização, mostrando como conceitos teóricos podem ser aplicados efetivamente em cenários do mundo real.

---

## 10. Referências

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

1. Diestel, R. (2017). *Graph Theory* (5th ed.). Springer.

1. Goldbarg, M. C., & Goldbarg, E. (2012). *Grafos: Conceitos, Algoritmos e Aplicações*. Elsevier.

1. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

1. West, D. B. (2001). *Introduction to Graph Theory* (2nd ed.). Prentice Hall.



