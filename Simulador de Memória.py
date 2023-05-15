c1 = '00000000'
c2 = '00000000'
c3 = '00000000'
c4 = '00000000'
c5 = '00000000'
c6 = '00000000'
c7 = '00000000'
c8 = '00000000'
c9 = '00000000'
c10 = '00000000'
c11 = '00000000'
c12 = '00000000'
c13 = '00000000'
c14 = '00000000'
c15 = '00000000'
c16 = '00000000'
eraser = '00000000'

print('''SIMULADOR DE MEMÓRIA
INSIRA:
[W] - Para efetuar a operação de escrita
[R] - Para efetuar a operação de litura
[L] - Para listar todas as células
[E] - Para limpar todas as células
[S] - Para parar a simulação ''')

instrução = input('Insira aqui a operação que deseja efetuar:')

while instrução != 'S' or instrução != 's':
    if instrução == 'L' or instrução == 'l':
        print('ESTADO DA MEMÓRIA')
        print(f'''
         {c1}
         {c2}
         {c3}
         {c4}
         {c5}
         {c6}
         {c7}
         {c8}
         {c9}
         {c10}
         {c11}
         {c12}
         {c13}
         {c14}
         {c15}
         {c16}''')
    elif instrução == 'R' or instrução == 'r':
        end = input('Insira aqui o endereço para leitura(4 bits):')
        if end == '0000':
            print(c1)
        elif end == '0001':
            print(c2)
        elif end == '0010':
            print(c3)
        elif end == '0100':
            print(c4)
        elif end == '0101':
            print(c5)
        elif end == '0011':
            print(c6)
        elif end == '0111':
            print(c7)
        elif end == '1000':
            print(c8)
        elif end == '1001':
            print(c9)
        elif end == '1011':
            print(c10)
        elif end == '1010':
            print(c11)
        elif end == '1101':
            print(c12)
        elif end == '1100':
            print(c13)
        elif end == '1110':
            print(c14)
        elif end == '0110':
            print(c15)
        elif end == '1111':
            print(c16)
        else:
            print('Verifique se digitou o endereço corretamente, e se o número de bits foi respeitado!')
    elif instrução == 'W' or instrução == 'w':
        end = input('Insira aqui o endereço para escrita(4 bits):')
        dado = input('Insira aqui o que deseja escrever na célula(até 8 bits):')
        if end == '0000':
            c1 = dado
        elif end == '0001':
            c2 = dado
        elif end == '0010':
            c3 = dado
        elif end == '0100':
            c4 = dado
        elif end == '0101':
            c5 = dado
        elif end == '0011':
            c6 = dado
        elif end == '0111':
            c7 = dado
        elif end == '1000':
            c8 = dado
        elif end == '1001':
            c9 = dado
        elif end == '1011':
            c10 = dado
        elif end == '1010':
            c11 = dado
        elif end == '1101':
            c12 = dado
        elif end == '1100':
            c13 = dado
        elif end == '1110':
            c14 = dado
        elif end == '0110':
            c15 = dado
        elif end == '1111':
            c16 = dado
        else:
            print('Verifique se digitou o endereço corretamente, e se o número de bits foi respeitado!')
    elif instrução == 'E' or instrução == 'e':
        c1 = eraser
        c2 = eraser
        c3 = eraser
        c4 = eraser
        c5 = eraser 
        c6 = eraser
        c7 = eraser
        c8 = eraser 
        c9 = eraser
        c10 = eraser
        c11 = eraser 
        c12 = eraser 
        c13 = eraser 
        c14 = eraser
        c15 = eraser
        c16 = eraser
        print('As células foram limpas!')
    else:
        print('Verifique se digitou a instrução corretamente, obedeça as teclas indicadas.')
    print('''SIMULADOR DE MEMÓRIA
INSIRA:
[W] - Para efetuar a operação de escrita
[R] - Para efetuar a operação de litura
[L] - Para listar todas as células 
[E] - Para limpar todas as células
[S] - Para parar a simulação ''')
    instrução = input('Insira aqui a operação que deseja efetuar:')

print('Encerrando a simulação')

     

