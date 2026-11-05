#%%writefile listaAresta.py
#Se executar no VSCode apagar/comentar a linha acima, pois ela só serve no google collab

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Para testes rápidos, descomente esse grafo abaixo
grafo = {
    "vertices": ["A", "B", "C", "D"],
    "arestas": [
        ("A", "B"),
        ("B", "C"),
        ("B", "D"),
        ("C", "A"),
        ("D", "C")
    ]
}

# print(grafo)

# Criar grafo
# grafo = {
#     "vertices" : {},
#     "arestas": {}
# }

# Mostrar Grafo
def imprimirGrafo(grafo):
  arestas = grafo["arestas"]

  for c in range(len(arestas)):
    origem = arestas[c][0]
    destino = arestas[c][1]

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
def inserirAresta(grafo, origem, destino):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  if origem in vertices and destino in vertices:
    arestas.append((origem, destino))#o método apend só recebe um argumento, por isso para mandar a tupla é necessário colocar eles entre ( )
    arestas.sort()#Para deixar organizada depois de uma nova inserção

# Remover arestas
def removerAresta(grafo, origem, destino):
  arestas = grafo["arestas"]

  if (origem, destino) in arestas:#tem que ser entre () visto que estamos trabalhando com tuplas
    arestas.remove((origem, destino))

# Grau direcionado
def calcularGrauVerticeDirecionado(grafo):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  for i in range(len(vertices)):#esse loop serve para percorrer todos os vértices
    grauEntrada = 0
    grauSaida = 0
    for j in range(len(arestas)):#esse loop serve paara percorrer todas as arestas
      if vertices[i] == arestas[j][1]:#verifico se o vértice atual está na entrada,  a entrada é depois da flecha ex: A -> B, a entrada é B, esse 1 representa a posição 1 dentro da tupla ("A", "B")
        grauEntrada += 1                                                                                                                                                                #( 0 ,  1 )
      if vertices[i] == arestas[j][0]:#verifico se o vértice atual está na saída  a saída é antes da flecha ex: A -> B, saída é A, esse 0 representa a posição 0 dentro da tupla ("A", "B")
        grauSaida += 1                                                                                                                                                          #( 0 ,  1 )

    print(f"{vertices[i]}")
    print(f"Entrada: {grauEntrada}")
    print(f"Saída: {grauSaida}")
    print(f"Total: {grauEntrada + grauSaida}")

# Grau NÂO direcionado
#dá pra fazer igual o direcionado, se direcionado só imprimir de forma separada os graus
#se não direcionado é só printar o total, é outra forma de fazer, porém só funciona em Lista de arestas, não daria para fazer isso em Matriz e lista de adjacência, pois seria contado 2x
def calcularGrauVerticeNaoDirecionado(grafo):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  for i in range(len(vertices)):#esse loop serve para percorrer todos os vértices
    grau = 0
    for j in range(len(arestas)):#esse loop serve paara percorrer todas as arestas
      if vertices[i] in arestas[j]:#verifico se o vértice atual aparece na aresta atual, não distinguindo se é de entrada ou saída, o in verifica se existe em qualquer posição, por isso não preciso verficar com == e verificar as posições, é mais fácil quando não é necessário especificar a posição e igualdade, apenas se existe em algum lugar dessa lista
        grau += 1
      if arestas[j][0] == arestas[j][1] and arestas[j][0] == vertices[i]:
        grau += 1

    print(f"{vertices[i]} = {grau}")

# Verificar aresta existe
def verificaArestaExistente(grafo, origem, destino, direcionado=True):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]

  if origem not in vertices or destino not in vertices:
    print("1 ou ambos os vértices não existem, tente novamente")
    return False

  #arestas contém tuplas e não índices individuais
  # indiceOrigem = arestas.index(origem)
  # indiceDestino = arestas.index(destino)

  if direcionado:
    if (origem, destino) in arestas:
      return True
    else:
      return False
  else:
    if (origem, destino) in arestas or (destino, origem) in arestas:
      return True
    else:
      return False

# Listar todos os Vizinhos de um vértice
def listarVizinhosVertice(grafo, vertice):
  vertices = grafo["vertices"]
  arestas = grafo["arestas"]
  vizinhos = []

  for j in range(len(arestas)):#esse loop serve paara percorrer todas as arestas
    if vertice == arestas[j][0]:
      if arestas[j][1] not in vizinhos:# para evitar repetir o mesmo vizinho caso haja laços
        vizinhos.append(arestas[j][1])

    elif vertice == arestas[j][1]:
      if arestas[j][0] not in vizinhos:
        vizinhos.append(arestas[j][0])                                                                                                                                               #( 0 ,  1 )

  for vizinho in vizinhos:
    print(f"- {vizinho}")


# Verificar se percurso é possível
def verificarPercurso(grafo, percurso, direcionado):
  if not percurso:
    print("Nenhum vértice informado")
    return False

  print(percurso)
  for i in range(len(percurso) - 1):
    origem = percurso[i]
    destino = percurso[i + 1]

    if not verificaArestaExistente(grafo, origem, destino, direcionado):
      print("Percurso Inválido")
      return False

  print("Percurso válido")
  return True

while True:
  print("1 - Inserir vértice")
  print("2 - Inserir aresta")
  print("3 - Remover vértice")
  print("4 - Remover aresta ")
  print("5 - Calcular e exibir o grau de cada vértice")
  print("6 - Listar vizinhos de um vértice")
  print("7 - Verificar percurso")
  print("0 - Sair")
  opcao = input("Digite a opção correspondente: ")
  limpar_tela()

  match opcao:
    case "1":
      vertice = input("Digite o vértice que deseja inserir: ")
      inserirVertice(grafo,vertice)
    case "2":
      origem = input("Digite o vértice de origem da aresta: ")
      destino = input("Digite o vértice de destino da aresta: ")
      inserirAresta(grafo,origem,destino)

    case "3":
      vertice = input("Digite o vértice que deseja remover: ")
      removerVertice(grafo,vertice)

    case "4":
      origem = input("Digite o vértice de origem da aresta: ")
      destino = input("Digite o vértice de destino da aresta: ")
      removerAresta(grafo,origem,destino)

    case "5":
      direcionado = input("O grafo é direcionado? (s/n): ").lower() == "s"
      if direcionado:
        calcularGrauVerticeDirecionado(grafo)
      else:
        calcularGrauVerticeNaoDirecionado(grafo)

    case "6":
      vertice = input("Digite o vértice que deseja listar os vizinhos: ")
      listarVizinhosVertice(grafo,vertice)

    case "7":
      percurso = input("Digite o percurso desejado, separando os vértices por vírgula: ").split(",")
      direcionado = input("O grafo é direcionado? (s/n): ").lower() == "s"
      verificarPercurso(grafo, percurso, direcionado)

    case "0":

      break


  print("Lista de arestas atual:")
  imprimirGrafo(grafo)