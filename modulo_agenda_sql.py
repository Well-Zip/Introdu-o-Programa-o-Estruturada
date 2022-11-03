# Agenda de Contatos
import sqlite3,time,os

def getConnection():
    #conectando
    connection = sqlite3.connect('agenda.db')
    #definindo um cursor
    cursor = connection.cursor()
    #criando a tabela(se não existir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             fone TEXT
    );
    """)
    #retorna a conexão
    return connection




def adiciona(nome, tel):
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO contatos(nome,fone) VALUES('{nome}','{tel}')")
    connection.commit()
    connection.close()

    os.system('cls')
    print('-'*30)
    print("Informações".center(40))
    print(f"O Contato {nome} foi Adicionado!")
    print('-'*30)
    time.sleep(3)
    os.system('cls')

def mostraContato(id):
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT nome FROM contatos WHERE id={id}")
    nome_contato = cursor.fetchone()
    cursor.execute(f"SELECT fone FROM contatos WHERE id={id}")
    fone_contato = cursor.fetchone()
    connection.commit()
    connection.close()

    os.system('cls')
    
    if fone_contato == None and nome_contato==None:
        print('-'*30)
        print("Informações".center(40))
        print("Nenhum contato pertence ao ID: ",id)
        print('-'*30)

    else:
        for nome in nome_contato:
            for phone in fone_contato:
                
                print('-'*30)
                print("Informações".center(40))
                print(f"\nO seguinte contato pertencente ao ID :{id}\nNome do contato: {nome}\nNumero do Contato:{phone}\n") 
                print('-'*30)
        
    
    time.sleep(5)
    os.system('cls')
    
    #print('Função que mostra contado pelo id!')


def mostraLista():
    connection = getConnection()
    cursor = connection.cursor()
    linhas = cursor.execute("SELECT * FROM contatos").fetchall()
    connection.close()

    os.system('cls') 
    print('-'*30)
    print('\tTodos os contatos')
    print('-'*30)
    print('ID\tNome\t\tTelefone')
    print('\n'.join(map(lambda x: str(x[0]) + '\t' + str(x[1]) + '\t\t' + str(x[2]), linhas)))
    print('-'*30)
    time.sleep(7)
    
    

def apagaContato(id):
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT nome FROM contatos WHERE id={id}")
    nome_contato = cursor.fetchone()
    cursor.execute(f"DELETE FROM contatos WHERE id={id}")
    connection.commit()
    connection.close()

    if nome_contato == None:
        os.system('cls') 
        print('-'*30)
        print("Informações".center(40))
        print("Nenhum contato pertence ao ID: ",id)
        print('-'*30)
        time.sleep(3)
        os.system('cls') 

    else:    
        for name in nome_contato:
            nome_contato=name

        os.system('cls') 
        print('-'*30)
        print("Informações".center(40))
        print(f"O contato {nome_contato} foi apagado")
        print('-'*30)
        time.sleep(3)
        os.system('cls') 
        #print('Função que apaga o contato')

def apagaTodosContatos():
    
    while True:
        print('-'*30)
        print("Informações".center(40))
        confirmacao = input("Essa operação vai apagar todos os contatos\nTem certeza que deseja continuar?\n0-Cancelar\n1-Confirmar\n")
        print('-'*30)
        try:
            confirmacao=int(confirmacao)
            if confirmacao == 1:
                connection = sqlite3.connect('agenda.db')
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM contatos")
                connection.commit()
                connection.close()
                os.system('cls')
                print('-'*30)
                print("Informações".center(40))
                print("Todos os contatos foram apagados")
                print('-'*30)
                
                time.sleep(3)
                os.system('cls')
                break
            elif confirmacao == 0:
                os.system('cls')
                break
            else:
                os.system('cls')
                print('-'*30)
                print("Informe uma operação valida")
                print('-'*30)
                
                time.sleep(3)
                os.system('cls')
        except:
            print('-'*30)
            print("Informe um valor numerico")
            print('-'*30)
            time.sleep(3)
            os.system('cls')
    #print('Função que apaga todos os contatos')

