'''
Final work of LFA

Members:
    Santiago Cardoso
    Lucas Gabriel
'''

veiculos = [
    """
    ____/   ___
   |_   \__'  _\\
   `-(*)----(*)'
    """,

    """
       ____
    __/___/______
   |_ \\__'   \\"_"\\
   `())--,())'-,,'
    """,

    """
        ____
      _/____]__
     |_v'_]"__"]
     `UJ-uJ--uJ

    """,

    """
        ____
      _/____)__
     |_v'_)"__")
     `UJ-uJ--uJ
    """,

    """
       _____
      i_____i
      ["___"]
      |J---L|
    """,

    """
      .(___).
     (O\_!_/O)
    """
]

class Fornecedora:
    def __init__(self):
        self.estoque = {
            1: {"tipo": "pneus", "quantidade": 800},
            2: {"tipo": "portas", "quantidade": 1000},
            3: {"tipo": "chassi", "quantidade": 2000},
            4: {"tipo": "bancos", "quantidade": 3000},
            5: {"tipo": "motores", "quantidade": 200},
            6: {"tipo": "baterias", "quantidade": 300},
            7: {"tipo": "freios", "quantidade": 500},
            8: {"tipo": "suspensoes", "quantidade": 700},
            9: {"tipo": "vidros", "quantidade": 3000},
            10: {"tipo": "portas", "quantidade": 200},
            11: {"tipo": "chassi", "quantidade": 500},
            12: {"tipo": "parafusos", "quantidade": 9000},
            13: {"tipo": "ar_condicionado", "quantidade": 10},
            14: {"tipo": "tapetes", "quantidade": 300},
            15: {"tipo": "farois", "quantidade": 200},
            16: {"tipo": "retrovisor", "quantidade": 100},
        }

    def enviar_pecas(self, tipo, quantidade):
        if tipo in self.estoque and self.estoque[tipo]["quantidade"] >= quantidade:
            self.estoque[tipo]["quantidade"] -= quantidade
            return quantidade
        else:
            return 0

    def to_string(self):
        print("Restam na fornecedora:")
        for elemento in self.estoque:
            print(f"\t{self.estoque[elemento]['quantidade']} {self.estoque[elemento]['tipo']}")
        print('\n')


class Carro:
    # TIPOS = Sedan, Hatch, SUV, Minivan, Fusca
    # MODELO A = direcao eletrica + automatico + 4 portas + ar condicionado
    # MODELO B = direcao eletrica + manual + 4 portas + ar condicionado
    # MODELO C = direcao hidraulica + manual + 2 portas + ventilacao
    # MODELO D = direcao mecanica + manual + 4 portas + ventilacao
    
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo
        self.completado = False
        self.direcao = "eletrica"
        self.cambio = "automatico"
        self.qtd_portas = 4
        self.ar = "ar condicionado"
        
        if modelo == "MODELO B":
            self.cambio = "manual"
            
        elif modelo == "MODELO C":
            self.direcao = "hidraulica"
            self.cambio = "manual"
            self.qtd_portas = 2
            self.ar = "ventilacao"
            
        elif modelo == "MODELO D":
            self.direcao = "mecanica"
            self.cambio = "manual"
            self.ar = "ventilacao"
            
    def to_string(self):
        return f"{self.tipo}, direcao {self.direcao}, {self.cambio}, {self.qtd_portas} portas, {self.ar}"


class LinhaProducao:
    def __init__(self):
        self.pilha_carros = []
        self.estoque_de_pneus = 400
        self.estoque_de_rodas = 400
        self.estoque_latarias = 200
        self.estoque_bancos = 3000
        self.motores = 3
        self.baterias = 300
        self.freios = 500
        self.suspensoes = 700
        self.estoque_de_vidros = 1000
        self.estoque_portas = 500
        self.estoque_chassi = 1000
        self.estoque_parafusos = 10000  # Um carro tem em média 1500 parafusos
        self.estoque_ar_condicionado = 30
        self.estoque_tapetes = 400
        self.estoque_farois = 400
        self.retrovisor = 200

    def obter_valores(self):
        atributos = vars(self)  # Obtém todos os atributos da instância
        valores = [atributos[attr] for attr in atributos if not attr.startswith('__') and not callable(getattr(self, attr))]
        return valores

    def produzir_carros_aleatorios_diarios(self, quantidade):
        tipos_carros = ["Sedan", "SUV", "Hatch", "Minivan", "Fusca"]
        modelos = ["MODELO A", "MODELO B", "MODELO C", "MODELO D"]

        for _ in range(quantidade):
            carro_aleatorio = random.choice(tipos_carros)
            modelo_aleatorio = random.choice(modelos)
            self.produzir_carro(carro_aleatorio, modelo_aleatorio)

    def produzir_carro(self, tipo, modelo):
        carro = Carro(tipo, modelo)
        self.pilha_carros.append(carro)
        self.executar_producao(carro)

    def corrigir_atributos(self):
        atributos = vars(self)
        for attr in atributos:
            if not attr.startswith('__') and not callable(getattr(self, attr)):
                if atributos[attr] == -1:
                    setattr(self, attr, 0)

    def executar_producao(self, carro):
        # Simulação das etapas de produção
        self.estoque_chassi -= 1
        self.estoque_parafusos -= 200

        self.estoque_de_rodas -= 4
        self.estoque_parafusos -= 100
        
        self.estoque_de_pneus -= 4
        
        self.motores -= 1
        self.estoque_parafusos -= 100

        self.baterias -= 1
        self.estoque_parafusos -= 100

        self.freios -= 4
        self.estoque_parafusos -= 100

        self.suspensoes -= 4
        self.estoque_parafusos -= 100
        
        self.estoque_latarias -= 1
        self.estoque_parafusos -= 200

        self.estoque_bancos -= 5
        self.estoque_parafusos -= 100
        
        self.estoque_de_vidros -= 6
        self.estoque_parafusos -= 100

        self.estoque_portas -= 4
        self.estoque_parafusos -= 100
        
        if carro.ar == "ar condicionado":
            self.estoque_ar_condicionado -= 1
            self.estoque_parafusos -= 100
        
        self.estoque_tapetes -= 4

        self.estoque_farois -= 4
        self.estoque_parafusos -= 100

        self.retrovisor -= 3
        self.estoque_parafusos -= 100
        
        # implementar as transições de estado
        # e manipulação da pilha para produzir o carro

        lista = self.obter_valores()
        print(f"\n\n{lista}\n\n")
        if -1 in lista:
            carro.completado = False
            self.corrigir_atributos()
        

        else:
            carro.completado = True  # Simulação de finalização

    def get_carros_finalizados(self):
        carros_finalizados = [carro for carro in self.pilha_carros if carro.completado]
        return carros_finalizados

    def relatorio_diario(self):
        carros_finalizados = [carro for carro in self.pilha_carros if carro.completado]
        carros_em_producao = [carro for carro in self.pilha_carros if not carro.completado]

        Sedan = [carro for carro in carros_finalizados if carro.tipo == "Sedan"]
        Hatch = [carro for carro in carros_finalizados if carro.tipo == "Hatch"]
        SUV = [carro for carro in carros_finalizados if carro.tipo == "SUV"]
        Minivan = [carro for carro in carros_finalizados if carro.tipo == "Minivan"]
        Fusca = [carro for carro in carros_finalizados if carro.tipo == "Fusca"]
        
        relatorio = f"Relatório Diário:\n"
        relatorio += "----------------------------------------\n"
        relatorio += f"Carros Finalizados: {len(carros_finalizados)}\n"
        relatorio += "Detalhes:\n\n"
        
        relatorio += "Sedan:\n"
        for carro in Sedan:
            relatorio += f"{carro.to_string()}\n"
        
        relatorio += "\nHatch:\n"
        for carro in Hatch:
            relatorio += f"{carro.to_string()}\n"
        
        relatorio += "\nSUV:\n"
        for carro in SUV:
            relatorio += f"{carro.to_string()}\n"

        relatorio += "\nMinivan:\n"
        for carro in Minivan:
            relatorio += f"{carro.to_string()}\n"

        relatorio += f"\nCarros em Produção: {len(carros_em_producao)}\n"
        relatorio += "Detalhes:\n"
        for carro in carros_em_producao:
            relatorio += f"- Tipo: {carro.tipo}, Modelo: {carro.modelo} - Em produção\n"
        
        relatorio += "-----------------------------------------\n"

        return relatorio


# Inicialização do simulador, defina os seguintes critérios:
quantidade_dias_simulacao = 5 # Número de dias que a simulação leva
quantidade_carros = 10 # Número de carros que a fábrica deve montar

linha = LinhaProducao()
fornecedora = Fornecedora()

'''
# Simulação de produção de carros
for dia in range(quantidade_dias_simulacao):
    linha.produzir_carros_aleatorios(quantidade_carros) # defina quantos carros podem ser produzidos diariamente

    # Gerar relatório diário
    print(f"\nRelatório Diário - Dia {dia + 1}:\n")
    print(linha.relatorio_diario())
'''

# Simulação de produção de carros
linha.produzir_carro("Sedan", "MODELO A")
linha.produzir_carro("SUV", "MODELO B")
linha.produzir_carro("Hatch", "MODELO C")
linha.produzir_carro("Minivan", "MODELO C")
linha.produzir_carro("Fusca", "MODELO C")

# Gerar relatório diário
print(linha.relatorio_diario())

carros_finalizados = linha.get_carros_finalizados()
for carros_finalizados in veiculos:
    print(veiculo)

dia += 1
