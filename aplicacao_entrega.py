"""
Aplicação de Otimização Logística de Entrega de Encomendas
Disciplina: Teoria dos Grafos (2026/1)
Universidade Presbiteriana Mackenzie

Aluno: Milton Almeida Leoncio | RA: 10416764

Técnicas de Teoria dos Grafos Aplicadas:
1. Caminhos Mínimos (Algoritmo de Dijkstra)
2. Problema do Caixeiro Viajante (Heurística do Vizinho Mais Próximo)
3. Fluxo Máximo (Algoritmo de Ford-Fulkerson)
"""

import heapq
import sys
from collections import defaultdict, deque

class GrafoEntrega:
    """Classe que representa o grafo de entrega de encomendas."""
    
    def __init__(self):
        """Inicializa o grafo vazio."""
        self.vertices = set()
        self.arestas = defaultdict(list)  # adjacency list
        self.capacidades = {}  # para fluxo máximo
        
    def adicionar_vertice(self, v):
        """Adiciona um vértice ao grafo."""
        self.vertices.add(v)
    
    def adicionar_aresta(self, u, v, peso):
        """Adiciona uma aresta ponderada ao grafo."""
        self.arestas[u].append((v, peso))
        self.capacidades[(u, v)] = peso
    
    def carregar_de_arquivo(self, nome_arquivo):
        """Carrega o grafo a partir de um arquivo."""
        try:
            with open(nome_arquivo, 'r') as f:
                linhas = f.readlines()
            
            modo = None
            for linha in linhas:
                linha = linha.strip()
                if not linha:
                    continue
                
                if linha == 'VERTICES':
                    modo = 'vertices'
                    continue
                elif linha == 'ARESTAS':
                    modo = 'arestas'
                    continue
                
                if modo == 'vertices':
                    self.adicionar_vertice(linha)
                elif modo == 'arestas':
                    partes = linha.split()
                    if len(partes) == 3:
                        u, v, peso = partes[0], partes[1], int(partes[2])
                        self.adicionar_aresta(u, v, peso)
            
            print(f"✓ Grafo carregado com sucesso!")
            print(f"  - Vértices: {len(self.vertices)}")
            print(f"  - Arestas: {sum(len(adj) for adj in self.arestas.values())}")
            return True
        except FileNotFoundError:
            print(f"✗ Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return False
        except Exception as e:
            print(f"✗ Erro ao carregar arquivo: {e}")
            return False
    
    def dijkstra(self, origem, destino):
        """
        Algoritmo de Dijkstra para encontrar o caminho mínimo.
        
        Retorna: (distância_mínima, caminho)
        """
        if origem not in self.vertices or destino not in self.vertices:
            return None, []
        
        distancias = {v: float('inf') for v in self.vertices}
        distancias[origem] = 0
        predecessores = {v: None for v in self.vertices}
        
        heap = [(0, origem)]
        visitados = set()
        
        while heap:
            dist_atual, u = heapq.heappop(heap)
            
            if u in visitados:
                continue
            
            visitados.add(u)
            
            if u == destino:
                break
            
            for v, peso in self.arestas[u]:
                if v not in visitados:
                    nova_dist = dist_atual + peso
                    if nova_dist < distancias[v]:
                        distancias[v] = nova_dist
                        predecessores[v] = u
                        heapq.heappush(heap, (nova_dist, v))
        
        # Reconstruir caminho
        caminho = []
        v = destino
        while v is not None:
            caminho.append(v)
            v = predecessores[v]
        caminho.reverse()
        
        if caminho[0] != origem:
            return None, []
        
        return distancias[destino], caminho
    
    def vizinho_mais_proximo(self, origem, pontos_visitar):
        """
        Heurística do Vizinho Mais Próximo para o Problema do Caixeiro Viajante.
        
        Retorna: (custo_total, rota)
        """
        if origem not in self.vertices:
            return None, []
        
        rota = [origem]
        nao_visitados = set(pontos_visitar) - {origem}
        custo_total = 0
        
        while nao_visitados:
            atual = rota[-1]
            
            # Encontrar o vizinho mais próximo
            melhor_vizinho = None
            melhor_distancia = float('inf')
            
            for proximo in nao_visitados:
                dist, _ = self.dijkstra(atual, proximo)
                if dist is not None and dist < melhor_distancia:
                    melhor_distancia = dist
                    melhor_vizinho = proximo
            
            if melhor_vizinho is None:
                break
            
            rota.append(melhor_vizinho)
            custo_total += melhor_distancia
            nao_visitados.remove(melhor_vizinho)
        
        # Retornar ao ponto de origem
        dist_retorno, _ = self.dijkstra(rota[-1], origem)
        if dist_retorno is not None:
            custo_total += dist_retorno
            rota.append(origem)
        
        return custo_total, rota
    
    def ford_fulkerson(self, origem, destino):
        """
        Algoritmo de Ford-Fulkerson para encontrar o fluxo máximo.
        
        Retorna: fluxo_máximo
        """
        if origem not in self.vertices or destino not in self.vertices:
            return 0
        
        # Criar grafo residual
        grafo_residual = defaultdict(lambda: defaultdict(int))
        for u in self.arestas:
            for v, capacidade in self.arestas[u]:
                grafo_residual[u][v] += capacidade
        
        def bfs_caminho(s, t):
            """BFS para encontrar caminho aumentante."""
            visitados = {s}
            fila = deque([(s, [s])])
            
            while fila:
                u, caminho = fila.popleft()
                
                for v in grafo_residual[u]:
                    if v not in visitados and grafo_residual[u][v] > 0:
                        novo_caminho = caminho + [v]
                        if v == t:
                            return novo_caminho
                        visitados.add(v)
                        fila.append((v, novo_caminho))
            
            return None
        
        fluxo_maximo = 0
        
        while True:
            caminho = bfs_caminho(origem, destino)
            if caminho is None:
                break
            
            # Encontrar a capacidade mínima no caminho
            fluxo_caminho = float('inf')
            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i + 1]
                fluxo_caminho = min(fluxo_caminho, grafo_residual[u][v])
            
            # Atualizar capacidades residuais
            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i + 1]
                grafo_residual[u][v] -= fluxo_caminho
                grafo_residual[v][u] += fluxo_caminho
            
            fluxo_maximo += fluxo_caminho
        
        return fluxo_maximo
    
    def verificar_conexidade(self):
        """Verifica se o grafo é conexo (considerando o grafo não orientado subjacente)."""
        if not self.vertices:
            return True
        
        # Criar lista de adjacência não orientada para teste de conexidade
        adj_nao_orientada = defaultdict(set)
        for u in self.vertices:
            for v, _ in self.arestas[u]:
                adj_nao_orientada[u].add(v)
                adj_nao_orientada[v].add(u)
        
        inicio = next(iter(self.vertices))
        visitados = {inicio}
        fila = deque([inicio])
        
        while fila:
            u = fila.popleft()
            for v in adj_nao_orientada[u]:
                if v not in visitados:
                    visitados.add(v)
                    fila.append(v)
        
        return len(visitados) == len(self.vertices)

    def verificar_euleriano(self):
        """
        Verifica se o grafo é Euleriano, Semi-Euleriano ou não Euleriano.
        Baseado no grau dos vértices (grafo não orientado subjacente).
        """
        if not self.verificar_conexidade():
            return "Não Euleriano (Grafo Desconexo)"
        
        # Calcular graus no grafo não orientado subjacente
        graus = defaultdict(int)
        for u in self.vertices:
            for v, _ in self.arestas[u]:
                graus[u] += 1
                graus[v] += 1
        
        impares = 0
        for v in self.vertices:
            if graus[v] % 2 != 0:
                impares += 1
        
        if impares == 0:
            return "Euleriano (Possui Ciclo Euleriano)"
        elif impares == 2:
            return "Semi-Euleriano (Possui Caminho Euleriano)"
        else:
            return f"Não Euleriano ({impares} vértices de grau ímpar)"

    def coloracao_vertices(self):
        """
        Algoritmo de coloração sequencial (heurística).
        Retorna: (número_cromático, dicionário_de_cores)
        """
        if not self.vertices:
            return 0, {}
            
        # Ordenar vértices pelo grau (heurística de maior grau primeiro)
        adj_nao_orientada = defaultdict(set)
        for u in self.vertices:
            for v, _ in self.arestas[u]:
                adj_nao_orientada[u].add(v)
                adj_nao_orientada[v].add(u)
                
        vertices_ordenados = sorted(list(self.vertices), 
                                   key=lambda v: len(adj_nao_orientada[v]), 
                                   reverse=True)
        
        resultado = {}
        
        for u in vertices_ordenados:
            cores_vizinhos = {resultado[v] for v in adj_nao_orientada[u] if v in resultado}
            
            cor = 1
            while cor in cores_vizinhos:
                cor += 1
            
            resultado[u] = cor
            
        num_cromatico = max(resultado.values()) if resultado else 0
        return num_cromatico, resultado

    def obter_estatisticas(self):
        """Retorna estatísticas do grafo."""
        num_vertices = len(self.vertices)
        num_arestas = sum(len(adj) for adj in self.arestas.values())
        
        # Calcular graus (orientado)
        graus_saida = {v: len(self.arestas[v]) for v in self.vertices}
        graus_entrada = defaultdict(int)
        for u in self.arestas:
            for v, _ in self.arestas[u]:
                graus_entrada[v] += 1
        
        grau_max_saida = max(graus_saida.values()) if graus_saida else 0
        grau_max_entrada = max(graus_entrada.values()) if graus_entrada else 0
        
        return {
            'num_vertices': num_vertices,
            'num_arestas': num_arestas,
            'grau_medio': num_arestas / num_vertices if num_vertices > 0 else 0,
            'grau_max_saida': grau_max_saida,
            'grau_max_entrada': grau_max_entrada,
            'conexo': self.verificar_conexidade(),
            'euleriano': self.verificar_euleriano()
        }
    
    def listar_vertices(self):
        """Lista todos os vértices do grafo."""
        return sorted(list(self.vertices))


def exibir_menu():
    """Exibe o menu principal da aplicação."""
    print("\n" + "="*60)
    print("APLICAÇÃO DE OTIMIZAÇÃO LOGÍSTICA DE ENTREGA")
    print("Teoria dos Grafos - Universidade Presbiteriana Mackenzie")
    print("="*60)
    print("\n1. Carregar grafo do arquivo")
    print("2. Exibir estatísticas e Análise Estrutural")
    print("3. Encontrar caminho mínimo (Dijkstra)")
    print("4. Otimizar rota de entrega (Vizinho Mais Próximo)")
    print("5. Calcular fluxo máximo (Ford-Fulkerson)")
    print("6. Realizar Coloração de Vértices")
    print("7. Listar todos os vértices")
    print("8. Sair")
    print("-"*60)


def main():
    """Função principal da aplicação."""
    grafo = GrafoEntrega()
    carregado = False
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            nome_arquivo = input("Digite o nome do arquivo (padrão: grafo.txt): ").strip()
            if not nome_arquivo:
                nome_arquivo = "grafo.txt"
            carregado = grafo.carregar_de_arquivo(nome_arquivo)
        
        elif opcao == '2':
            if not carregado:
                print("✗ Erro: Grafo não carregado. Carregue o grafo primeiro (opção 1).")
            else:
                stats = grafo.obter_estatisticas()
                print("\n" + "="*60)
                print("ESTATÍSTICAS E ANÁLISE ESTRUTURAL")
                print("="*60)
                print(f"Número de vértices: {stats['num_vertices']}")
                print(f"Número de arestas: {stats['num_arestas']}")
                print(f"Grau médio: {stats['grau_medio']:.2f}")
                print(f"Grau máximo de saída: {stats['grau_max_saida']}")
                print(f"Grau máximo de entrada: {stats['grau_max_entrada']}")
                print(f"Grafo Conexo: {'Sim' if stats['conexo'] else 'Não'}")
                print(f"Classificação Euleriana: {stats['euleriano']}")
                print("="*60)
        
        elif opcao == '3':
            if not carregado:
                print("✗ Erro: Grafo não carregado. Carregue o grafo primeiro (opção 1).")
            else:
                origem = input("Digite o vértice de origem: ").strip()
                destino = input("Digite o vértice de destino: ").strip()
                
                distancia, caminho = grafo.dijkstra(origem, destino)
                
                if caminho:
                    print("\n" + "="*60)
                    print("CAMINHO MÍNIMO (ALGORITMO DE DIJKSTRA)")
                    print("="*60)
                    print(f"Origem: {origem}")
                    print(f"Destino: {destino}")
                    print(f"Distância mínima: {distancia}")
                    print(f"Caminho: {' → '.join(caminho)}")
                    print("="*60)
                else:
                    print("✗ Erro: Não há caminho entre os vértices especificados.")
        
        elif opcao == '4':
            if not carregado:
                print("✗ Erro: Grafo não carregado. Carregue o grafo primeiro (opção 1).")
            else:
                origem = input("Digite o ponto de origem (depósito): ").strip()
                pontos_str = input("Digite os pontos a visitar (separados por vírgula): ").strip()
                pontos = [p.strip() for p in pontos_str.split(',')]
                
                custo, rota = grafo.vizinho_mais_proximo(origem, pontos)
                
                if rota:
                    print("\n" + "="*60)
                    print("ROTA OTIMIZADA (VIZINHO MAIS PRÓXIMO)")
                    print("="*60)
                    print(f"Ponto de origem: {origem}")
                    print(f"Custo total da rota: {custo}")
                    print(f"Rota: {' → '.join(rota)}")
                    print("="*60)
                else:
                    print("✗ Erro: Não foi possível construir a rota.")
        
        elif opcao == '5':
            if not carregado:
                print("✗ Erro: Grafo não carregado. Carregue o grafo primeiro (opção 1).")
            else:
                origem = input("Digite o vértice de origem (fonte): ").strip()
                destino = input("Digite o vértice de destino (sumidouro): ").strip()
                
                fluxo = grafo.ford_fulkerson(origem, destino)
                
                print("\n" + "="*60)
                print("FLUXO MÁXIMO (ALGORITMO DE FORD-FULKERSON)")
                print("="*60)
                print(f"Origem (fonte): {origem}")
                print(f"Destino (sumidouro): {destino}")
                print(f"Fluxo máximo: {fluxo}")
                print("="*60)
        
        elif opcao == '6':
            if not carregado:
                print("✗ Erro: Grafo não carregado. Carregue o grafo primeiro (opção 1).")
            else:
                num_cromatico, cores = grafo.coloracao_vertices()
                print("\n" + "="*60)
                print("COLORAÇÃO DE VÉRTICES (HEURÍSTICA SEQUENCIAL)")
                print("="*60)
                print(f"Número Cromático Estimado (X(G)): {num_cromatico}")
                print("\nPartições de Cores (Amostra):")
                # Agrupar por cor para mostrar partições
                particoes = defaultdict(list)
                for v, cor in cores.items():
                    particoes[cor].append(v)
                
                for cor in sorted(particoes.keys()):
                    membros = particoes[cor]
                    print(f"Cor {cor}: {len(membros)} vértices ({', '.join(membros[:3])}...)")
                print("="*60)

        elif opcao == '7':
            if not carregado:
                print("✗ Erro: Grafo não carregado. Carregue o grafo primeiro (opção 1).")
            else:
                vertices = grafo.listar_vertices()
                print("\n" + "="*60)
                print("LISTA DE VÉRTICES DO GRAFO")
                print("="*60)
                print(f"Total: {len(vertices)} vértices\n")
                for i, v in enumerate(vertices, 1):
                    print(f"{i:3d}. {v}")
                print("="*60)
        
        elif opcao == '8':
            print("\nEncerrando a aplicação. Até logo!")
            sys.exit(0)
        
        else:
            print("✗ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
