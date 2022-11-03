
from ast import While
import modulo_agenda_sql as agenda
import os,time

os.system('cls')


print('     Agenda de Contatos')

agenda.getConnection()

while True:
  print('1 - Cadastrar contato;')
  print('2 - Listar contato;')
  print('3 - Listar todos os contatos;')
  print('4 - Apagar contato;')
  print('5 - Apagar todos os contatos;')
  print('6 - Sair.')

  op = int(input('Entre com a opção desejada: '))

  if op == 1:
    os.system('cls')
    loop = True
    while loop==True:
      nome = input('Digite o nome:')
      if len(nome)>0:
        while True:
          try:
            tel = int(input('Digite o telefone:'))
            agenda.adiciona(nome,tel)
            loop = False
            break
            
            
          except: 
            print("Telefone do contato não pode ser vazio ou conter letras/caracteres")
      else:
        print("Nome do contato não pode ser vazio")
      


    
    
  elif op == 2:
    os.system('cls')
    id = input('Digite o id para a pesquisa:')
    agenda.mostraContato(id)
    
  elif op == 3:
    os.system('cls')
    agenda.mostraLista()
    os.system('cls') 
    
  elif op == 4:
    os.system('cls')
    agenda.mostraLista()
    id = input('Digite o id que deseja apagar:')
    agenda.apagaContato(id)
  elif op == 5:
    os.system('cls')
    agenda.apagaTodosContatos()
  elif op == 6:
    break
  else:
    os.system('cls')
    print('Digite uma opção valida!')
    time.sleep(3)

os.system('cls')
print('-'*30)
print('Obrigado por usar a agenda!!!')
print('-'*30)
