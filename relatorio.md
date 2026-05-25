<!-- Arquivo Markdown (.md) pronto para exportação e uso acadêmico -->

# RELATÓRIO DO PROJETO
## Aplicação para Resolução de Categorias de Problemas com Grafos

**Disciplina:** Teoria dos Grafos – Turma 6G  
**Professor:** Prof. Dr. Ivan Carlos Alcântara de Oliveira  
**Universidade:** Universidade Presbiteriana Mackenzie  
**Faculdade:** Faculdade de Computação e Informática  
**Período:** 2026/1  

---

# SUMÁRIO

1. Introdução  
2. Definição do Problema  
3. Objetivos do Projeto  
4. Objetivos de Desenvolvimento Sustentável (ODS)  
5. Modelagem do Problema com Grafos  
6. Técnicas de Teoria dos Grafos Aplicadas  
7. Estrutura da Implementação  
8. Resultados Obtidos  
9. Análise Computacional  
10. Desafios Encontrados  
11. Possíveis Extensões  
12. Conclusão  
13. Referências  
14. Apêndice  

---

# 1. INTRODUÇÃO

A Teoria dos Grafos constitui uma importante área da Ciência da Computação e da Matemática Discreta, sendo amplamente utilizada na modelagem e resolução de problemas relacionados a redes, logística, comunicação, transporte, distribuição e otimização.

O presente projeto tem como objetivo desenvolver uma aplicação computacional capaz de modelar e resolver um problema real de logística de entregas utilizando conceitos fundamentais da disciplina de Teoria dos Grafos. A aplicação foi desenvolvida utilizando linguagem Python e implementa diferentes algoritmos estudados ao longo da disciplina, permitindo analisar rotas, fluxos e características estruturais da rede modelada.

O problema selecionado representa um sistema de entregas em uma área metropolitana, no qual pontos de coleta, entrega, centros de distribuição e conexões viárias são representados por vértices e arestas de um grafo ponderado direcionado.

A proposta busca demonstrar a aplicabilidade prática dos conceitos teóricos estudados em sala de aula, evidenciando como algoritmos clássicos podem ser utilizados para solucionar problemas reais de otimização logística.

---

# 2. DEFINIÇÃO DO PROBLEMA

## 2.1 Contextualização

Empresas de logística e transporte enfrentam diariamente desafios relacionados ao planejamento eficiente de rotas, redução de custos operacionais e melhoria da eficiência das entregas.

O crescimento urbano e o aumento da demanda por entregas tornam necessário o desenvolvimento de sistemas capazes de:

- reduzir distâncias percorridas;
- minimizar o tempo total de entrega;
- evitar congestionamentos;
- identificar gargalos na malha viária;
- otimizar a utilização da frota de entregadores.

Diante desse cenário, foi desenvolvido um sistema baseado em grafos para representar a infraestrutura logística de uma região metropolitana.

---

## 2.2 Descrição do Cenário

O sistema modelado contempla:

- 1 depósito central;
- 26 pontos de coleta;
- 36 pontos de entrega;
- 11 vértices intermediários representando cruzamentos e conexões viárias;
- 4 centros de distribuição secundários.

A rede total possui:

- **73 vértices**
- **219 arestas**

As arestas representam ruas e avenidas conectando diferentes regiões da cidade, enquanto os pesos associados representam custo, distância ou tempo médio de deslocamento.

---

# 3. OBJETIVOS DO PROJETO

## 3.1 Objetivo Geral

Desenvolver uma aplicação computacional baseada em Teoria dos Grafos para modelar e otimizar um sistema logístico de entregas urbanas.

---

## 3.2 Objetivos Específicos

- Implementar algoritmos clássicos de Teoria dos Grafos;
- Modelar um problema real utilizando grafos ponderados;
- Determinar caminhos mínimos entre pontos da rede;
- Analisar capacidades e gargalos da infraestrutura;
- Investigar características estruturais do grafo;
- Produzir análises quantitativas sobre a rede logística.

---

# 4. OBJETIVOS DE DESENVOLVIMENTO SUSTENTÁVEL (ODS)

O projeto apresenta relação direta com os Objetivos de Desenvolvimento Sustentável definidos pela Organização das Nações Unidas (ONU).

## ODS 9 – Indústria, Inovação e Infraestrutura

A aplicação contribui para a melhoria da eficiência logística e otimização da infraestrutura urbana, utilizando tecnologia computacional para análise de redes.

## ODS 11 – Cidades e Comunidades Sustentáveis

A otimização de rotas reduz congestionamentos, melhora a mobilidade urbana e contribui para sistemas de transporte mais eficientes.

## ODS 13 – Ação Contra a Mudança Global do Clima

A redução de trajetos desnecessários contribui para menor emissão de gases poluentes e redução do consumo de combustível.

---

# 5. MODELAGEM DO PROBLEMA COM GRAFOS

O problema foi modelado como um grafo ponderado direcionado:

```math
G = (V, E)
```

Onde:

- \(V\) representa o conjunto de vértices;
- \(E\) representa o conjunto de arestas direcionadas.

Os vértices representam:

- depósitos;
- pontos de coleta;
- pontos de entrega;
- centros de distribuição;
- conexões viárias.

As arestas representam conexões entre regiões da cidade.

Cada aresta possui um peso associado:

```math
w(e) = d(e) + t(e)
```

Onde:

- \(d(e)\) representa distância;
- \(t(e)\) representa tempo médio de deslocamento.

---

## 5.1 Características do Grafo

| Característica | Valor |
|---|---|
| Número de vértices | 73 |
| Número de arestas | 219 |
| Grau médio | 3,00 |
| Grau máximo | 17 |
| Densidade | 0,041 |
| Tipo | Direcionado |
| Ponderação | Sim |

---

# 6. TÉCNICAS DE TEORIA DOS GRAFOS APLICADAS

## 6.1 Algoritmo de Dijkstra

O algoritmo de Dijkstra foi utilizado para determinar caminhos mínimos entre diferentes pontos da rede logística.

### Objetivos

- encontrar a rota mais curta;
- minimizar tempo de deslocamento;
- reduzir custos operacionais.

### Complexidade

```math
O((V + E) \log V)
```

### Aplicações

- rota entre depósito e ponto de entrega;
- cálculo de menor distância;
- planejamento de deslocamento.

---

## 6.2 Heurística do Vizinho Mais Próximo

A heurística do Vizinho Mais Próximo foi aplicada ao Problema do Caixeiro Viajante.

### Objetivos

- determinar sequência eficiente de visitas;
- reduzir distância percorrida;
- otimizar rotas múltiplas.

### Funcionamento

1. inicia no depósito central;
2. seleciona o vértice não visitado mais próximo;
3. repete o processo até visitar todos os pontos;
4. retorna ao ponto inicial.

### Limitações

A heurística não garante solução ótima global, porém apresenta baixo custo computacional e desempenho satisfatório para aplicações práticas.

---

## 6.3 Algoritmo de Ford-Fulkerson

O algoritmo de Ford-Fulkerson foi utilizado para análise de fluxo máximo na rede.

### Objetivos

- identificar gargalos;
- analisar capacidade da rede;
- avaliar limites operacionais.

### Complexidade

```math
O(E \cdot f^*)
```

Onde \(f^*\) representa o fluxo máximo encontrado.

---

# 7. ESTRUTURA DA IMPLEMENTAÇÃO

O projeto foi desenvolvido utilizando linguagem Python.

## 7.1 Estrutura de Arquivos

```text
projeto_teoria_grafos/
├── grafo.txt
├── aplicacao_entrega.py
├── RELATORIO_PROJETO.md
├── README.md
└── definicao_e_modelagem.md
```

---

## 7.2 Classe Principal

A aplicação utiliza a classe `GrafoEntrega`, responsável pela manipulação do grafo e execução dos algoritmos.

### Principais Métodos

| Método | Função |
|---|---|
| carregar_de_arquivo() | Carrega o grafo |
| dijkstra() | Caminho mínimo |
| vizinho_mais_proximo() | Otimização de rotas |
| ford_fulkerson() | Fluxo máximo |
| obter_estatisticas() | Estatísticas do grafo |
| listar_vertices() | Exibição dos vértices |

---

# 8. RESULTADOS OBTIDOS

A aplicação apresentou funcionamento adequado para os cenários testados.

## 8.1 Caminhos Mínimos

O algoritmo de Dijkstra permitiu determinar rotas eficientes entre diferentes pontos da rede logística.

---

## 8.2 Otimização de Rotas

A heurística do Vizinho Mais Próximo reduziu significativamente o custo total das rotas planejadas.

---

## 8.3 Fluxo Máximo

O algoritmo de Ford-Fulkerson possibilitou identificar regiões críticas da rede e limitações estruturais.

---

## 8.4 Características Estruturais Investigadas

Durante a análise do grafo foram investigadas:

- grau dos vértices;
- densidade da rede;
- conectividade;
- distribuição de conexões;
- existência de gargalos;
- capacidade de fluxo.

---

# 9. ANÁLISE COMPUTACIONAL

| Algoritmo | Complexidade | Finalidade |
|---|---|---|
| Dijkstra | O((V+E)logV) | Caminho mínimo |
| Vizinho Mais Próximo | O(n²) | Roteamento |
| Ford-Fulkerson | O(E*f*) | Fluxo máximo |

---

## 9.1 Comparação das Técnicas

| Técnica | Vantagens | Limitações |
|---|---|---|
| Dijkstra | Alta precisão | Não aceita pesos negativos |
| Vizinho Mais Próximo | Baixo custo computacional | Não garante solução ótima |
| Ford-Fulkerson | Excelente análise de capacidade | Custo elevado em redes grandes |

---

# 10. DESAFIOS ENCONTRADOS

Durante o desenvolvimento do projeto foram identificados diversos desafios técnicos, dentre os quais destacam-se:

- modelagem adequada da rede logística;
- definição dos pesos das arestas;
- garantia de conectividade do grafo;
- tratamento de ciclos;
- organização eficiente da estrutura de dados;
- implementação correta dos algoritmos;
- controle da complexidade computacional.

Além disso, houve preocupação com a escalabilidade da aplicação, visando permitir expansão futura da rede modelada.

---

# 11. POSSÍVEIS EXTENSÕES

O projeto pode ser expandido futuramente com:

- algoritmo A*;
- algoritmo de Bellman-Ford;
- análise de centralidade;
- coloração de grafos;
- emparelhamentos;
- visualização gráfica dinâmica;
- integração com APIs de mapas;
- análise em tempo real do trânsito urbano.

---

# 12. CONCLUSÃO

O projeto demonstrou a aplicabilidade prática da Teoria dos Grafos na resolução de problemas logísticos reais.

Os algoritmos implementados permitiram:

- determinar caminhos mínimos;
- otimizar rotas;
- analisar capacidades da rede;
- investigar características estruturais do sistema.

A utilização de grafos mostrou-se eficiente para representação da infraestrutura logística urbana, permitindo análises computacionais relevantes e soluções aplicáveis ao contexto real.

Além disso, o projeto evidencia como conceitos teóricos estudados em disciplinas de Matemática Discreta e Ciência da Computação podem ser utilizados para solucionar problemas concretos relacionados à mobilidade, transporte e logística.

---

# 13. REFERÊNCIAS

1. CORMEN, Thomas H. et al. *Introduction to Algorithms*. 3. ed. MIT Press, 2009.

2. DIESTEL, Reinhard. *Graph Theory*. 5. ed. Springer, 2017.

3. GOLDBARG, Marco César; GOLDBARG, Elizabeth. *Grafos: Conceitos, Algoritmos e Aplicações*. Elsevier, 2012.

4. SEDGEWICK, Robert; WAYNE, Kevin. *Algorithms*. 4. ed. Addison-Wesley, 2011.

5. WEST, Douglas B. *Introduction to Graph Theory*. 2. ed. Prentice Hall, 2001.

---

# 14. APÊNDICE

## Repositório GitHub

[Link do repositorio do GitHub.](https://github.com/NewsMoney/Projeto-P3-Grafos/blob/main/README.md)

---

## Vídeo de Apresentação

Link do vídeo publicado no YouTube.

---

## Dados dos Integrantes

| Nome | RA |
|---|---|
| Milton Almeida Leoncio | 10416764 |


