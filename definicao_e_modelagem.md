# Definição do Problema e Modelagem do Grafo

# 1. Definição do Problema Real

O presente projeto aborda o problema de otimização logística de entrega de encomendas em uma área metropolitana, considerando aspectos relacionados ao planejamento de rotas, distribuição urbana e análise da capacidade da infraestrutura logística.

Empresas de transporte e entrega enfrentam desafios constantes relacionados à redução de custos operacionais, diminuição do tempo de entrega e melhoria da eficiência da malha logística. Nesse contexto, técnicas de Teoria dos Grafos podem ser utilizadas para representar e analisar redes urbanas complexas.

O objetivo principal da aplicação consiste em determinar rotas eficientes para coleta e entrega de encomendas, minimizando custos de deslocamento e identificando gargalos da rede.

---

## 1.1 Cenário Modelado

A rede logística desenvolvida representa uma estrutura urbana dividida em diferentes regiões da cidade:

* norte;
* sul;
* leste;
* oeste;
* centro.

O sistema modelado contempla:

* 1 depósito central;
* 25 pontos de coleta;
* 30 pontos de entrega;
* centros de distribuição regionais;
* cruzamentos estratégicos;
* pontos de conexão urbana.

A modelagem totaliza:

* **73 vértices**
* **219 arestas direcionadas e ponderadas**

As arestas representam conexões viárias entre diferentes regiões da cidade, enquanto os pesos representam custos de deslocamento associados ao trajeto.

---

# 2. Modelagem do Problema como Grafo

O sistema foi modelado como um grafo ponderado direcionado:

```math
G = (V, E)
```

Onde:

* (V) representa o conjunto de vértices;
* (E) representa o conjunto de arestas direcionadas.

O direcionamento das arestas permite representar:

* ruas de mão única;
* fluxo urbano;
* restrições de deslocamento;
* conectividade assimétrica entre regiões.

---

## 2.1 Vértices

Os vértices representam elementos relevantes da infraestrutura logística urbana.

### Depósito Central

Representa o ponto principal de saída e retorno das operações logísticas.

Exemplo:

```text
deposito_central
```

---

### Pontos de Coleta

Representam locais responsáveis pela coleta inicial de encomendas.

Exemplos:

```text
coleta_norte_1
coleta_centro_3
coleta_sul_2
```

---

### Pontos de Entrega

Representam os destinos finais das encomendas.

Exemplos:

```text
entrega_leste_4
entrega_oeste_2
entrega_centro_5
```

---

### Cruzamentos Estratégicos

Representam conexões relevantes da malha viária.

Exemplos:

```text
cruzamento_norte_central
cruzamento_sul_leste
cruzamento_oeste_central
```

Esses vértices aumentam a conectividade do grafo e tornam a modelagem mais realista.

---

### Centros de Distribuição

Representam pontos intermediários de redistribuição logística.

Exemplos:

```text
centro_distribuicao_norte
centro_distribuicao_sul
```

---

## 2.2 Arestas

As arestas representam conexões entre vértices da rede logística.

Cada aresta possui um peso associado:

```math
w(u,v)
```

Onde o peso representa:

* tempo estimado de deslocamento;
* distância percorrida;
* custo operacional do trajeto.

Exemplo extraído do arquivo `grafo.txt`:

```text
deposito_central coleta_norte_1 15
```

Nesse caso:

* origem: `deposito_central`
* destino: `coleta_norte_1`
* peso: `15`

---

## 2.3 Estrutura de Dados

O grafo foi implementado utilizando lista de adjacências, estrutura adequada para grafos esparsos e eficiente em termos computacionais.

Exemplo:

```python
{
    "deposito_central": [
        ("coleta_norte_1", 15),
        ("cruzamento_centro_leste", 6)
    ],

    "coleta_norte_1": [
        ("entrega_norte_1", 12)
    ]
}
```

Essa estrutura permite:

* inserção eficiente de arestas;
* melhor desempenho em algoritmos de busca;
* redução de consumo de memória.

---

# 3. Técnicas de Teoria dos Grafos Aplicadas

Foram implementadas técnicas clássicas de Teoria dos Grafos para resolução de diferentes aspectos do problema logístico.

---

## 3.1 Algoritmo de Dijkstra

O algoritmo de Dijkstra foi utilizado para determinação de caminhos mínimos entre vértices da rede.

### Objetivos

* minimizar distância percorrida;
* reduzir tempo de entrega;
* encontrar trajetos mais eficientes.

### Aplicações

* rota entre depósito e ponto de coleta;
* deslocamento entre entregas;
* planejamento de trajetos urbanos.

### Complexidade

```math
O((V + E)\log V)
```

A implementação utiliza fila de prioridade baseada em heap binário.

---

## 3.2 Problema do Caixeiro Viajante

Foi utilizada a heurística do Vizinho Mais Próximo para otimização de rotas envolvendo múltiplos pontos.

### Objetivos

* reduzir custo total da rota;
* otimizar sequência de visitas;
* melhorar eficiência operacional.

### Justificativa

O Problema do Caixeiro Viajante possui elevada complexidade computacional, tornando inviável a busca exata para grandes redes. Dessa forma, foi utilizada uma abordagem heurística capaz de produzir soluções aproximadas em tempo viável.

---

## 3.3 Algoritmo de Ford-Fulkerson

O algoritmo de Ford-Fulkerson foi utilizado para análise de fluxo máximo na rede logística.

### Objetivos

* identificar gargalos;
* analisar capacidade da rede;
* avaliar regiões críticas da infraestrutura.

### Aplicações

* análise da capacidade entre centros de distribuição;
* avaliação de trechos sobrecarregados;
* estudo do fluxo máximo de encomendas.

### Complexidade

```math
O(E \cdot f^*)
```

Onde (f^*) representa o fluxo máximo encontrado.

---

# 4. Considerações Finais da Modelagem

A modelagem proposta permite representar de forma realista uma rede logística urbana utilizando conceitos fundamentais da Teoria dos Grafos.

A utilização de grafos ponderados direcionados possibilita analisar:

* rotas mínimas;
* eficiência logística;
* capacidade operacional;
* conectividade urbana;
* fluxo de distribuição.

Além disso, a implementação desenvolvida fornece base para futuras expansões, incluindo visualização gráfica, integração com mapas urbanos e análise dinâmica de tráfego em tempo real.
