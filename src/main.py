import random
# Projeto solicitado pelo Felipão da DIO.io, basicamente era pra fazer um sistema de classes que exibisse X informações relacionadas aquela classe
# Tem alguns detalhes, que não me atentei enquanto criava o projeto, que eram algumas boas práticas de PYTHON em específico, por exemplo, o estilo camel case não é utilizado em Python
# Mas como eu tenho uma familiaridade com o tipo camel case, não me atentei em usar o snake case, e também não me atentei em usar o padrão de classes e variáveis com nomes em inglês por boas praticas..
# Porém, decidi usar pseudo-aleatoriedade para fazer essa atividade de uma forma mais dinâmica e para ampliar os conhecimentos:
class player: # Ainda não dei uma funcionalidade pra esse classe.. mas logo mais ela tera, usando a função de randomizar nome e classe
    def __init__(self, nome, sobrenome, classe):
        self.nome = nome
        self.sobrenome = sobrenome
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
    listaNome = ['Tolric', 'HewFrith', 'Badic', 'Marmafrea', 'Egar', 'Thascas','Isenhal', 'Drax', 'Richethel', 'Bryt', 'Pabrand', 'Wenledryt']
    randomiName = random.choice(listaNome)
    return randomiName

def AleatorizarSobrenome(): # Uma simples função que contém uma variável armazenando uma lista, que é embaralhada e tem um resultado selecionado, algoritmo simples e eficaz, graças a biblioteca "Random"
    listaNome = ['Tolric', 'HewFrith', 'Badic', 'Marmafrea', 'Egar', 'Thascas','Isenhal', 'Drax', 'Richethel', 'Bryt', 'Pabrand', 'Wenledryt']
    randomiSobrename = random.choice(listaNome)
    return randomiSobrename

def AleatorizarClasse(): # A mesma ideia, porém com classes ao invés de nomes, também parte crucial do esqueleto do sistema
    listaClasse = ['Patrulheiro', 'Feiticeiro', 'Ladino', 'Guerreiro']
    randomiClasse = random.choice(listaClasse)
    return randomiClasse

                      
def main(): # Função principal, responsável por ser o epicentro de todo o código, basicamente reunindo tudo para compilação final
    print('=' * 50) 
    title = 'GERADOR DE HEROI RPG'
    print(f'{title:=^50}'.format(title))
    print('=' * 50)
    
    nome = AleatorizarNome() # fase de declaração de variáveis que armazenam retornos 
    classe = AleatorizarClasse() # fase de declaração de variáveis que armazenam retornos 
    sobrenome = AleatorizarSobrenome() # fase de declaração de variáveis que armazenam retornos 
    player_equipaments = Equipamento(classe) # fase de execução dos métodos para armazenar os dados
    player_equipaments.armamento() # fase de execução dos métodos para armazenar os dados
    player_informations = player(nome, sobrenome, classe) # fase de execução dos métodos para armazenar os dados
    player_informations.__init__ # fase de execução dos métodos para armazenar os dados
    while True: # Estrutura de repetição / decisão simples, com opções printando os objetos das classes
        print("O que deseja consultar?")
        print('[1] - Nome')
        print('[2] - Classe')
        print('[3] - Arma')
        print('[4] - Dano')
        print('[5] - Sair')
        # Inicio da estruta de decisão
        escolha = str(input('Selecione uma opção: '))
        if escolha == '1':
            print(f'O nome do seu herói é: {player_informations.nome} {player_informations.sobrenome}')
        elif escolha == '2':
            print(f'Sua classe inicial é: {player_informations.classe}')
        elif escolha == '3':
            print(f'Sua arma atual é: {player_equipaments.arma}')
        elif escolha == '4':
            print(f'Sua dano atual é de: {player_equipaments.dano}pts e seu tipo de dano é {player_equipaments.tipo}')
        elif escolha == '5':
            print('Encerrando programa..')
            break # Quebra do laço de repetição
        else:
            print('Escolha uma opção válida.')
    
main() #chamada da função principal, executando assim todo o código
