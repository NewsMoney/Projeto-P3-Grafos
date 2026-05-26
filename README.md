# Aplicação de Otimização Logística de Entrega de Encomendas

Projeto da disciplina de **Teoria dos Grafos** (Turma 6G, 2026/1) da Universidade Presbiteriana Mackenzie.

## Descrição

Esta aplicação implementa uma solução prática para otimização de rotas de entrega em uma área metropolitana, utilizando três técnicas fundamentais de Teoria dos Grafos:

1. **Algoritmo de Dijkstra** - Encontrar caminhos mínimos
2. **Heurística do Vizinho Mais Próximo** - Resolver o Problema do Caixeiro Viajante
3. **Algoritmo de Ford-Fulkerson** - Calcular fluxo máximo

## Características

- **Grafo Realista:** 73 vértices e 219 arestas representando uma área metropolitana
- **Interface Interativa:** Menu de fácil uso para executar diferentes algoritmos
- **Sem Dependências Externas:** Utiliza apenas bibliotecas padrão do Python
- **Documentação Completa:** Código comentado e relatório detalhado

## Estrutura do Projeto

```
projeto_teoria_grafos/
├── grafo.txt                    # Dados do grafo (vértices e arestas)
├── aplicacao_entrega.py         # Aplicação principal
├── definicao_e_modelagem.md     # Documentação da modelagem do problema
├── RELATORIO_PROJETO.md         # Relatório completo do projeto
└── README.md                    # Este arquivo
```

## Requisitos

- Python 3.7 ou superior
- Sistema operacional: Linux, macOS ou Windows

## Como Executar

### 1. Preparação

Certifique-se de que o arquivo `grafo.txt` está no mesmo diretório que `aplicacao_entrega.py`.

### 2. Executar a Aplicação

```bash
python3 aplicacao_entrega.py
```

### 3. Usar o Menu Interativo

Após iniciar a aplicação, você verá um menu com as seguintes opções:

```
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

## Exemplos de Uso

### Exemplo 1: Carregar o Grafo e Exibir Estatísticas

```
Escolha uma opção: 1
Digite o nome do arquivo (padrão: grafo.txt): grafo.txt
✓ Grafo carregado com sucesso!
  - Vértices: 73
  - Arestas: 219

Escolha uma opção: 2
============================================================
ESTATÍSTICAS DO GRAFO
============================================================
Número de vértices: 73
Número de arestas: 219
Grau médio: 3.00
Grau máximo: 17
============================================================
```

### Exemplo 2: Encontrar Caminho Mínimo

```
Escolha uma opção: 3
Digite o vértice de origem: deposito_central
Digite o vértice de destino: entrega_norte_1

============================================================
CAMINHO MÍNIMO (ALGORITMO DE DIJKSTRA)
============================================================
Origem: deposito_central
Destino: entrega_norte_1
Distância mínima: 27
Caminho: deposito_central → coleta_norte_1 → entrega_norte_1
============================================================
```

### Exemplo 3: Otimizar Rota de Entrega

```
Escolha uma opção: 4
Digite o ponto de origem (depósito): deposito_central
Digite os pontos a visitar (separados por vírgula): coleta_norte_1, coleta_norte_2, entrega_norte_1

============================================================
ROTA OTIMIZADA (VIZINHO MAIS PRÓXIMO)
============================================================
Ponto de origem: deposito_central
Custo total da rota: 68
Rota: deposito_central → coleta_norte_1 → coleta_norte_2 → entrega_norte_1 → deposito_central
============================================================
```

### Exemplo 4: Calcular Fluxo Máximo

```
Escolha uma opção: 5
Digite o vértice de origem (fonte): deposito_central
Digite o vértice de destino (sumidouro): entrega_norte_1

============================================================
FLUXO MÁXIMO (ALGORITMO DE FORD-FULKERSON)
============================================================
Origem (fonte): deposito_central
Destino (sumidouro): entrega_norte_1
Fluxo máximo: 27
============================================================
```

## Formato do Arquivo de Dados (grafo.txt)

O arquivo `grafo.txt` contém a definição do grafo em um formato estruturado:

```
VERTICES
deposito_central
coleta_norte_1
coleta_norte_2
...
entrega_norte_1
...

ARESTAS
deposito_central coleta_norte_1 15
deposito_central coleta_norte_2 18
coleta_norte_1 entrega_norte_1 12
...
```

**Formato das arestas:** `origem destino peso`

- `origem`: Vértice de origem da aresta
- `destino`: Vértice de destino da aresta
- `peso`: Peso da aresta (tempo, distância ou custo)

## Algoritmos Implementados

### Algoritmo de Dijkstra

Encontra o caminho de menor peso entre dois vértices em um grafo com pesos não-negativos.

- **Complexidade:** O((V + E) log V) com heap binário
- **Aplicação:** Determinar a rota mais rápida ou curta entre dois pontos

### Heurística do Vizinho Mais Próximo

Resolve aproximadamente o Problema do Caixeiro Viajante, visitando pontos na ordem do vizinho mais próximo.

- **Complexidade:** O(n² · (V + E) log V)
- **Aplicação:** Otimizar a sequência de coleta e entrega de encomendas

### Algoritmo de Ford-Fulkerson

Calcula o fluxo máximo em uma rede de fluxo.

- **Complexidade:** O(E · f*) onde f* é o fluxo máximo
- **Aplicação:** Analisar a capacidade da rede em pontos críticos

## Modelagem do Problema

### Vértices

O grafo contém 73 vértices representando:

- **1 Depósito Central:** Ponto de partida e retorno
- **26 Pontos de Coleta:** Locais onde buscar encomendas
- **36 Pontos de Entrega:** Locais onde deixar encomendas
- **4 Centros de Distribuição:** Pontos de distribuição secundários
- **6 Cruzamentos:** Pontos de transição na malha viária
- **4 Pontos Estratégicos:** Pontos adicionais para conectividade

### Arestas

O grafo contém 219 arestas representando:

- Conexões entre depósito e pontos de coleta/entrega
- Conexões entre pontos de coleta
- Conexões entre pontos de entrega
- Conexões entre cruzamentos (malha viária)
- Conexões entre centros de distribuição

## Contribuições Esperadas

Este projeto demonstra a aplicação prática de Teoria dos Grafos em:

- **Otimização Logística:** Planejamento eficiente de rotas
- **Análise de Redes:** Identificação de gargalos e capacidades
- **Algoritmos Clássicos:** Implementação de algoritmos fundamentais

## Documentação Adicional

Para mais detalhes sobre a modelagem e análise, consulte:

- `definicao_e_modelagem.md` - Descrição detalhada do problema e modelagem
- `RELATORIO_PROJETO.md` - Relatório completo com análise teórica e resultados

## Autor

Desenvolvido como projeto da disciplina de Teoria dos Grafos (2026/1) da Universidade Presbiteriana Mackenzie.

## Licença

Este projeto é fornecido para fins educacionais.

---

**Última atualização:** 25 de maio de 2026
