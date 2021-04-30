'''
----------------- Validador de CPF ----------------
  
            __Author__ = LouizF
            __License__= GPLv3
            __Github__ = https://github.com/TronGuy
            __Python Version___ = 3.x.x

---------------------------------------------------
'''

#Entrada de dados
cpf = input('Digite o seu cpf:').strip()

#verificação
if len(cpf) == 11 and cpf.isnumeric():
  
  #transformação de entrada de String para Lista/Vetor
  cpf_vet = list(cpf)
  #declaração das variáveis
  resultado1 = 0
  resultado2 = 0

  #Loop para acumular valores
  for n,valores in enumerate(range(10, 1, -1)):
    resultado1 += valores * int(cpf_vet[n])
  
  resultado1 = 11 - (resultado1 % 11)
  resultado1 = abs(resultado1)
  resultado1 = 0 if resultado1 > 9 else resultado1
  
  resultado2 += resultado1 * 2

  for n,values in enumerate(range(11, 2, -1)):
    resultado2 += values  * int(cpf_vet[n])

  resultado2 = 11 - (resultado2 % 11)
  resultado2 = abs(resultado2)
  resultado2 = 0 if resultado2 > 9 else resultado2

  #verifica se o CPF é válido ou não :D
  final = 'o CPF é válido!' if resultado1 == int(cpf_vet[9]) and \
  resultado2 == int(cpf_vet[10]) else 'o CPF é inválido!'

  #resultado final
  print(f'{cpf} {final}')

else:
  print('Digite um CPF válido!')
