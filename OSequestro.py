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
        print('Voce se sente cansado e decide dormir')
        print('Voce acorda com uma voz vindo da grade acima de você:"HAHA, parece que você acordou colega\nVamos para sua primeira charada, olhe perto da porta ')
        print('Você se aproxima da porta e la você encontra duas folhas')
        print('Folha 1:\nEu vou te explicar como o jogo vai funcionar meu querido amigo\n simples, eu te passo uma charada, você a resolve, você terá três chances de resolve-la, mas antes você precisa de uma caneta não é mesmo?! ')
        print('Folha 2:\nVa,os começar com uma fácil o que você acha?\n No alvorecer 4 pes tem, ao anoitecer mais 2 pés vêm ')
        rc = input('Qual das coisas nesse quarto ele se refere? ')
        # Codigo para as chances
        count = 2
        while rc != 'cama':
            count = count - 1
            print('Voce tem mais', count, 'Chances')
            rc = input('Tente de novo')
        if count == 0:
            print('Fim de jogo')
            exit()

        if rc == 'Cama' or 'cama':
            print('Você se aproxima da cama e acha uma caneta, marca a resposta e joga ela pela fresta da porta')
    elif choic12 == 2:
        print('Voce achou ums chave de fenda e um pequeno canivete')
        inv.append('Chave de fenda')
        inv.append('Canivete')
        print('Seu inventário:',inv)
        print('Voce se sente cansado e decide dormir')
        print('Voce acorda com uma voz vindo da grade acima de você:"HAHA, parece que você acordou colega\nVamos para sua primeira charada, olhe perto da porta ')
        print('Você se aproxima da porta e la você encontra duas folhas')
        print('Folha 1:\nEu vou te explicar como o jogo vai funcionar meu querido amigo\n simples, eu te passo uma charada, você a resolve, você terá três chances de resolve-la, mas antes você precisa de uma caneta não é mesmo?! ')
        print('Folha 2:\nVa,os começar com uma fácil o que você acha?\n No alvorecer 4 pes tem, ao anoitecer mais 2 pés vêm ')
        rc = input('Qual das coisas nesse quarto ele se refere? ')
        #Codigo para as chances
        count = 2
        while rc != 'cama':
            count = count-1
            print('Voce tem mais', count, 'Chances')
            rc = input('Tente de novo')
        if count == 0:
            print('Fim de jogo')
            exit()

        if rc == 'Cama' or 'cama':
            print('Você se aproxima da cama e acha uma caneta, marca a resposta e joga ela pela fresta da porta')


elif choic == 2:
    print('Ele para em sua frente bloqueando seu caminho, logo em seguida ele tira um pano do bolso\ne coloca em sua boca, você desmaia.')
    print('\nVocê acorda em um quarto escuro. Nele tem uma cama, uma privada, uma grade\n no teto e uma porta')
    choic22 = int(input('\n1.Verifica a porta, se está trancada ou não\n2.Procura algo no quarto'))
    if choic22 == 1:
        print('A porta está trancada, mas no caminho até ela você tropeça em uma pequena chave, você\n testa ela na porta mas ela não se encaixa vocêguarda a chave no bolso   ')
        inv.append('Chave')
        print('Seu inventário:',inv)
        print('Voce se sente cansado e decide dormir')
        print('Voce acorda com uma voz vindo da grade acima de você:"HAHA, parece que você acordou colega\nVamos para sua primeira charada, olhe perto da porta ')
        print('Você se aproxima da porta e la você encontra duas folhas')
        print('Folha 1:\nEu vou te explicar como o jogo vai funcionar meu querido amigo\n simples, eu te passo uma charada, você a resolve, você terá três chances de resolve-la, mas antes você precisa de uma caneta não é mesmo?! ')
        print('Folha 2:\nVa,os começar com uma fácil o que você acha?\n No alvorecer 4 pes tem, ao anoitecer mais 2 pés vêm ')
        rc = input('Qual das coisas nesse quarto ele se refere? ')
        # Codigo para as chances
        count = 2
        while rc != 'cama':
            count = count - 1
            print('Voce tem mais', count, 'Chances')
            rc = input('Tente de novo')
            if count == 0:
                print('Fim de jogo')
                exit()
        if rc == 'cama':
            print('Você se aproxima da cama e acha uma caneta, marca a resposta e joga ela pela fresta da porta')

    elif choic22 == 2:
        print('Voce achou ums chave de fenda e um pequeno canivete')
        inv.append('Chave de fenda')
        inv.append('Canivete')
        print('Seu invetário:', inv)
        print('Voce se sente cansado e decide dormir')
        print('Voce acorda com uma voz vindo da grade acima de você:"HAHA, parece que você acordou colega\nVamos para sua primeira charada, olhe perto da porta ')
        print('Você se aproxima da porta e la você encontra duas folhas')
        print('Folha 1:\nEu vou te explicar como o jogo vai funcionar meu querido amigo\n simples, eu te passo uma charada, você a resolve, você terá três chances de resolve-la, mas antes você precisa de uma caneta não é mesmo?! ')
        print('Folha 2:\nVa,os começar com uma fácil o que você acha?\n No alvorecer 4 pes tem, ao anoitecer mais 2 pés vêm ')
        rc = input('Qual das coisas nesse quarto ele se refere? ')
        # Codigo para as chances
        count = 2
        while rc != 'cama':
            count = count - 1
            print('Voce tem mais', count, 'Chances')
            rc = input('Tente de novo')
            if count == 0:
                print('Fim de jogo')
                exit()
        if rc == 'cama':
            print('Você se aproxima da cama e acha uma caneta, marca a resposta e joga ela pela fresta da porta')