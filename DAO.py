from Models import *


class DaoCategoria:
    # salva no arquivo texto categoria txt
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    # abre o arquivo texto da categoria.txt
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.categoria = arq.readlines()
            
        # tira o \n
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat  
    
class DaoVenda:
    # metodo salvar da DAO venda
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + '|' + venda.itensVendido.preco + '|' + venda.itensVendido.categoria + '|' + venda.vendedor + '|' + venda.comprador + '|' + str(venda.quantidadeVendida) + '|' + venda.data)
            arq.writelines('\n')


    # abre o arquivo texto da venda.txt
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            # pega tudo que tem no arquivo texto e joga dentro de categoria
            cls.venda = arq.readlines()

        # tira o \n
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
       
        vende = []
        for i in cls.venda:
            produto = Produtos(i[0], i[1], i[2])
            venda = Venda(produto, i[3], i[4], i[5])
            vende.append(venda)
        return vende
    

x = DaoVenda.ler()
print(x)