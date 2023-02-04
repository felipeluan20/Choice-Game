print('''
                                   __ 
             /|/              .--'"`__`
            / |-.,,____       |--'"`__`
         __/|   ______/       |--'"`__`
     ..""_ |   |              |--'"`_ `
     ..""_ |   |              |--'"` `
     ..""_ |   |           __,'-'"``
     ..""_ |   |     __,."`    /
     .."" ,\   ,\,."`  ,       `:
          \ :,; `: \`: :  ,-"\  .
          :    ` | | ' ;_"\   `. `:
          | .^.  ;_,.""    \  | ;  .
          : ; ', :          `.\  \ `;
          | ;  : |           '`, : ;`
          :;    ;|           /;  ' /
          :;    ;:          ';   ;;
          ;:    :|         //    :/
          ||    ||        //    /;
          ||    ||       ,;    ;/
          "     "       "     "

''')
print("""
        Bem vindo às Aventuras de Minduim!
        Sua missão é achar um cabo de carregador para comer.""")

caminho1 = input("""
        Você chegou da creche e precisa achar um cabo de carregador para mastigar.
        Você vai para esquerda ou direita? """)
if caminho1 == "direita":
    print("""
        Você deu de cara com Rinaldo Tadeu com uma almofada! 
        Sua sapecagem foi descoberta e você perdeu!""")
elif caminho1 == "esquerda":
    caminho2 = input("""
        Você está entre a cozinha e a escada.
        Você vai para a cozinha ou sobe a escada? """)
    if caminho2 == "cozinha":
        print("""
        Você deu de cara com uma Sunny enfurecida e apanhou!
        Você perdeu.""")
    elif caminho2 == "escada":
        caminho3 = input("""
        Após você subir as escadas, você vê três portas abertas. 
        Você entra na porta da esquerda, na porta da frente ou na porta da direita? """)
        if caminho3 == "porta da esquerda" or caminho3 == "esquerda":
            print("""
        Você viu um gato andando e não aguentou seu impulso de correr atrás e se esqueceu do seu objetivo. 
        Você perdeu.""")
        elif caminho3 == "porta da direita" or caminho3 == "direita":
            print("""
        Você tentou abrir a porta da direita porém a mesma estava trancada.
        frustrado, você continua a tentar até o fim dos tempos.
        Você perdeu.""")
        else:
            print("""
        Você encontrou um carregador novinho pronto para ser degustado!
        Parabéns, você venceu!""")
