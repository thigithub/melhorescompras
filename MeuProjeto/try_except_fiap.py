class IdadeMaximaExcedida(Exception):
    def __str__(self):
        return ('A idade não pode ser superior a 125 anos')

try:
    idade = int(input('Por favor, insira a idade do aluno: '))
    idade_amigo = int(input('Por favor, forneça a idade do amigo: '))

    idade_total = idade + idade_amigo
    if idade < 0 or idade_amigo < 0:
        raise  ValueError('Valor da idade não pode ser menor que zero')
    elif idade > 125 or idade_amigo > 125:
        raise IdadeMaximaExcedida
except ValueError as Error:
    #print('Por favor entre com um valor inteiro para idade')
        print('Erro', Error)
except TypeError:
    print('Estamos com problemas tecnico, tentando somar inteiro com string. Aguarde a correção do código.')
else:
    print("A idade do aluno é", idade)
    print("A idade do amigo é", idade_amigo)
    print("A idade total do aluno e do amigoo é", idade_total)
finally:
    print('Obrigado por usar o nosso programa')
