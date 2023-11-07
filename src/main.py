import random
# Projeto solicitado pelo Felipão da DIO.io, basicamente era pra fazer um sistema de classes que exibisse X informações relacionadas aquela classe
# Porém, decidi usar pseudo-aleatoriedade para fazer essa atividade de uma forma mais dinâmica e para ampliar os conhecimentos:
class Jogador: # Ainda não dei uma funcionalidade pra esse classe.. mas logo mais ela tera, usando a função de randomizar nome e classe
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe

class Equipamento: # A classe mais importante do projeto, contendo dentro dela as hierarquias relacionadas as classes, como: armamento, dano, tipo
    def __init__(self, classe):
        self.arma = ''
        self.dano = 0
        self.tipo = ''
        self.classe = classe

    def armamento(self): # Dentro desse escopo, temos as condicionais que armazenam os resultados inerentes a cada classe
        if self.classe == 'Patrulheiro':
            self.arma = 'Arco e Flecha'
            self.dano = random.randint(10, 30)
            self.tipo = 'Perfurante a Distância'
        elif self.classe == 'Feiticeiro':
            self.arma = 'Cajado e Grimório'
            self.dano = random.randint(20, 40)
            self.tipo = 'Mágico'
        elif self.classe == 'Ladino':
            self.arma = 'Adaga Envenenada'
            self.dano = random.randint(10, 30 * 2)
            self.tipo = 'Perfurante e Furtivo'
        elif self.classe == 'Guerreiro':
            self.arma = 'Espada e Escudo'
            self.dano = random.randint(10, 30)
            self.tipo = 'Concussão e Curta-Distância'

    def listarArmamento(self): # Uma função que tem como foco listar as condicionais da classe, dentro desse escopo é passado o self que contem dos os dados necessários
        print(f'Seu armamento é um(a) {self.arma}, e seu dano atualmente é de {self.dano} AD/AP')

def AleatorizarNome(): # Uma simples função que contém uma variável armazenando uma lista, que é embaralhada e tem um resultado selecionado, algoritmo simples e eficaz, graças a biblioteca "Random"
    listaNome = ['Tolric', 'HewFrith', 'Badic', 'Marmafrea', 'Egar', 'Thascas',
             'Isenhal', 'Drax', 'Richethel', 'Bryt', 'Pabrand', 'Wenledryt']
    randomiName = random.choice(listaNome)
    return randomiName

def AleatorizarClasse(): # A mesma ideia, porém com classes ao invés de nomes, também parte crucial do esqueleto do sistema
    listaClasse = ['Patrulheiro', 'Feiticeiro', 'Ladino', 'Guerreiro']
    randomiClasse = random.choice(listaClasse)
    return randomiClasse

def main(): # Função principal, responsável por ser o epicentro de todo o código, basicamente reunindo tudo para compilação final
    randomizarClasse = AleatorizarClasse()
    print(randomizarClasse)
    armamento = Equipamento(randomizarClasse)
    armamento.armamento()
    armamento.listarArmamento()

main() # Chamada da função principal
