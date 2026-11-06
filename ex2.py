import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Cria um grafo vazio para ser alimentado pelas outras funções
def criarGrafo():
  return {
      "vertices": [],
      "matriz": []
  }

#Função para imprimir o grafo de forma mais estética, pulando linha e criando uma linha de separação antes e depois
def imprimirGrafo(grafo):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  print("   ", end="")#deixa um espacinho para a primeira célula

  for c in range(len(vertices)):
    print(vertices[c], end="  ")#coloco todos os vértices na horizontal

  print()

  for i in range(len(vertices)):
    print(vertices[i], end="  ")#coloco primeiro a letra do vértice

    for j in range(len(vertices)):
      print(matriz[i][j], end="  ")#aí coloco todos os valores daquela linha

    print()#Terminou a linha pulo uma linha e preencho a próxima com a letra da coluna e seus valores

#Inserir vértice
def inserirVertice(grafo, vertice):
  if vertice not in grafo["vertices"]:
    grafo["vertices"].append(vertice)#adiciono o vértice novo na lista de vértices

    #adiciono uma coluna
    for linha in grafo["matriz"]:
      linha.append(0)# coloco inicialmente como 0 já que não existem conexões quando o vértice é criado
      #percorro todas as linhas da matriz e no final de cada 1 eu adiciono um novo elemento com valor 0

    #adiciono uma linha
    tamanho = len(grafo["vertices"])#pego o tamanho da lista de vértices para depois no código abaixo possa preencher com 0 toda linha que se relacione com o novo vértice criado
    novaLinha = []
    for i in range(tamanho):
      novaLinha.append(0)
    grafo["matriz"].append(novaLinha)#preencho toda a linha do novo vértice com 0 pois não há conexões no momento de sua criacão

#Inserir Aresta em Direcionado e nÂO DIRECIONADO
def inserirAresta(grafo, origem, destino, direcionado):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  if origem not in grafo["vertices"]:
    inserirVertice(grafo, origem)

  if destino not in grafo["vertices"]:
    inserirVertice(grafo, destino)

  i = vertices.index(origem)
  j = vertices.index(destino)

  matriz[i][j] = 1

  if not direcionado: #se não for direcionado tbm coloca a aresta de forma recíproca, ex AB e BA se NÂO DIRECIONADO
    matriz[j][i] = 1

def removerVertice(grafo, vertice):
  if vertice not in grafo["vertices"]:
    print(f"O vértice {vertice} NÂO existe")
    return

  indice = grafo["vertices"].index(vertice)

  grafo["matriz"].pop(indice)
  for linha in grafo["matriz"]:
    linha.pop(indice)

  grafo["vertices"].pop(indice)

def removerAresta(grafo, origem, destino, direcionado):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  if origem not in vertices or destino not in vertices:
    print("Tente novamente, 1 ou ambos vértices não existem")
    return

  i = vertices.index(origem)
  j = vertices.index(destino)

  matriz[i][j] = 0 #direcionado tira só de 1, ex AB só tirar o 1 e pronto

  if not direcionado:
    matriz[j][i] = 0 #não direcionado, tem que tirar tanto de AB quanto de BA

def calcularGrauVerticeNaoDirecionado(grafo):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  for i in range(len(vertices)):
    grau = 0
    for j in range(len(vertices)):
      if matriz[i][j] == 1:
        grau += 1
    if matriz[i][i] == 1:
        grau += 1 #aqui se houver laços, tem que contar de novo, pq laços contam 2vezes

    print(f"{vertices[i]}: {grau}")

def calcularGrauVerticeDirecionado(grafo):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  for i in range(len(grafo["vertices"])):
    grauSaida = 0
    grauEntrada = 0
    for j in range(len(grafo["vertices"])):
      if matriz[i][j] == 1:
        grauSaida += 1
      if matriz[j][i] == 1:
        grauEntrada += 1

    print(f"{vertices[i]}")
    print(f"Saída: {grauSaida}")
    print(f"Entrada: {grauEntrada}")
    print(f"Total: {grauEntrada + grauSaida}")
    print()

def verificaArestaExistente(grafo, origem, destino):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  if origem not in vertices or destino not in vertices:
    print("Tente novamente, 1 ou ambos os vértices não existem")
    return False

  origemIndice = vertices.index(origem)
  destinoIndice = vertices.index(destino)

  if matriz[origemIndice][destinoIndice] == 1:
    return True
  else:
    return False

def listarVizinhosVertice(grafo, vertice):
  vertices = grafo["vertices"]
  matriz = grafo["matriz"]

  if vertice not in vertices:
    print("Tente novamente, 1 ou ambos os vértices não existem")
    return

  origemIndice = vertices.index(vertice)

  print(f"Vizinhos de {vertice}: ")

  for j in range(len(vertices)):
    if matriz[origemIndice][j] == 1:
      print(f" - {vertices[j]}")

def verificarPercurso(grafo, percurso):
  if not percurso:
    print("Nenhum percurso informado")
    return False

  for vertice in percurso:
    if vertice not in grafo["vertices"]:
      print("Existem vértices que não existem no grafo, confira novamente")
      return False

  for i in range(len(percurso) - 1):
    origem = percurso[i]
    destino = percurso[i + 1]

    if not verificaArestaExistente(grafo, origem, destino):
      return False

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
