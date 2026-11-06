import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criar grafo
def criarGrafo():
  return {
    "vertices" : [],
    "arestas": []
}

# Mostrar Grafo
def imprimirGrafo(grafo):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  print("Vértices: ")
  print(vertices)

  print("Arestas: ")
  for c in range(len(arestas)):
    origem = arestas[c][0]
    destino = arestas[c][1]

    if origem == destino:# para laços
      if arestas.index([origem, destino]) != c:#eu preciso que conte 2x o laço, mas não quero que ao inserir um laço ele apreça 2x na lista
        continue

    print(f"{origem} -> {destino}")

# Inserir vértices
def inserirVertice(grafo, vertice):
  if vertice not in grafo["vertices"]:
    grafo["vertices"].append(vertice)

# Remover vértices
def removerVertice(grafo, vertice):
  if vertice in grafo["vertices"]:
    vertices = grafo["vertices"]
    arestas = grafo["arestas"]

    vertices.remove(vertice)

    i = 0

    while i < len(arestas):
      if vertice in arestas[i]:
        arestas.pop(i)
      else:
        i += 1
        #só incremento quando não removo a aresta, pq a função pop depois de remover o valor de um índice reorganiza os valores
        #Dessa forma se eu retirar a aresta da posição 0, o valor de 1 será colocado em 0 e assim sucessivamente
        #o que faria eu não apagar essa aresta se ela tivesse o vértice que eu apaguei
        #remove faz da mesma forma, a diferença entre eles, é que o pop remove pelo índice e o remove pelo valor


# Inserir arestas
def inserirAresta(grafo, origem, destino, direcionado):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  #Se os vértices não existirem crio eles, não precisa de um if pois a função inserirVertice já verifica isso para mim
  inserirVertice(grafo, origem)
  inserirVertice(grafo, destino)

  arestas.append([origem, destino])#append recebe um argumento, nesse caso origem e destino
  if not direcionado:
    arestas.append([destino, origem])

  arestas.sort()#Para deixar organizada depois de uma nova inserção

# Remover arestas
def removerAresta(grafo, origem, destino, direcionado):
  arestas = grafo["arestas"]

  if [origem, destino] in arestas:
    arestas.remove([origem, destino])

  if not direcionado and [destino, origem] in arestas:
    arestas.remove([destino, origem])

# Grau direcionado
def calcularGrauVerticeDirecionado(grafo):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  for i in range(len(vertices)):#esse loop serve para percorrer todos os vértices
    grauEntrada = 0
    grauSaida = 0
    for j in range(len(arestas)):#esse loop serve paara percorrer todas as arestas
      if vertices[i] == arestas[j][1]:#verifico se o vértice atual está na entrada,  a entrada é depois da flecha ex: A -> B, a entrada é B, esse 1 representa a posição 1 dentro da tupla ["A", "B"]
        grauEntrada += 1                                                                                                                                                                #[ 0 ,  1 ]
      if vertices[i] == arestas[j][0]:#verifico se o vértice atual está na saída  a saída é antes da flecha ex: A -> B, saída é A, esse 0 representa a posição 0 dentro da tupla ["A", "B"]
        grauSaida += 1                                                                                                                                                          #[ 0 ,  1 ]

    print(f"{vertices[i]}")
    print(f"Entrada: {grauEntrada}")
    print(f"Saída: {grauSaida}")
    print(f"Total: {grauEntrada + grauSaida}")

# Grau NÂO direcionado
def calcularGrauVerticeNaoDirecionado(grafo):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  for i in range(len(vertices)):#esse loop serve para percorrer todos os vértices
    grau = 0
    for j in range(len(arestas)):#esse loop serve paara percorrer todas as arestas
      if vertices[i] == arestas[j][0]:
        grau += 1

    print(f"{vertices[i]} = {grau}")

# Verificar aresta existe
def verificaArestaExistente(grafo, origem, destino):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  if origem not in vertices or destino not in vertices:
    print("1 ou ambos os vértices não existem, tente novamente")
    return False

  if [origem, destino] in arestas:
    return True
  else:
    return False

# Listar todos os Vizinhos de um vértice
def listarVizinhosVertice(grafo, vertice):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]
  vizinhos = []

  if vertice not in vertices:
    print(f"{vertice} NÂO existe")
    return

  for j in range(len(arestas)):#esse loop serve paara percorrer todas as arestas
    if vertice == arestas[j][0]:
      if arestas[j][1] not in vizinhos:# para evitar repetir o mesmo vizinho caso haja laços
        vizinhos.append(arestas[j][1]) #[ 0 ,  1 ]

  for vizinho in vizinhos:
    print(f"- {vizinho}")


# Verificar se percurso é possível
def verificarPercurso(grafo, percurso):
  vertices = grafo["vertices"]

  if not percurso:
    print("Nenhum vértice informado")
    return False

  for vertice in percurso:
    if vertice not in vertices:
      print(f"O vértice {vertice} Nâo existe")
      return False

  print(percurso)

  for i in range(len(percurso) - 1):
    origem = percurso[i]
    destino = percurso[i + 1]

    if not verificaArestaExistente(grafo, origem, destino):
      print("Percurso Inválido")
      return False

  print("Percurso válido")
  return True

#Menu do programa
def menu():
  grafo = criarGrafo()

  while True:
    print("="*40)
    print("Qual o tipo de Grafo que você deseja?")
    print("0 - Sair")
    print("1 - Direcionado")
    print("2 - Não Direcionado")
    print("="*40)
    op = input()
    match op:
      case "0":
        print("Sistema Finalizado")
        return
      case "1":
        direcionado = True
        break
      case "2":
        direcionado = False
        break
      case _:
        limpar_tela();
        print("Opção inválida, tente novamente")

  while True:
    print("="*40)
    print(" "*15, "Menu")
    print("="*40)
    print("0 - Sair")
    print("1 - Mostrar o Grafo")
    print("2 - Inserir Vértice")
    print("3 - Inserir Aresta")
    print("4 - Remover Vértice")
    print("5 - Remover Aresta")
    print("6 - Exibir grau de cada vértice")
    print("7 - Verificar aresta existente")
    print("8 - Listar todos os vizinhos de um vértice")
    print("9 - Verificar percurso")

    opcao = input("Digite uma opção: ")

    match opcao:
      case "0":
        print("Sistema de grafos finalizado...")
        break
      case "1":
        imprimirGrafo(grafo)#Como foi criada uma função pra deixar mais bonitinho a apresentação do grafo é melhor usar essa função do que só chamar o grafo
      case "2":
        vertice = input("Vértice a ser inserido: ").upper()
        inserirVertice(grafo, vertice)
        imprimirGrafo(grafo)
      case "3":
        origem = input("Vértice Origem da aresta: ").upper()
        destino = input("Vértice Destino da aresta: ").upper()
        inserirAresta(grafo, origem, destino, direcionado)
        imprimirGrafo(grafo)
      case "4":
        vertice = input("Vértice a ser removido: ").upper()
        removerVertice(grafo, vertice)
        imprimirGrafo(grafo)
      case "5":
        origem = input("Vértice Origem da aresta: ").upper()
        destino = input("Vértice Destino da aresta: ").upper()
        removerAresta(grafo, origem, destino, direcionado)
        imprimirGrafo(grafo)
      case "6":
        if direcionado:
          calcularGrauVerticeDirecionado(grafo)
        else:
          calcularGrauVerticeNaoDirecionado(grafo)
      case "7":
        origem = input("Vértice Origem da aresta: ").upper()
        destino = input("Vértice Destino da aresta: ").upper()
        existente = verificaArestaExistente(grafo, origem, destino)
        if existente:
          print(f"{origem} -> {destino} existe")
        else:
          print(f"{origem} -> {destino} NÂO existe")
      case "8":
        vertice = input("Vértice a ser consultado: ").upper()
        listarVizinhosVertice(grafo, vertice)
      case "9":
        print("Exemplo de percurso: a b c")
        print("Exemplo de percurso: A b C")
        percurso = input("Digite o percurso desejado separando cada vértice por espaço: ").upper().split()
        print(" -> ".join(percurso))
        resultado = verificarPercurso(grafo, percurso)
        if resultado:
          print("Percurso EXISTE")
        else:
          print("Percurso NÂO existe")
      case _:
        limpar_tela();
        print("Opção inválida, tente novamente")

menu()
