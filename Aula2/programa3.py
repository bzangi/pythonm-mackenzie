print("Insira a nota e o peso da prova 1: ")
a = float(input())
ap = float(input())
print("Insira a nota e o peso da prova 2: ")
b = float(input())
bp = float(input())
print("Insira a nota e o peso da prova 3: ")
c = float(input())
cp = float(input())

media = (a*ap+b*bp+c*cp)/(ap+bp+cp)
print('Média = ', media)