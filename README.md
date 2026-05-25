# Aplicação de Otimização Logística de Entrega de Encomendas

Projeto desenvolvido para a disciplina de **Teoria dos Grafos** da Universidade Presbiteriana Mackenzie.

---

# Descrição do Projeto

Aplicação desenvolvida em Python para simulação e otimização logística de entregas utilizando conceitos de Teoria dos Grafos.

O sistema modela uma rede logística urbana através de um grafo ponderado direcionado, permitindo executar algoritmos de caminho mínimo, roteamento e análise de fluxo máximo.

O projeto foi desenvolvido como atividade acadêmica da disciplina de Teoria dos Grafos da Universidade Presbiteriana Mackenzie.

---

# Objetivos

O sistema foi desenvolvido com os seguintes objetivos:

- representar uma rede logística utilizando grafos;
- determinar caminhos mínimos entre pontos da rede;
- otimizar rotas de entrega;
- analisar capacidades e gargalos da infraestrutura;
- aplicar algoritmos clássicos estudados na disciplina;
- demonstrar aplicações práticas da Teoria dos Grafos.

---

# Técnicas e Algoritmos Utilizados

A aplicação implementa três técnicas principais:

## 1. Algoritmo de Dijkstra

Utilizado para determinar o caminho mínimo entre dois vértices do grafo.

### Aplicações

- cálculo da menor distância;
- definição de rotas eficientes;
- minimização de custos de deslocamento.

### Complexidade

```math
O((V + E) \log V)
```

---

## 2. Heurística do Vizinho Mais Próximo

Aplicada ao Problema do Caixeiro Viajante para otimização de rotas com múltiplos pontos.

### Aplicações

- planejamento de sequência de entregas;
- otimização logística;
- redução de distância percorrida.

### Característica

A heurística produz soluções aproximadas em tempo polinomial.

---

## 3. Algoritmo de Ford-Fulkerson

Utilizado para cálculo de fluxo máximo em redes.

### Aplicações

- identificação de gargalos;
- análise da capacidade da rede;
- avaliação de regiões críticas.

### Complexidade

```math
O(E \cdot f^*)
```

---

# Características do Grafo

| Característica     | Valor             |
| ------------------ | ----------------- |
| Número de vértices | 73                |
| Número de arestas  | 219               |
| Tipo               | Grafo direcionado |
| Ponderação         | Sim               |
| Grau máximo        | 17                |
| Densidade          | 0,041             |

---

# Estrutura do Projeto

```text
projeto_teoria_grafos/
├── grafo.txt
├── aplicacao_entrega.py
├── definicao_e_modelagem.md
├── RELATORIO_PROJETO.md
├── README.md
└── assets/
```

---

# Requisitos

Para execução da aplicação é necessário:

- Python 3.7 ou superior;
- sistema operacional Linux, Windows ou macOS.

O projeto não utiliza dependências externas.

---

# Execução da Aplicação

## 1. Preparação

Certifique-se de que os arquivos `grafo.txt` e `aplicacao_entrega.py` estejam no mesmo diretório.

---

## 2. Execução

```bash
python3 aplicacao_entrega.py
```

---

# Menu da Aplicação

A aplicação apresenta um menu interativo contendo as seguintes funcionalidades:

```text
============================================================
APLICAÇÃO DE OTIMIZAÇÃO LOGÍSTICA DE ENTREGA
Teoria dos Grafos - Universidade Presbiteriana Mackenzie
============================================================

1. Carregar grafo do arquivo
2. Exibir estatísticas do grafo
3. Encontrar caminho mínimo (Dijkstra)
4. Otimizar rota de entrega (Vizinho Mais Próximo)
5. Calcular fluxo máximo (Ford-Fulkerson)
6. Listar todos os vértices
7. Sair
```

---

# Formato do Arquivo `grafo.txt`

O arquivo responsável pela modelagem do grafo segue a estrutura:

```text
VERTICES
deposito_central
coleta_norte_1
coleta_norte_2

ARESTAS
deposito_central coleta_norte_1 15
deposito_central coleta_norte_2 18
```

Cada aresta contém:

- vértice de origem;
- vértice de destino;
- peso associado.

---

# Modelagem do Problema

O sistema foi modelado como um grafo ponderado direcionado:

```math
G = (V, E)
```

Onde:

- $V$ representa o conjunto de vértices;
- $E$ representa o conjunto de arestas.

Os vértices representam:

- depósito central;
- pontos de coleta;
- pontos de entrega;
- centros de distribuição;
- cruzamentos e conexões urbanas.

As arestas representam conexões entre diferentes regiões da malha urbana.

---

# Possíveis Extensões

O projeto pode ser expandido futuramente com:

- algoritmo A\*;
- algoritmo de Bellman-Ford;
- visualização gráfica;
- integração com APIs de mapas;
- análise de centralidade;
- coloração de grafos;
- análise dinâmica de tráfego.

---

# Documentação Complementar

Arquivos adicionais do projeto:

| Arquivo                    | Descrição                        |
| -------------------------- | -------------------------------- |
| `RELATORIO_PROJETO.md`     | Relatório acadêmico completo     |
| `definicao_e_modelagem.md` | Descrição detalhada da modelagem |
| `grafo.txt`                | Estrutura de dados do grafo      |

---

# Licença

Este projeto possui finalidade exclusivamente acadêmica e educacional.

---

# Última Atualização

25 de maio de 2026.

