#Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
s =float(input('Digite o salário do funcionário: R$'))
a =s*0.15
ns =s+a
print('O funcionário que recebia R${}, com 15% de aumento, passa a receber R${:.2f}' .format(s, ns)) 