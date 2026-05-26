# Relatório do Projeto: Aplicação para Resolução de Categorias de Problemas com Grafos

**Disciplina:** Teoria dos Grafos (Turma 6G)**Período:** 2026/1**Universidade:** Universidade Presbiteriana Mackenzie**Faculdade:** Faculdade de Computação e Informática**Professor:** Prof. Dr. Ivan Carlos Alcântara de Oliveira

**INTEGRANTES DO GRUPO:**

- **Nome:** Milton Almeida Leoncio

- **RA:** 10416764

---

## 1. Título da Aplicação

**Sistema de Otimização Logística e Análise de Malha Viária Metropolitana (SOL-AVM)**

---

## 2. Introdução e Definição do Problema

### 2.1 Descrição do Problema Real

O problema abordado é a **otimização logística de entrega de encomendas em uma área metropolitana**. Uma empresa de logística precisa gerenciar uma frota de veículos que operam a partir de um depósito central para atender dezenas de pontos de coleta e entrega espalhados por uma malha viária complexa.

O desafio consiste em:

- **Roteamento Eficiente:** Encontrar os caminhos mais curtos entre pontos para reduzir consumo de combustível e tempo.

- **Planejamento de Sequência:** Determinar a melhor ordem de visitação de múltiplos pontos (Problema do Caixeiro Viajante).

- **Capacidade de Rede:** Avaliar o fluxo máximo suportado por trechos da cidade para evitar congestionamentos e gargalos.

- **Análise de Conflitos:** Organizar janelas de entrega ou atribuição de frotas para evitar sobreposição em áreas críticas.

### 2.2 Modelagem do Grafo

O problema foi modelado como um **grafo ponderado direcionado** G = (V, E), onde:

- **Vértices (V):** Representam 73 locais distintos, incluindo 1 Depósito Central, 26 Pontos de Coleta, 36 Pontos de Entrega, 4 Centros de Distribuição e 6 Cruzamentos Estratégicos.

- **Arestas (E):** Representam 219 trechos de vias urbanas. Os pesos das arestas correspondem ao custo logístico (uma composição de tempo e distância).

- **Direcionalidade:** As arestas são direcionadas para representar mãos de direção das vias urbanas.

---

## 3. Objetivos de Desenvolvimento Sustentável (ODS)

Este projeto contempla os seguintes objetivos da Agenda 2030 da ONU:

| ODS | Justificativa no Projeto |
| --- | --- |
| **ODS 9: Indústria, Inovação e Infraestrutura** | O uso de algoritmos de grafos (Ford-Fulkerson) permite identificar gargalos na infraestrutura urbana e otimizar o fluxo de mercadorias, promovendo uma logística mais resiliente e inovadora. |
| **ODS 11: Cidades e Comunidades Sustentáveis** | Ao otimizar rotas com Dijkstra e Vizinho Mais Próximo, reduz-se o tempo de permanência de veículos de carga nas ruas, diminuindo o tráfego urbano e as emissões de poluentes, contribuindo para cidades mais limpas. |
| **ODS 12: Consumo e Produção Responsáveis** | A eficiência logística reduz o desperdício de recursos (combustível e pneus) e melhora a gestão da cadeia de suprimentos, promovendo padrões de produção e distribuição mais sustentáveis. |

---

## 4. Técnicas de Teoria dos Grafos Aplicadas

### 4.1 Algoritmos de Otimização

1. **Algoritmo de Dijkstra:** Utilizado para encontrar a rota de custo mínimo entre o depósito e qualquer ponto de entrega.

1. **Heurística do Vizinho Mais Próximo:** Aplicada para fornecer uma solução viável ao Problema do Caixeiro Viajante, organizando a sequência de entregas.

1. **Algoritmo de Ford-Fulkerson:** Utilizado para calcular o fluxo máximo de veículos/encomendas que a malha viária suporta entre dois pontos críticos.

### 4.2 Análise Estrutural (Requisito 2)

1. **Grau dos Vértices:** Identificação de "Hubs" logísticos através dos graus de entrada e saída.

1. **Verificação Euleriana:** Análise da paridade dos graus para determinar se a rede permite percursos que cubram todas as vias sem repetição.

1. **Coloração de Vértices:** Utilizada para particionar os pontos de entrega em grupos independentes, facilitando o escalonamento de equipes de entrega que não interferem entre si.

---

## 5. Printscreens e Testes de Execução

Abaixo constam os logs de testes realizados para cada opção do menu da aplicação:

### Teste 1: Carregamento e Estatísticas

```
Opção: 1 (Carregar grafo.txt) -> ✓ Grafo carregado com sucesso! (73 Vértices, 219 Arestas)
Opção: 2 (Estatísticas) -> Grafo Conexo: Sim | Classificação: Não Euleriano (48 vértices ímpares)
```

### Teste 2: Caminho Mínimo (Dijkstra)

```
Origem: deposito_central | Destino: entrega_norte_1
Resultado: Distância 27 | Caminho: deposito_central → coleta_norte_1 → entrega_norte_1
```

### Teste 3: Rota Otimizada (Vizinho Mais Próximo)

```
Origem: deposito_central | Visitas: coleta_norte_1, coleta_norte_2, entrega_norte_1
Resultado: Custo 121 | Rota: deposito_central → coleta_norte_1 → coleta_norte_2 → entrega_norte_1 → deposito_central
```

### Teste 4: Fluxo Máximo (Ford-Fulkerson)

```
Origem: deposito_central | Destino: entrega_norte_1
Resultado: Fluxo Máximo 23
```

### Teste 5: Coloração de Vértices

```
Resultado: Número Cromático Estimado (X(G)): 5
Partições: Cor 1 (18 vértices), Cor 2 (15 vértices), Cor 3 (14 vértices)...
```

---

## 6. Conclusões

O sistema SOL-AVM demonstra como a Teoria dos Grafos provê ferramentas matemáticas robustas para resolver problemas complexos de logística urbana. A integração de algoritmos de busca, fluxo e coloração permite uma visão 360º do problema, desde a execução de uma entrega individual até o planejamento macro da infraestrutura da cidade.

---

## 7. Apêndice

### Links do Projeto

- **GitHub:** [https://github.com/miltonleoncio/projeto-grafos-mackenzie](https://github.com/NewsMoney/Projeto-P3-Grafos)

### Estrutura de Arquivos

- `aplicacao_entrega.py`: Código fonte com cabeçalho e histórico.

- `grafo.txt`: Dados do modelo (73 vértices, 219 arestas).

- `README.md`: Instruções de instalação e uso.

---

**Data de Entrega:** 25 de maio de 2026

