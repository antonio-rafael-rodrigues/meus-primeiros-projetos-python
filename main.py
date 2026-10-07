print('='*35)
print('    MEUS PRIMEIROS DESAFIOS    ')
print('   Formação Python - Guanabara  ')
print('='*35)

print('Escolha uma opção para testar:')
print(' Desafio 01: Mensagem de Boas-Vindas')
print(' Desafio 02: Validador de Data de Nascimento')
print(' Desafio 03: Mini Calculadora de Junção')
print('='*35)

opcao = input('Digite o número da sua opção (1, 2 ou 3): ')
print('-'*35)

if opcao == '1':
    # --- DESAFIO 1 ---
    nome = input('Qual é o seu nome? ')
    print(f'Olá {nome}! É um prazer te conhecer.')

elif opcao == '2':
    # --- DESAFIO 2 ---
    dia = input('Em qual dia você nasceu? ')
    mês = input('Em que mês você nasceu? ')
    ano = input('Qual ano você nasceu? ')
    print(f'Você nasceu no dia {dia} de {mês} de {ano}. Correto?')

elif opcao == '3':
    # --- DESAFIO 3 (Junção de Números/Textos) ---
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')
    print(f'Resultado da junção: {primeiro_numero + segundo_numero}')

else:
    print('Opção inválida! Por favor, execute o programa novamente e digite 1, 2 ou 3.')
print('='*35)
