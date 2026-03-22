from Models import *


class DaoCategoria:
    # salva no arquivo texto categoria txt
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    # abre o arquivo texto
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
