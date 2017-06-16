count = 3
rc = input()
while rc != 'A':
    count = count-1
    rc = input()
    print(count)
    if count == 0:
        print('Fim de jogo')
        break
if rc == 'A':
    print('Parabens')
print('Voce conseguiu')

