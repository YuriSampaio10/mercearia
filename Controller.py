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
            if i.categoria == novaCategoria:
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
        cat = list(filter(lambda x: x.categoria == removeCategoria, x))
        
        # Se existir, remove a primeira ocorrência da lista.
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria.lower() == removeCategoria.lower():
                    del x[i]
                    break
            print('Categoria removida com sucesso')

        # Escreve a lista atualizada de volta no arquivo.
        with open('txt/categoria.txt', 'w') as arq:
            for i in x :
                arq.writelines(i.categoria)
                arq.writelines('\n')

a = ControllerCategoria()
# a.removeCategoria('Frios')
a.cadastraCategoria('Legumes')
