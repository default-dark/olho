import random
from rich import print 
import os 
import time
class machines:
    def gerador(self):
        olho1 = 'qwertyuiopasdfghjklzxcvbnm' 
        olho2 = "QWERTYUIOPASDFGHJKLZXCVBNM"
        escarlate = "0123456789"
        print("[red][+][green] digite quantidade de caracter para gerar")
        ge1 = int(input(">> "))
        machine  = olho1 + olho2 + escarlate 
        machine2 = escarlate + olho2 + olho1 
        machine3 = escarlate + olho1 + olho2 
        machine4 = olho2 + escarlate + olho1 
        machine5 = olho1 + escarlate + olho2 
        machine6 = olho2 + olho1 + escarlate 

        visao = "".join(random.sample(machine,ge1)) 
        visao2 = "".join(random.sample(machine2,ge1))
        visao3 = "".join(random.sample(machine3,ge1))
        visao4 = "".join(random.sample(machine4,ge1))
        visao5 = "".join(random.sample(machine5,ge1))
        visao6 = "".join(random.sample(machine6,ge1))
        visao7 = "".join(random.sample(machine,ge1))
        visao8 = "".join(random.sample(machine2,ge1))
        visao9 = "".join(random.sample(machine3,ge1))
        visao10 = "".join(random.sample(machine4,ge1))
        visao11 = "".join(random.sample(machine5,ge1))
        visao12 = "".join(random.sample(machine6,ge1))
        visao13 = "".join(random.sample(machine,ge1))
        visao14 = "".join(random.sample(machine6,ge1))
        visao15 = "".join(random.sample(machine,ge1))
        visao16 = "".join(random.sample(machine2,ge1))
        visao17 = "".join(random.sample(machine3,ge1))
        visao18 = "".join(random.sample(machine4,ge1))
        visao19 = "".join(random.sample(machine5,ge1))
        visao20 = "".join(random.sample(machine,ge1))
        visao21 = "".join(random.sample(machine2,ge1))
        visao22 = "".join(random.sample(machine3,ge1))
        visao23 = "".join(random.sample(machine4,ge1))
        visao24 = "".join(random.sample(machine5,ge1))

        print("[red]-"*60)
        print("[blue]1.[green]gerador de senha simples")
        print("[blue]2.[green]gerador de senha avançada")
        print("[blue]3.[green]olho escarlate")
        print("[blue]5.[green]gerar senha simples")
        print("[blue]4.[green]info")
        print("[red]-"*60)
        olhos = int(input(f"\033[1;32m_=_=>  "))

        match olhos:
            case 1:
                    print("[red] digite um nome do arquivo? ")
                    ar1 = input(">>> ")
                    print("[red]-"*10)
                    print("[yellow]gerar")
                    date = input("digite data de nacimento: ")
                    name = input("digite nome: ")
                    mae = input("digite o nome da mae: ")
                    pai = input("digite o nome do pai: ") 
                        
                    l1 = visao + name + mae 
                    l2 = name + date + visao 
                    l3 = pai + date + visao2 
                    l4 = mae + date + visao3 
                    l5 = date + mae + visao4 
                    l6 = visao5 + date + pai 
                    l7 = visao6 + name + mae 
                    l8 = name + visao7  
                    l9 = mae + visao8   
                    l10 = pai + visao9
                    with open(ar1,"a")as chave1:
                        chave1.write(l1+'\n'+l2+'\n'+l3+'\n'+l4+'\n'+l5+'\n'+l6+'\n'+l7+'\n'+l8+'\n'+l9+'\n'+l10)
                    with open(ar1,"r")as ler:
                        print(ler.read())
            case 2:
                    print("[red][+][green]digite o nome do arquivo")
                    ar2 = input(f">>> ")
                    print("[red]-"*10)
                    print("[yellow]gerar")
                    name2 = input("digite um nome: ")
                    mae2 = input("digite o nome da mae: ")
                    pai2 = input("digite o nome do pai: ")
                    vo = input("digite o nome da vó: ")
                    v1 = input("digite o nome do vô: ")
                    tia = input("digite o nome da tia: ")
                    tio = input("digite o nome do tio: ")
                    prima = input("digite o nome da prima: ") 
                    primo = input("digite o nome do primo: ")
                        
                    ge1 = name2 + visao 
                    ge2 = pai2 + visao2 
                    ge3 = mae2 + visao3  
                    ge4 = vo + visao4  
                    ge5 = v1 + visao5  
                    ge6 = tia + visao6  
                    ge7 = tio + visao7   
                    ge8 = prima + visao8  
                    ge9 = primo + visao9 
                    ge10 = name2 + pai2 + visao10  
                    ge11 = pai2 + name2 + visao11  
                    ge12 = name2 + mae2 + visao12  
                    ge12 = mae2 + name2 + visao13 
                    ge13 = pai2 + mae2 + visao14 
                    ge14 = mae2 + pai2 + visao15 

                    with open(ar2,"a")as ch1:
                        ch1.write(ge1+"\n"+ge2+"\n"+ge3+"\n"+ge4+"\n"+ge5+"\n"+ge6+"\n"+ge7+"\n"+ge8+"\n"+ge9+"\n"+ge10+"\n"+ge11+"\n"+ge12+"\n"+ge13+"\n"+ge14)
                    with open(ar2,"r")as readp:
                        print(readp.read()) 
            case 3:
                    print("[red]digite nome do arquivo? ")
                    ar3 = input(">>> ")
                    name3 = input("digite um nome: ")
                    idade3 = input("digite a idade: ")
                    mae3 = input("digite o nome da mae: ")
                    pai3 = input("digite o nome do pai: ")
                    vo = input("digite o nome da vó: ")
                    v2 = input("digite o nome do vô: ")
                    cao = input("digite o nome do cachorro: ")
                    tia = input("digite o nome da tia: ")
                    tio = input("digite o nome do tio: ")
                    primo = input("digite o nome do primo: ")
                    prima = input("digite onome da prima: ")
                    amigo = input("digite o nome do amigo: ")
                    namo = input("digite o nome da namorada: ") 

                    g1 = name3 + visao 
                    g2 = pai3 + visao2 
                    g3 = mae3 + visao3 
                    g4 = vo + visao4  
                    g5 = v2 + visao5  
                    g6 = cao + visao6  
                    g7 = name3 + mae3 + visao7  
                    g8 = tia + visao8  
                    g9 = tio + visao9  
                    g10 = primo + visao10  
                    g11 = prima + visao11  
                    g12 = amigo + visao12  
                    g13 = namo + visao13  
                    g14 = name3 + idade3 + visao14  
                    g15 = idade3 + name3 + visao15   
                    g16 = primo + idade3 + visao16  
                    g17 = prima + idade3 + visao17  
                    g18 = amigo + name3 + visao18  
                    g19 = name3 + amigo + visao19  
                    g20 = visao + pai3 + mae3 + visao20 
                    g21 = name3 + pai3 + visao21  
                    g22 = name3 + mae3 + visao22  
                    g23 = name3 + amigo + visao23  
                    g24 = name3 + cao + visao24 

                    with open(ar3,"a")as m2:
                        m2.write(g1+"\n"+g2+"\n"+g3+"\n"+g4+"\n"+g5+"\n"+g6+"\n"+g7+"\n"+g8+"\n"+g9+"\n"+g10+"\n"+g11+"\n"+g12+"\n"+g13+"\n"+g14+"\n"+g15+"\n"+g16+"\n"+g17+"\n"+g18+"\n"+g19+"\n"+g19+"\n"+g20+"\n"+g21+"\n"+g22+"\n"+g23+"\n"+g24)
                    with open(ar3,"r")as m2:
                        print(m2.read())
            case 4:
                print("""[green]
                      criador::default-dark
                      redes sociais não vou falar porque sou timido [°^_^°]
                      kkkk 
                      github: https://github.com/default-dark
                      e isso perá 
                      """)
            case 5:
                print("digite uma palavra chave? [red]:)")
                chave = input(">>> ")
                chave_master = chave + visao 
                print("[red][°^_^°][yellow]escreva sua senha num papel")
                print("[green]senha gerada:[red]",chave_master)
    def me1(self):
        os.system("clear")
        menus = random.randint(1,4)
        if menus == 1:
            print("""[purple]
                      ──▄────▄▄▄▄▄▄▄────▄───
                      ─▀▀▄─▄█████████▄─▄▀▀──
                      ─────██─▀███▀─██──────
                      ───▄─▀████▀████▀─▄────
                      ─▀█────██▀█▀██────█▀──
                      criador::: default-dark
                      """)
        elif menus == 2:
            print("""[red] 
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⠤⠤⠤⠴⠤⢤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠛⠉⠉⣠⠊⠁⠀⠀⢀⣀⣀⡀⠀⠀⠉⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠁⠀⠀⠀⣀⡔⡏⠀⠐⠊⣉⣀⡀⠀⠀⠀⠀⠀⠀⠤⣀⠉⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢠⢞⠁⠀⢀⡠⠖⠊⢉⡑⠒⣾⡀⠀⠀⠀⠀⠀⠉⠑⠢⣄⠀⠀⠀⠀⠙⠲⡈⠳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣰⡫⠃⢀⠔⠁⠀⢀⣠⠎⠀⠀⢣⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢦⠉⠢⡄⠀⠈⢢⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⣸⡗⢁⡔⠀⢀⠔⠁⢋⣼⠀⠀⡆⠈⣧⠀⠰⡀⠠⡀⠐⢤⣀⠀⠀⠀⠱⣄⠈⠢⡱⡄⠱⡈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⣰⠆⣸⠏⡠⡞⠀⣠⠋⢀⡰⢫⡇⠀⢰⠀⠀⣯⢧⡀⠘⡄⢷⡀⠈⢻⢿⣶⣄⡀⠘⣷⣄⠑⡵⡀⠹⡘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡴⡫⡞⡼⢀⣼⠇⢠⠋⢠⢃⢷⠀⣸⡄⠀⣇⣇⠹⣦⡈⢪⣿⣦⡀⠱⣵⡙⢟⣦⡘⡿⡧⡈⢷⡀⢳⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣮⡞⡘⣜⠇⡞⡜⢠⡟⢀⡇⣬⢺⡀⣿⣷⡀⠸⣹⢆⠙⡝⣶⢝⡷⡿⣦⣈⠻⡄⢫⣻⣾⡘⠹⣮⡳⡀⢣⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠞⠋⣼⠁⡝⢸⣼⠇⣇⣾⡇⣼⡇⡇⡎⣧⢫⡇⣧⡀⢻⡌⡧⣈⠪⣧⣻⢿⢻⢮⡳⣿⣦⣣⢻⣳⠀⢻⡷⣝⢌⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠸⢡⢿⢿⢰⢸⡎⣷⣻⠇⡇⠇⣿⣿⣧⣧⣷⣄⢣⣹⡼⣷⣬⣛⢦⡳⣫⣑⡜⡼⡌⢣⢳⣣⠈⡇⢻⡷⣅⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠇⡎⢨⡜⢸⣞⢀⢹⣼⢸⡇⡀⢿⡿⡹⣇⢹⣽⣷⣿⣿⣱⢳⣣⡹⡟⡟⣷⡜⣾⣱⠈⣆⢯⡄⠃⠸⠹⡜⣷⣽⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣦⢁⢸⡇⣼⢿⠀⡘⡏⣾⡌⣧⠸⣸⡣⢏⠙⣱⣻⡈⣿⢳⢧⠳⣷⣳⡄⢸⣽⡼⡍⡆⡟⡜⣥⢲⢠⣇⢻⣾⣆⠉⠻⢦⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡞⢸⣰⢉⣾⠀⣇⢸⡁⡷⣻⣦⢷⣷⡼⣦⢳⡳⡳⣳⣧⠿⣷⣘⣿⣿⣆⣿⣿⣿⠇⣷⢣⡿⢸⡈⡼⣮⣧⡛⠧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣇⡶⡇⡎⣿⣧⢩⢾⣵⣿⣻⣿⣿⣽⡬⣿⣻⣿⢦⡙⢿⡧⡟⣰⣿⣿⣿⣯⣽⣿⢀⢿⡇⡿⣸⣧⢹⣿⡙⢷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡅⢰⡇⠇⣏⣎⢾⣿⣿⠏⣴⣿⣿⡟⠻⣷⠷⣿⣿⡞⠓⣬⡽⣽⣿⣷⠶⣨⡿⢙⣿⣧⢿⣷⣷⣧⣿⢷⡌⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⣾⢿⡈⡏⡾⣧⣫⠹⣧⣙⠿⠟⣃⣴⡿⠊⢸⢏⣀⡀⡰⢯⣘⠿⢿⣷⢋⡓⡾⡟⢿⡼⣸⢹⡍⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢸⣷⢻⣦⣷⡮⡞⢿⡌⠳⠈⠉⠙⠉⠡⠛⠀⢀⣾⠊⠙⡻⡝⠈⢫⢛⡟⠁⠀⣽⢽⢋⢞⢧⡇⣾⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣰⣿⣏⣷⡎⢋⢧⡄⠀⠀⠀⠀⠀⠀⢠⠾⢶⣤⣴⣧⢱⠀⡼⠋⣤⣄⣼⡟⡘⣿⣿⡟⢿⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⣾⡿⣿⣻⡛⡿⠫⠺⣾⡀⠀⠀⠀⠀⢠⡟⢺⣿⣿⡿⢿⠼⣛⠿⡶⣾⣫⣏⠞⣼⣿⣿⡇⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢡⣷⣧⣇⣧⢀⣤⣾⣿⣤⣠⣤⢴⣻⡏⢹⣿⡟⠛⡛⢿⣶⣶⣿⢿⢷⣼⠿⣿⣧⣿⡇⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢻⡿⣿⠻⣿⣵⡿⣯⠵⠊⡤⢪⠏⠇⣴⣿⣄⣟⣥⣿⣿⠿⣿⣿⡯⣿⣿⣿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣨⣥⣼⣾⡏⠀⢿⣿⣎⠆⠀⠀⢇⠏⡜⠀⣿⣼⢋⣾⣿⣿⣥⣴⣿⣿⣿⡾⡉⠛⣿⡽⣧
                  criador::: default-dark""")
        elif menus == 3:
            print("""[green]
                      .... NO! ...                  ... MNO! ...
                      ..... MNO!! ...................... MNNOO! ...
                      ..... MMNO! ......................... MNNOO!! .
                      .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
                      ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
                      ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
                      ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
                       ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
                      ....... MMMMM..    OPPMMP    .,OMI! ....
                       ...... MMMM::   o.,OPMP,.o   ::I!! ...
                          .... NNM:::.,,OOPM!P,.::::!! ....
                            .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
                            ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
                              .. MMMMMNNOOMMNNIIIPPPOO!! ......
                              ...... MMMONNMMNNNIIIOO!..........
                      ....... MN MOMMMNNNIIIIIO! OO ..........
                      ......... MNO! IiiiiiiiiiiiI OOOO ...........
                      ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
                      .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
                      ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
                      ...... OO! ................. ON! .......
                      ................................
                      criador::: default-dark""")
        elif menus == 4:
            print("""[blue]
                      ...                            
                     ;::::;                           
                     ;::::; :;                          
                     ;:::::'   :;                         
                     ;:::::;     ;.                        
                     ,:::::'       ;           OOO\         
                     ::::::;       ;          OOOOO\        
                     ;:::::;       ;         OOOOOOOO       
                     ,;::::::;     ;'         / OOOOOOO      
                     ;:::::::::`. ,,,;.        /  / DOOOOOO    
                    .';:::::::::::::::::;,     /  /     DOOOO   
                     ,::::::;::::::;;;;::::;,   /  /        DOOO  
                    ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
                    :`:::::::`;::::::;;::: ;::#  /            DOOO
                    ::`:::::::`;:::::::: ;::::# /              DOO
                    `:`:::::::`;:::::: ;::::::#/               DOO
                     :::`:::::::`;; ;:::::::::##                OO
                     ::::`:::::::`;::::::::;:::#                OO
                     `:::::`::::::::::::;'`:;::#                O 
                      `:::::`::::::::;' /  / `:#                  
                       ::::::`:::::;'  /  /   `# 
                      criador:::default-dark""")
    def me2(self):
        rd = random.randint(1,3)
        if rd == 1:
            print("""[yellow]
                      ┏━┓┏┓░┏┓┏┓┏━┓  ┏━┓┏━━┓┏━┓┏━━┓┏━┓┏┓░┏━━┓┏━━┓┏━┓
                      ┃┃┃┃┃░┃┗┛┃┃┃┃  ┃┳┛┃━━┫┃┏┛┃━━┫┃╋┃┃┃░┃┏┓┃┗┓┏┛┃┳┛
                      ┃┃┃┃┗┓┃┏┓┃┃┃┃  ┃┻┓┣━━┃┃┗┓┣━━┃┃┓┫┃┗┓┃┣┫┃░┃┃░┃┻┓
                      ┗━┛┗━┛┗┛┗┛┗━┛  ┗━┛┗━━┛┗━┛┗━━┛┗┻┛┗━┛┗┛┗┛░┗┛░┗━┛""")
        elif rd == 2:
            print("""[red]
                      ╱╱╱╱╭╮╱╭╮╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱
                      ╱╱╱╱┃┃╱┃┃╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱╱╱
                      ╭━━╮┃┃╱┃╰━╮╭━━╮   ╭━━╮╭━━╮╭━━╮╭━━╮╭━╮┃┃╱╭━━╮╰╮╭╯╭━━╮
                      ┃╭╮┃┃┃╱┃╭╮┃┃╭╮┃   ┃┃━┫┃━━┫┃╭━╯┃╭╮┃┃╭╯┃┃╱┃╭╮┃╱┃┃╱┃┃━┫
                      ┃╰╯┃┃╰╮┃┃┃┃┃╰╯┃   ┃┃━┫┣━━┃┃╰━╮┃╭╮┃┃┃╱┃╰╮┃╭╮┃╱┃╰╮┃┃━┫
                      ╰━━╯╰━╯╰╯╰╯╰━━╯   ╰━━╯╰━━╯╰━━╯╰╯╰╯╰╯╱╰━╯╰╯╰╯╱╰━╯╰━━╯
                      ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
                      ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
                      """)
        elif rd == 3:
            print("""[purple]
                       █▀▀█ █░░ █░░█ █▀▀█   █▀▀ █▀▀ █▀▀ █▀▀█ █▀▀█ █░░ █▀▀█ ▀▀█▀▀ █▀▀
                       █░░█ █░░ █▀▀█ █░░█   █▀▀ ▀▀█ █░░ █▄▄█ █▄▄▀ █░░ █▄▄█ ░░█░░ █▀▀
                       ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀   ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀
                      """)
pass
bot = machines()
bot.me1() 
bot.me2()
bot.gerador()
