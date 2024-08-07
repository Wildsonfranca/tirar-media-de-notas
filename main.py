

quantidade =int(input(f'Quantas notas você deseja informar para saber a média?'))

if quantidade <=0:
    print('Numero de notas precisa ser positivo:')
else:
    #inicializa a soma das notas
    soma_notas =0 

     #loop para ler as notas
    for i in range(quantidade):
          #recebe cada nota do usuario
        nota = float(input(f' Digite a nota {i+1}:'))
          #adiciona a nota a soma total
        soma_notas += nota
    media = soma_notas/quantidade
     #Exibe o resultado
    print(f'A média das notas é: {media:.2f}')     