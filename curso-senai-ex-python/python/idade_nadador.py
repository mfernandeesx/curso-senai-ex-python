import os 
os.system ("cls")

idade =int(input("digite a idade do nadador: "))

if idade >=5 and idade <=7:
    print("infantil A")
elif idade >=8 and idade <=11:
    print ("infantil B")
elif idade>=12 and idade <=13:
    print ("juvenil A")
elif idade>=14 and idade <=17:
    print ("juvenil B")
elif idade >=18:
    print ("adulto ")
else:
    print("a idade invalida ")