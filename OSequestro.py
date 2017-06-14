inv = ['Pano']

print('Você está andando na rua a noite, voce percebe um estranho se aproximando.')
choic = int(input('\n1.Da a volta e tenta despista-lo\n2.Continua seu caminho e o ignora\n'))
if choic == 1:
    print('Ele começou a andar mais rápido ficando lado a lado com voce, ele tira um pano do bolso\ne coloca em sua boca você desmaia.')
    print('\nVocê acorda em um quarto escuro. Nele tem uma cama, uma privada, uma grade\n no teto e uma porta')
    choic12 = int(input('1.Verifica a porta, se está trancada ou não\n2.Procura algo no quarto'))
    if choic12 == 1:
        print('A porta está trancada, mas no caminho até ela você tropeça em uma pequena chave, você\n testa ela na porta mas ela não se encaixa vocêguarda a chave no bolso   ')
        inv.append('Chave')
        print('Seu inventário:',inv)
    elif choic12 == 2:
        print('Voce achou ums chave de fenda e um pequeno canivete')
        inv.append('Chave de fenda')
        inv.append('Canivete')
        print('Seu inventário:',inv)
    print('Voce se sente cansado e decide dormir')
    print('Voce acorda com uma voz vindo da grade acima de você:"HAHA, parece que você acordou colega\nVamos para sua primeira charada, olhe perto da porta ')
    print('Você se aproxima da porta e la você encontra duas folhas')
    print('Folha 1:\n ')
elif choic == 2:
    print('Ele para em sua frente bloqueando seu caminho, logo em seguida ele tira um pano do bolso\ne coloca em sua boca, você desmaia.')
    print('\nVocê acorda em um quarto escuro. Nele tem uma cama, uma privada, uma grade\n no teto e uma porta')
    choic22 = int(input('\n1.Verifica a porta, se está trancada ou não\n2.Procura algo no quarto'))
    if choic22 == 1:
        print('A porta está trancada, mas no caminho até ela você tropeça em uma pequena chave, você\n testa ela na porta mas ela não se encaixa vocêguarda a chave no bolso   ')
        inv.append('Chave')
        print('Seu inventário:',inv)
    elif choic22 == 2:
        print('Voce achou ums chave de fenda e um pequeno canivete')
        inv.append('Chave de fenda')
        inv.append('Canivete')
        print('Seu invetário:', inv)
    print('Voce se sente cansado e decide dormir')