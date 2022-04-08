nome = input("Qual o seu nome: ")
num1 = int(input("Quanto você tirou na primeira prova: "))
num2 = int(input("Quanto você tirou na segunda prova: "))
total = num1 + num2 
media = total/2
ps = media<5
if ps == True:
  print("Tente melhorar suas notas")
else:
  print("Parabéns",nome,"você passou")