import os


#opa seila qualuqer coisa
restaurantes = [{'nome':'praça', 'categoria': 'japonesa', 'ativo':False},
                {'nome': 'Pizza suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome': 'Cauan Dog', 'categoria':'Brasileira', 'ativo':False}]

def exibir_nome_do_programa(): 
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opçoes():
    """" Esse função é responsavel para exibir as opçoes"""
    print('1. Cadastrar restuarante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do resturante')
    print('4. Sair\n')

def finalizar_app():
    """" Esse função é responsavel para finalizar o app"""
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal(): 
     """" Esse função é responsavel para voltar ao menu principal"""
     input('Digite uma tecla para voltar ao menu principal')
     main()

    
def opcao_invalida():
    """" Esse função é responsavel por mostrar que uma opção foi invalida"""
    print('opcao invalida !\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): 
    """" Esse função é responsavel por exibir os subtitulos das funções"""
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_resturante():
    """" Esse função é responsavel por cadastrar um novo restaurante"""
    exibir_subtitulo('Cadastro de novos restuarantes ')
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar : ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} : ')
    dados_do_restaurante={'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso !')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """" Esse função é responsavel por listar todos os restaurantes"""
    exibir_subtitulo('Listando restaurantes')
    print(f'{'nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo_restaurante = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo_restaurante}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """"Esse função é responsavel por  alterar o estado do restaurante"""

    exibir_subtitulo('Alterndando estado do restaurante')
    nome_restaurante = input('Nome do restaurante que deseja alterna o estado:')
    restaurante_encontrado = False 

    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']: 
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso' #ternario 
            print(mensagem)
    if not restaurante_encontrado: 
        print('O restaurante nao foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcoes():
    """" Esse função é responsavel por escolher as opções """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_resturante()
        elif opcao_escolhida == 2: 
           listar_restaurantes()
        elif opcao_escolhida == 3: 
           alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except: 
        opcao_invalida()

def main(): 
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opcoes()
    
if __name__ == '__main__': 
    main()


