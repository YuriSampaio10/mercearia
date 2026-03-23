from Models import *

# DAO CATEGORIA
class DaoCategoria:
    # salva no arquivo texto categoria txt
    @classmethod
    def salvar(cls, categoria):
        with open('txt/categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    # abre o arquivo texto da categoria.txt
    @classmethod
    def ler(cls):
        with open('txt/categoria.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.categoria = arq.readlines()
            
        # tira o \n
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat  

# DAO VENDA
class DaoVenda:
    # metodo salvar da DAO venda
    @classmethod
    def salvar(cls, venda: Venda):
        with open('txt/venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + ' | ' + venda.itensVendido.preco + ' | ' + venda.itensVendido.categoria + ' | ' + venda.vendedor + ' | ' + venda.comprador + ' | ' + str(venda.quantidadeVendida) + ' | ' + venda.data)
            arq.writelines('\n')


    # abre o arquivo texto da venda.txt
    @classmethod
    def ler(cls):
        with open('txt/venda.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.venda = arq.readlines()

        # tira o \n
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
       
        vend = []
        for i in cls.venda:
            produto = Produtos(i[0], i[1], i[2])
            venda = Venda(produto, i[3], i[4], i[5], i[6])
            vend.append(venda)
        return vend
    
# DAO ESTOQUE
class DaoEstoque:
    @classmethod
    def salvar(cls, estoque):
        with open('txt/estoque.txt', 'a') as arq:
            arq.writelines(estoque.produto.nome + ' | ' + estoque.produto.preco + ' | ' + estoque.produto.categoria + ' | ' + str(estoque.quantidade))
            arq.writelines('\n')

    
    # abre o arquivo texto da estoque.txt
    @classmethod
    def ler(cls):
        with open('txt/estoque.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.estoque = arq.readlines()

        # tira o \n
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                produto = Produtos(i[0], i[1], i[2])
                estoque = Estoque(produto, int(i[3]))
                est.append(estoque)
        print(cls.estoque)
        return est
    
# adiciona o produto no estoque(nome, preco, categoria e quantidade) ao estoque e os lê
# x = Produtos('macarrao', '8', 'alimento')
# y = Estoque(x, '3')
# DaoEstoque.salvar(y)
# DaoEstoque.ler()


# DAO FORNECEDOR
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('txt/fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + ' | ' + fornecedor.cnpj + ' | ' + fornecedor.telefone + ' | ' + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('txt/fornecedores.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.fornecedores = arq.readlines()

        # tira o \n e da split
        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        # cria a lista
        forn = []
        for i in cls.fornecedores:
            # percorre a lista de fornecedor
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        print(cls.fornecedores)
        return forn
    
# adiciona o produto no estoque(nome, preco, categoria e quantidade) ao estoque e os lê
# x = Fornecedor('SA multimarcas', '858412928', '11958423655', 'cosmeticos')
# DaoFornecedor.salvar(x)
# DaoFornecedor.ler()


# DAO PESSOA
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('txt/pessoa.txt', 'a') as arq:
            arq.writelines(pessoas.nome + ' | ' + pessoas.telefone + ' | ' + pessoas.cpf + ' | ' + pessoas.email + ' | ' + pessoas.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('txt/pessoa.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.clientes = arq.readlines()

        # tira o \n e da split
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        # cria a lista
        clientes = []
        for i in cls.clientes:
            # percorre a lista de fornecedor
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        print(cls.clientes)
        return clientes
    
# # adiciona o produto no estoque(nome, preco, categoria e quantidade) ao estoque e os lê
# x = Pessoa('gabrielly', '11956234877', '151958423655', 'gaby@gmail.com', 'rua: fjsofjowi')
# DaoPessoa.salvar(x)
# DaoPessoa.ler()


# DAO FUNCIONARIO
class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('txt/funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.nome + ' | ' + funcionario.telefone + ' | ' + funcionario.cpf + ' | ' + funcionario.email + ' | ' + funcionario.endereco + '|' + funcionario.clt)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('txt/funcionario.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.funcionarios = arq.readlines()

        # tira o \n e da split
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

         # cria a lista
        funcionarios = []
        for i in cls.funcionarios:
            # percorre a lista de fornecedor
            funcionarios.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        print(cls.funcionarios)
        return funcionarios
    
# adiciona o produto no estoque(nome, preco, categoria e quantidade) ao estoque e os lê
# x = Funcionario('lucas', '119580453950', '15889245253655', 'lucas@gmail.com', 'rua: 44hg8855owi', '481253318')
# DaoFuncionario.salvar(x)
# DaoFuncionario.ler()