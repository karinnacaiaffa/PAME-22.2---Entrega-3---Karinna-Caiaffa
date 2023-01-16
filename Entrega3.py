############## CLASSES ############## 

class Consultor:
    def __init__(self, nomeConsultor, id, usuario, senha) -> None:
        self.nomeConsultor = nomeConsultor
        self.id = id
        self.usuario = usuario
        self.__senha = senha

    def nomeConsultor():
        nomeConsultor = input ("Insira o nome do Consultor: ")   

    def id() -> int:
        id = int(input("Insira a id do Consultor: ")) 

    def usuario() -> int:
        usuario = input("Insira o nome do usuario: ")

    def senha (self):
        return self.__senha


class Gerente (Consultor):
     def __init__(self, nomeGerente, id, usuario, senha) -> None:
        super().__init__(id, usuario, senha)
        self.nomeGerente = nomeGerente

class Projeto(Consultor):
    def __init__(self, nomeProjeto, Cliente, idConsultor, idGerente, Desenvolvimento, Concepcao, IdentidadeVisual) -> None:
        super().__init__(id, )

    def AvancaDesenvolvimento(self):
        self.Desenvolvimento -= 1
        return

    def AvancaConcepcao(self):
        self.Concepcao -= 1
        return
    
    def AvancaIdentidadeVisual(self):
        self.IdentidadeVisual -= 1
        return
    
class Sistema(Projeto):
    pass


############## PROGRAMA PRINCIPAL ############## 

def menu1():

    print ("""\033[1;37m
        ATENCAO: Voce ainda nao esta logado. Selecione uma das opcoes abaixo: \033[m
       \033[0;32m 1- Logar \033[m
       \033[0;33m 2- Criar projeto \033[m
       \033[0;34m 3- Remover projeto \033[m
       \033[0;35m 4- Criar Gerente \033[m
       \033[0;36m 5- Remover Gerente \033[m
       \033[0;31m 6- Sair do programa \033[m
        """)

    opcao = int(input())

    if opcao == 1 :
            logar = input("Aperte 1 se voce for Consultor e 2 se for Gerente: ")
            if logar == 1:
                acessuser = input("Insira seu nome de usuario: ")
                acesspin = int (input ("Insira a senha: "))
                if acessuser == usuario & acesspin == __senha:
                    menu2()
                else:
                    print ("Unmatched. Try again.")
            elif logar == 2:
                acessuser = input("Insira seu nome de usuario: ")
                acesspin = int (input ("Insira a senha: "))
                if acessuser == usuario & acesspin == __senha:
                    menu3()
                else:
                    print ("Unmatched. Try again.")
            else:
                print ("Opcao invalida.")
                menu1()
                
    elif opcao == 2 :
        menu1()
        
    elif opcao == 3 :
        menu1()

    elif opcao == 4 :
        menu1()

    elif opcao == 5 :
        menu1() 

    elif opcao == 6:
        print ("                                ")
        print (""" \033[0;34m O programa foi encerrado.
                
               				 	The end. \033[m   """)
        print ("                                ")

    else:
        print ("                                ")
        print (""" \033[0;35m  Por favor, escolha uma opcao existente.	\033[m	""")
        print ("                                ") 
        menu1()

    return

menu1()

############## MENU 2 - CONSULTOR ############## 

def menu2():

    print ("""\033[1;37m
        Ola, consultor. Selecione uma das opcoes abaixo: \033[m
       \033[0;32m 1- Ver seus dados \033[m
       \033[0;33m 2- Modificar seus dados \033[m
       \033[0;34m 3- Verificar projetos em que esta alocado \033[m
       \033[0;35m 4- Avancar com um projeto \033[m
       \033[0;36m 5- Pedir retirada de um projeto \033[m
       \033[0;31m 6- Sair do programa \033[m
        """)

    opcao = int(input())
    
    if opcao == 1 :
        menu1()
	
    elif opcao == 2 :
        menu1()

    elif opcao == 3 :
        menu1()

    elif opcao == 4 :
        escolha = int( input("Selecione 1 se quiser avançar em Desenvolvimento, 2 se em Concepção e 3 se em Identidade Visual."))
        if escolha == 1:
            AvancaDesenvolvimento(self)
        elif escolha == 2:
            AvancaConcepcao(self)

        elif escolha == 3:
            AvancaIdentidadeVisual(self)
        menu1()

    elif opcao == 5 :
        menu1() 

    elif opcao == 6:
        print ("                                ")
        print (""" \033[0;34m O programa foi encerrado.
                
               				 	The end. \033[m   """)
        print ("                                ")

    else:
        print ("                                ")
        print (""" \033[0;35m  Por favor, escolha uma opcao existente.	\033[m	""")
        print ("                                ") 

        menu1()

    return


############## MENU 3 - GERENTE ############## 

def menu3():

    print ("""\033[1;37m
        Ola, gerente. Selecione uma das opcoes abaixo: \033[m
       \033[0;32m 1- Ver seus dados \033[m
       \033[0;33m 2- Modificar seus dados \033[m
       \033[0;34m 3- Verificar projetos em que esta alocado \033[m
       \033[0;35m 4- Avancar com um projeto \033[m
       \033[0;36m 5- Retirar Consultor \033[m
       \033[0;31m 6- Passar projeto a outro gerente \033[m
       \033[0;31m 7- Entregar projeto \033[m
       \033[0;31m 8- Sair do programa \033[m
        """)

    opcao = int(input())
    
    if opcao == 1 :
        menu1()
	
    elif opcao == 2 :
        menu1()

    elif opcao == 3 :
        menu1()

    elif opcao == 4 :
        escolha = int( input("Selecione 1 se quiser avançar em Desenvolvimento, 2 se em Concepção e 3 se em Identidade Visual."))
        if escolha == 1:
            AvancaDesenvolvimento(self)
        elif escolha == 2:
            AvancaConcepcao(self)

        elif escolha == 3:
            AvancaIdentidadeVisual(self)
        menu1()

    elif opcao == 5 :
        menu1() 

    elif opcao == 6:
        print ("                                ")
        print (""" \033[0;34m O programa foi encerrado.
                
               				 	The end. \033[m   """)
        print ("                                ")

    else:
        print ("                                ")
        print (""" \033[0;35m  Por favor, escolha uma opcao existente.	\033[m	""")
        print ("                                ") 

        menu1()

    return