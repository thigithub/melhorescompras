try:
    idade = int(input('Por favor, insira a idade do aluno: '))
    idade_amigo = input('Por favor, forneça a idade do amigo: ')

    idade_total = idade + idade_amigo
except ValueError:
    print('Por favor entre com um valor inteiro para idade')
except TypeError:
    print('Estamos com problemas tecnico, tentando somar inteiro com string. Aguarde a correção do código.')
else:
    print("A idade do aluno é", idade)
    print("A idade do amigo é", idade_amigo)
    print("A idade total do aluno e do amigoo é", idade_total)
finally:
    print('Obrigado por usar o nosso programa')
