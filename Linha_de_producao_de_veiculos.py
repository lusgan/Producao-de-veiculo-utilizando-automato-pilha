class Fornecedora:
    def __init__(self):
        self.estoque = {
            1: {"tipo": "pneus", "quantidade": 800},
            2: {"tipo": "vidros_porta", "quantidade": 200},
            3: {"tipo": "portas", "quantidade": 1000},
            4: {"tipo": "chassi", "quantidade": 2000}
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
            print(f"\t{self.estoque[elemento]["quantidade"]} {self.estoque[elemento]["tipo"]}")
        print('\n')




class Carro:
    #tipos = Sedan, hatch, SUV, minivan
    #modelo A = direcao eletrica + automatico + 4 portas + ar condicionado
    #modelo B = direcao eletrica + manual + 4 portas + ar condicionado
    #modelo C = direcao hidraulica + manual + 2 portas + ventilação
    #modelo D = direcao mecânica + manual + 4 portas + ventilacao
    
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo
        self.completado = False
        self.direcao = "eletrica"
        self.cambio = "automatico"
        self.qtd_portas = 4
        self.ar = "Ar condicionado"
        
        if(modelo == "modelo B"):
            self.cambio = "manual"
            
        elif modelo == "modelo C":
            self.direcao = "hidraulica"
            self.cambio = "manual"
            self.qtd_portas = 2
            self.ar = "ventilacao"
            
        elif modelo == "modelo D":
            self.direcao = "mecanica"
            self.cambio = "manual"
            self.ar = "ventilacao"
            
    def to_string(self):
        return f"{self.tipo}, direcao {self.direcao}, {self.cambio}, {self.qtd_portas} portas, {self.ar}"




class LinhaProducao:
    def __init__(self):
        self.pilha_carros = []
        self.estoque_de_pneus = 400
        self.estoque_de_vidros_porta = 100
        self.estoque_portas = 500
        self.estoque_chassi = 1000

    def produzir_carro(self, tipo, modelo):
        carro = Carro(tipo, modelo)
        self.pilha_carros.append(carro)
        self.executar_producao(carro)

    def executar_producao(self, carro):
        # Simulação das etapas de produção
        # Aqui você implementaria as transições de estado
        # e manipulação da pilha para produzir o carro

        carro.completado = True  # Simulação de finalização

    def relatorio_diario(self):
        carros_finalizados = [carro for carro in self.pilha_carros if carro.completado]
        carros_em_producao = [carro for carro in self.pilha_carros if not carro.completado]
        
        Sedan = [carro for carro in carros_finalizados if carro.tipo == "Sedan"]
        Hatch = [carro for carro in carros_finalizados if carro.tipo == "Hatch"]
        SUV = [carro for carro in carros_finalizados if carro.tipo == "SUV"]
        Minivan = [carro for carro in carros_finalizados if carro.tipo == "Minivan"]
        
        relatorio = f"Relatório Diário:\n"
        relatorio+="----------------------------------------\n"
        relatorio+= f"Carros Finalizados: {len(carros_finalizados)}\n"
        relatorio += "Detalhes:\n\n"
        
        relatorio+="Sedan:\n"
        for carro in Sedan:
            relatorio+= f"{carro.to_string()}\n"
        
        relatorio+="\nHatch:\n"
        for carro in Hatch:
            relatorio+= f"{carro.to_string()}\n"
        
        relatorio+="\nSUV:\n"
        for carro in SUV:
            relatorio+= f"{carro.to_string()}\n"

        relatorio+="\nMinivan:\n"
        for carro in Minivan:
            relatorio+= f"{carro.to_string()}\n"

        relatorio += f"\nCarros em Produção: {len(carros_em_producao)}\n"
        relatorio += "Detalhes:\n"
        for carro in carros_em_producao:
            relatorio += f"- Tipo: {carro.tipo}, Modelo: {carro.modelo} - Em produção\n"
        
        relatorio +="-----------------------------------------\n"

        return relatorio




# Exemplo de uso
dia = 0

linha = LinhaProducao()
fornecedora = Fornecedora()

a = fornecedora.enviar_pecas(1, 10)
print(a)
fornecedora.to_string()

# Simulação de produção de carros
linha.produzir_carro("Sedan", "modelo A")
linha.produzir_carro("SUV", "modelo B")
linha.produzir_carro("Hatch", "modelo C")

# Gerar relatório diário
print(linha.relatorio_diario())
dia += 1
