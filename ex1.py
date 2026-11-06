#Lista de Adjacência


import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criarGrafo():
    return {}



def imprimirGrafo(grafo):
    print("-" * 40)
    for vertice in grafo:
        print(vertice, ": ", grafo[vertice])
    print("-" * 40)



def inserirVertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def inserirArestaDirecionada(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        grafo[origem].append(destino)
    else:
        print("Um ou ambos os vértices não existem")



def inserirArestaNaoDirecionada(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        grafo[origem].append(destino)
        grafo[destino].append(origem)
    else:
        print("Um ou ambos os vértices não existem")



def removerVertice(grafo, vertice):
    if vertice in grafo:
        for v in grafo:
            while vertice in grafo[v]:
                grafo[v].remove(vertice)

        del grafo[vertice]
    else:
        print(f"O vértice {vertice} não existe")


def removerArestaDirecionada(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        while destino in grafo[origem]:
            grafo[origem].remove(destino)
    else:
        print("Um ou ambos os vértices não existem")



def removerArestaNaoDirecionada(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        while destino in grafo[origem]:
            grafo[origem].remove(destino)

        while origem in grafo[destino]:
            grafo[destino].remove(origem)
    else:
        print("Um ou ambos os vértices não existem")



def calcularGrauVerticeNaoDirecionado(grafo):
    print("=" * 40)
    print("Lista de graus de cada vértice:")
    print("=" * 40)

    for v in grafo:
        grau = len(grafo[v])
        print(f"{v}: {grau}")


def calcularGrauVerticeDirecionado(grafo):
    print("=" * 40)
    print("Lista de graus de cada vértice:")
    print("=" * 40)

    for v in grafo:
        entrada = 0
        saida = len(grafo[v])

        for vertice in grafo:
            if v in grafo[vertice]:
                entrada += grafo[vertice].count(v)

        print(f"{v}")
        print(f"Entrada: {entrada}")
        print(f"Saída: {saida}")
        print(f"Total: {entrada + saida}")
        print("-" * 20)


def verificaArestaExistente(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        if destino in grafo[origem]:
            return True

    return False


def listarVizinhosVertice(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos de {vertice}:")

        for v in grafo[vertice]:
            print(f" - {v}")
    else:
        print("O vértice não existe")



def verificarPercurso(grafo, percurso):
    if not percurso:
        print("Nenhum percurso informado")
        return False

    for vertice in percurso:
        if vertice not in grafo:
            print("Existem vértices que não existem no grafo")
            return False

    for i in range(len(percurso) - 1):
        origem = percurso[i]
        destino = percurso[i + 1]

        if not verificaArestaExistente(grafo, origem, destino):
            return False

    return True


def menu():
    grafo = criarGrafo()

    while True:
        print("=" * 40)
        print("Qual o tipo de Grafo que você deseja?")
        print("0 - Sair")
        print("1 - Direcionado")
        print("2 - Não Direcionado")
        print("=" * 40)

        op = input("Digite uma opção: ")

        if op == "0":
            print("Sistema finalizado")
            return

        elif op == "1":
            direcionado = True
            break

        elif op == "2":
            direcionado = False
            break

        else:
            limpar_tela()
            print("Opção inválida, tente novamente")


    while True:
        print("=" * 40)
        print(" " * 15, "Menu")
        print("=" * 40)
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

        if opcao == "0":
            print("Sistema de grafos finalizado...")
            break

        elif opcao == "1":
            imprimirGrafo(grafo)

        elif opcao == "2":
            vertice = input("Vértice a ser inserido: ").upper()
            inserirVertice(grafo, vertice)
            imprimirGrafo(grafo)

        elif opcao == "3":
            origem = input("Vértice Origem da aresta: ").upper()
            destino = input("Vértice Destino da aresta: ").upper()

            if direcionado:
                inserirArestaDirecionada(grafo, origem, destino)
            else:
                inserirArestaNaoDirecionada(grafo, origem, destino)

            imprimirGrafo(grafo)

        elif opcao == "4":
            vertice = input("Vértice a ser removido: ").upper()
            removerVertice(grafo, vertice)
            imprimirGrafo(grafo)

        elif opcao == "5":
            origem = input("Vértice Origem da aresta: ").upper()
            destino = input("Vértice Destino da aresta: ").upper()

            if direcionado:
                removerArestaDirecionada(grafo, origem, destino)
            else:
                removerArestaNaoDirecionada(grafo, origem, destino)

            imprimirGrafo(grafo)

        elif opcao == "6":
            if direcionado:
                calcularGrauVerticeDirecionado(grafo)
            else:
                calcularGrauVerticeNaoDirecionado(grafo)

        elif opcao == "7":
            origem = input("Vértice Origem da aresta: ").upper()
            destino = input("Vértice Destino da aresta: ").upper()

            existente = verificaArestaExistente(grafo, origem, destino)

            if existente:
                print(f"{origem} -> {destino} existe")
            else:
                print(f"{origem} -> {destino} NÃO existe")

        elif opcao == "8":
            vertice = input("Vértice a ser consultado: ").upper()
            listarVizinhosVertice(grafo, vertice)

        elif opcao == "9":
            print("Exemplo de percurso: A B C")

            percurso = input(
                "Digite o percurso separando os vértices por espaço: "
            ).upper().split()

            print(" -> ".join(percurso))

            resultado = verificarPercurso(grafo, percurso)

            if resultado:
                print("Percurso EXISTE")
            else:
                print("Percurso NÃO existe")

        else:
            print("Opção inválida, tente novamente")


menu()
