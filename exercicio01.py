class Cliente:
    def __init__(self, nome, endereco, contato):
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
class Vendedor:
    def __init__(self, nome, id, contato):
        self.nome = nome
        self.id = id
        self.contato = contato
class Contrato:
    def __init__(self, termos):
        self.termos = termos
class Venda:
    def __init__(self, cliente, vendedor, contrato, data, valor, status_pagamento):
        self.cliente = cliente
        self.vendedor = vendedor
        self.contrato = contrato
        self.data = data
        self.valor = valor
        self.status_pagamento = status_pagamento

    def calcularcomissao(self):
        if self.vendedor.id < 100:  
            return self.valor * 0.04
        else:
            return self.valor * 0.07 

class SistemaComissoes:
    def __init__(self):
        self.clientes = []
        self.vendedores = []
        self.contratos = []
        self.vendas = []

    def cadastrarcliente(self, nome, endereco, contato):
        cliente = Cliente(nome, endereco, contato)
        self.clientes.append(cliente)

    def cadastrarvendedor(self, nome, id, contato):
        vendedor = Vendedor(nome, id, contato)
        self.vendedores.append(vendedor)

    def cadastrarcontrato(self, termos):
        contrato = Contrato(termos)
        self.contratos.append(contrato)

    def cadastrarvenda(self, cliente, vendedor, contrato, data, valor, status_pagamento):
        venda = Venda(cliente, vendedor, contrato, data, valor, status_pagamento)
        self.vendas.append(venda)

    def gerarrelatorio(self):
        for venda in self.vendas:
            comissao = venda.calcularcomissao()
            print(f"Data: {venda.data}, cliente: {venda.cliente.nome}, vendedor: {venda.vendedor.nome}, valor: R${venda.valor}, comissão: R${comissao}")
sistema = SistemaComissoes()
cliente = Cliente("cliente a", "enderoço A", "ctt A")
sistema.clientes.append(cliente)
vendedor = Vendedor("vend 1", 1001, "ctt 1")
sistema.vendedores.append(vendedor)
contrato = Contrato(" contrato 1")
sistema.contratos.append(contrato)
venda = Venda(sistema.clientes[0], sistema.vendedores[0], sistema.contratos[0], "2023-09-01", 1000, "pago")
sistema.vendas.append(venda)
for venda in sistema.vendas:
    comissao = venda.calcularcomissao()
    print(f"data: {venda.data}, cliente: {venda.cliente.nome}, vendedor: {venda.vendedor.nome}, valor: R${venda.valor}, comissão: R${comissao}")
