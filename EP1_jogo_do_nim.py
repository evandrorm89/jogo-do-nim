def computador_escolhe_jogada (n, m):
    x = 1
    temp = 0
    while x <= m:
        if (n - x) % (m + 1) == 0:
            temp = x
        x = x + 1
    if temp == 0 and n >= m:
        return m
    elif temp != 0 and temp <= n:
        return temp
    else:
        return n


def usuario_escolhe_jogada (n, m):
    jog_feita = False
    while not jog_feita:
        jogada = int (input ("Quantas peças você vai tirar? "))
        if jogada <= m and jogada <= n and jogada > 0:
            jog_feita = True
        else:
            print ("Oops! Jogada inválida! Tente de novo.")
    return jogada


def partida ():
    n = int (input ("Quantas peças? "))
    m = int (input ("Limite de peças por jogada? "))
    comp_comeca = vc_comeca = False
    vez = 1

    if n % (m+1) != 0:
        comp_comeca = True
        print ("O computador começa!")
    else:
        vc_comeca = True
        print ("Você começa!")
        

    while n > 0:
        comp_ganhou = vc_ganhou = False
        if comp_comeca:
            
            if vez % 2 != 0:
                peca_tirada = computador_escolhe_jogada (n, m)
                print ("O computador tirou", peca_tirada, "peças.")
                n = n - peca_tirada
                print ("Agora restam", n, "peças no tabuleiro.")
                if n <= 0:
                    comp_ganhou = True
               
            else:
                peca_tirada = usuario_escolhe_jogada (n, m)
                print ("Você tirou", peca_tirada, "peças.")
                n = n - peca_tirada
                print ("Agora restam", n, "peças no tabuleiro.")
                if n == 0:
                    vc_ganhou = True
            vez = vez + 1
        else:
            
            if vez % 2 != 0:
                peca_tirada = usuario_escolhe_jogada (n, m)
                print ("Você tirou", peca_tirada, "peças.")
                n = n - peca_tirada
                print ("Agora restam", n, "peças no tabuleiro.")
                if n == 0:
                    vc_ganhou = True
            
            else:
                peca_tirada = computador_escolhe_jogada (n, m)
                print ("O computador tirou", peca_tirada, "peças.")
                n = n - peca_tirada
                print ("Agora restam", n, "peças no tabuleiro.")
                if n <= 0:
                    comp_ganhou = True
            vez = vez + 1
    if comp_ganhou:
        print ("Fim de jogo! O computador ganhou!")
        
    else:
        print ("Fim de jogo! Você ganhou!")
    return comp_ganhou
        


print ("Bem-vindo ao jogo do NIM! Escolha:")
print()
opcao = 3
while opcao != 1 and opcao != 2:
    
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato")
    opcao = int (input ())
    if opcao !=1 and opcao != 2:
        print ("Opção inválida!")
    

if opcao == 1:
    print ("Você escolheu uma partida isolada")
    partida()
else:
    vc = 0
    comp = 0
    i = 1
    print ("Você escolheu um campeonato!")
    
    while i <=3:
        print()
        print("*** Rodada", i, " ***")
        print()
        
        if partida() == True:
            comp = comp + 1
        else:
            vc = vc + 1
        i = i + 1
    print ("*** Final do campeonato! ***")
    print ()
    print ("Placar: Você", vc, "X", comp, "Computador")
