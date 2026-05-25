# Definição do Problema e Modelagem do Grafo

# 1. Definição do Problema Real

O problema abordado neste projeto consiste na otimização logística de entrega de encomendas em uma área metropolitana. Empresas de transporte e distribuição enfrentam diariamente desafios relacionados ao planejamento eficiente de rotas, redução de custos operacionais e minimização do tempo de entrega.

A aplicação desenvolvida busca representar computacionalmente uma rede logística urbana, permitindo analisar trajetos, capacidades da infraestrutura e eficiência operacional por meio de técnicas de Teoria dos Grafos.

O objetivo principal consiste em minimizar o custo total das entregas, considerando fatores como:

* distância percorrida;
* tempo estimado de deslocamento;
* conectividade da malha viária;
* capacidade operacional da rede;
* eficiência das rotas de coleta e entrega.

---

## 1.1 Cenário do Problema

O cenário modelado contempla:

* um depósito central responsável pelo despacho das encomendas;
* pontos de coleta distribuídos em diferentes regiões;
* pontos de entrega localizados em áreas urbanas distintas;
* centros de distribuição secundários;
* cruzamentos e conexões estratégicas da malha viária.

A rede logística foi modelada utilizando:

* 73 vértices;
* 219 arestas direcionadas e ponderadas.

Os pesos das arestas representam custos associados ao deslocamento, como tempo médio de percurso ou distância estimada.

---

# 2. Modelagem do Problema como Grafo

O sistema foi modelado como um grafo ponderado direcionado:

```math
G = (V, E)
```

Onde:

* (V) representa o conjunto de vértices;
* (E) representa o conjunto de arestas direcionadas.

O direcionamento das arestas permite representar ruas de mão única e restrições de tráfego urbano.

---

## 2.1 Vértices

Os vértices do grafo representam elementos relevantes da infraestrutura logística:

* depósito central;
* pontos de coleta;
* pontos de entrega;
* centros de distribuição;
* cruzamentos e conexões urbanas.

Cada vértice representa uma localização específica da rede logística.

---

## 2.2 Arestas

As arestas representam conexões viárias entre diferentes regiões da cidade.

Cada aresta possui um peso associado:

```math
w(u,v)
```

O peso pode representar:

* tempo estimado de deslocamento;
* distância percorrida;
* custo operacional do trajeto.

A utilização de pesos permite que algoritmos de otimização determinem rotas mais eficientes.

---

## 2.3 Estrutura de Dados

O grafo foi implementado utilizando lista de adjacências, permitindo melhor eficiência no armazenamento e manipulação da rede.

Exemplo:

```python
{
    "deposito_central": [
        ("coleta_norte_1", 15),
        ("cruzamento_1", 8)
    ],

    "coleta_norte_1": [
        ("entrega_norte_1", 12)
    ]
}
```

Cada entrada contém:

* vértice de destino;
* peso associado à aresta.

---

# 3. Técnicas de Teoria dos Grafos Aplicadas

Foram aplicadas técnicas clássicas de Teoria dos Grafos para resolver diferentes aspectos do problema logístico.

---

## 3.1 Algoritmo de Dijkstra

O algoritmo de Dijkstra foi utilizado para determinação de caminhos mínimos entre vértices da rede.

### Objetivos

* encontrar rotas mais curtas;
* minimizar tempo de deslocamento;
* reduzir custos operacionais.

### Aplicações

* trajeto entre depósito e ponto de coleta;
* trajeto entre pontos de entrega;
* cálculo de menor distância entre regiões da rede.

---

## 3.2 Problema do Caixeiro Viajante (PCV)

Para otimização de múltiplas entregas foi utilizada a heurística do Vizinho Mais Próximo, aplicada ao Problema do Caixeiro Viajante.

### Objetivos

* otimizar sequência de visitas;
* reduzir distância total percorrida;
* melhorar eficiência das rotas.

### Justificativa

O Problema do Caixeiro Viajante possui elevada complexidade computacional, tornando inviável a busca exata em redes grandes. Dessa forma, foi utilizada uma heurística capaz de produzir soluções aproximadas em tempo polinomial.

---

## 3.3 Algoritmo de Ford-Fulkerson

O algoritmo de Ford-Fulkerson foi aplicado para análise de fluxo máximo na rede logística.

### Objetivos

* identificar gargalos;
* analisar capacidade da infraestrutura;
* avaliar regiões críticas da rede.

### Aplicações

* análise da capacidade de centros de distribuição;
* identificação de trechos sobrecarregados;
* avaliação do fluxo máximo de encomendas.

---

# 4. Considerações Finais da Modelagem

A modelagem proposta permite representar de forma realista uma rede logística urbana, possibilitando aplicação prática de conceitos fundamentais da Teoria dos Grafos.

A utilização de algoritmos clássicos possibilita analisar diferentes aspectos operacionais da rede, incluindo roteamento, otimização de trajetos e capacidade da infraestrutura logística.

Além disso, a modelagem fornece base para futuras expansões, como integração com sistemas de trânsito em tempo real, análise dinâmica de rotas e visualização gráfica da rede.
