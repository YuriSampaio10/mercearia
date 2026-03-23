from Models import *
from DAO import *
from datetime import datetime


class ControllerCategoria:

    def cadastraCategoria(self, novaCategoria):
        existe = False
        # Lê todas as categorias existentes do arquivo via DAO.
        x = DaoCategoria.ler()
        # Verifica se a categoria nova já está cadastrada.
        for i in x:
            if i.categoria.lower() == novaCategoria.lower():
                existe = True

        # Se não estiver, salva a categoria no arquivo e avisa que deu certo.
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastradada com sucesso')
        # Se já estiver, apenas avisa que não pode cadastrar duplicado.
        else:
            print('A categoria que deseja cadastrar ja existe')

# a = ControllerCategoria()
# a.cadastraCategoria('Frios')

    def removeCategoria(self, removeCategoria):
        # Ler todas as categorias
        x = DaoCategoria.ler()
        # Verifica se a categoria que você quer remover existe.
        cat = list(filter(lambda x: x.categoria.lower() == removeCategoria.lower(), x))
        
        # Se existir, remove a primeira ocorrência da lista.
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria.lower() == removeCategoria.lower():
                    del x[i]
                    break
            print('Categoria removida com sucesso')

# TODO: COLOCAR SEM CATEGORIA NO ESTOQUE

        # Escreve a lista atualizada de volta no arquivo.
        with open('txt/categoria.txt', 'w') as arq:
            for i in x :
                arq.writelines(i.categoria)
                arq.writelines('\n')

# a = ControllerCategoria()
# a.removeCategoria('frios')
# a.cadastraCategoria('FRIOS')

    def alterarCAtegoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        
        cat = list(filter(lambda x: x.categoria.lower() == categoriaAlterar.lower(), x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria.lower() == categoriaAlterada.lower(), x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada.lower()) if(x.categoria.lower() == categoriaAlterar) else(x), x))
            else:
                print('A categoria que deseja alterar já existe')
#TODO: ALTERAR A CATEGORIA,TAMBEM, DO ESTOQUE
        else:
            print('A categoria que deseja alterar não existe')

        
        with open('txt/categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
            print('Categoria alterada com sucesso!')

# a = ControllerCategoria()
# a.alterarCAtegoria('frutas', 'vegetais')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('CAtegoria vazia')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

# x = ControllerCategoria()
# x.mostrarCategoria()


class ControllerEstoque:

    def cadastrarProduto(self, nome, preco,categoria, quantidade):
        # Lê os produtos do estoque e as categorias cadastradas
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        # Verifica se a categoria informada existe
        h = list(filter(lambda c: c.categoria.lower() == categoria.lower(), y))
        # Verifica se o produto já está cadastrad
        est = list(filter(lambda p: p.produto.nome == nome, x ))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                estoque = Estoque(produto, quantidade)
                DaoEstoque.salvar(estoque)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto ja existe no estoque')
        else:
            print('Categoria inexistente')

x = ControllerEstoque()
x.cadastrarProduto('banana','5', 'verduras', '10')
