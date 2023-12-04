'''
Final work of LFA

Members:
    Santiago Cardoso
    Lucas Gabriel
'''

import os
import random
import Linha_de_producao_de_veiculos as Linha

''' _.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~._ '''
#  Inicialização do simulador, defina os seguintes critérios:
quantidade_dias_simulacao = 4 #  Número de dias que a simulação leva
quantidade_carros = 5 #  Número de carros limite que a fábrica consegue produzir
''' _.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~._ '''

linha = Linha.LinhaProducao()

#  Pilha de dias
pilha_dias = ["D"] * quantidade_dias_simulacao

if os.path.exists("relatorio_diario.txt"): #  Deleta o arquivo anterior do relatório diário, caso ele exista
    os.remove("relatorio_diario.txt")

#  Simulação de produção de carros
while pilha_dias:
    #  Desempilhar um "D" para representar o dia que passa
    pilha_dias.pop()

    tipos_carros = ["Sedan", "SUV", "Hatch", "Minivan", "Fusca"]
    modelos = ["MODELO A", "MODELO B", "MODELO C", "MODELO D"]

    fita = []

    for _ in range(quantidade_carros):
        tipo_carro_aleatorio = random.choice(tipos_carros)
        modelo_aleatorio = random.choice(modelos)
        fita.append([tipo_carro_aleatorio, modelo_aleatorio])

    for element in fita:
        linha.produzir_carro(element[0], element[1])
    
    #  Gerar relatório diário
    linha.relatorio_diario()

    input("\nAperte ENTER para passar o dia...")
    os.system("cls")

    if not pilha_dias:
        print("Cronograma de montagens finalizado!\n")

        if (not linha.pilha_carros_em_producao):
            print("Fábrica conseguiu realizar todo o processo de montagem!")
        else:
            print("Fábrica não conseguiu atingir a cota de veículos montados nos dias!")

        input("Aperte ENTER para fechar a fábrica...")
        os.system("cls")
