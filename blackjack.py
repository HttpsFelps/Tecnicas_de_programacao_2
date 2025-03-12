import random
cont = 0
ac = 0
empate = 0
usuario = 0
maquina = 0
cartas = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
def num(n):
  n1 = cartas.index(n) + 1
  if n1 > 10:
    return 10;
  return n1;
def msg(n):
  print(n,"ganhou!")
print("Bem-vindo!")
while True:
  cont+=1
  print("Jogo black-jack")
  u1 = random.choice(cartas);
  u2= random.choice(cartas);
  u3 = random.choice(cartas);
  m1= random.choice(cartas);
  m2= random.choice(cartas);
  m3= random.choice(cartas);
  print("cartas do usuario")
  print(u1,u2,u3)
  su = num(u1)+num(u2)+num(u3)
  print('soma das cartas usuario: {}'.format(su) )
  print("cartas da maquina ")
  print(m1,m2,m3)
  sm = num(m1)+num(m3)+num(m3)
  print('soma das cartas maquina: {}'.format(sm) )

  if su > 21 and sm > 21:
    empate+=1
    print("Empate!")
  elif su > 21:
    maquina+=1
    msg('maquina ')
  elif sm > 21:
    usuario+=1
    msg('usuario ')
  elif sm > su:
    maquina +=1
    msg('maquina ')
  elif su > sm:
    usuario +=1
    msg('usuario ')

  # placar
  print('jogos   : ',cont)
  print('empates : ',empate)
  print('usuario : ',usuario)
  print('maquina : ',maquina)
  #parte que começa novamente
  confirma = input("jogar de novo? [S/N]")
  print("|------------------------|")
  if confirma == 'n' or confirma == 'N':
    print("|----------fim-----------|")
    break