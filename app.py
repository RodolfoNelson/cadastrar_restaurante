import os #importando biblioteca OS, build in

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},#utilizando dicionario pré cadastro de restaurantes e guardaremos nessa var novos
                {'nome':'Pizza Suprema','categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina','categoria':'Italiano','ativo':False}] #parametros são passados seguindo essa sequencia


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n') #seleciona tudo, CTRL TAB, alinham 

def finalizar_app(): 
    exibir_subtitulo('Finalizando o app')#chama a função exibir_subtitulo e printa 'Finalizando o app'

def voltar_ao_menu_principal(): #criada função e refaturando o codigo, retirar as redundancias
    input('Digite uma tecla para voltar ao menu principal\n')
    main()

def opcao_invalida():
    print('Opção invalida !\n')
    voltar_ao_menu_principal()#na sequencia chama a função voltar ao menu principal
    
def exibir_subtitulo(texto): #criada função e refaturando o codigo, onde tinha sempre os print, função pega o texto que vai esta no pedaço do codigo, vai utilizar novamente, porém antes ira executar o cls, na sequencia print
    os.system('cls')#essa função pega o texto, limpa o terminal, e printa o texto
    print(texto)
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante) #armazenando dentro da lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso !\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes: #para cada restaurante na lista restaurantes
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try: #utilizando o try o programa ira tentar ler o input como int, caso não consiga ele chamara a função opcao_invalida, dessa forma resolvemos o problema caso o usuario digite uam letra str
        opcao_escolhida = int(input('Escolha uma opção: ')) #convertido para int, se não ele ira comprar com uma str

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    
    
def main():#a sequencia que o codigo sera executado
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':#converte o nome do app para main
 main()