login = str( input ( 'Login: '))
familia = str( input( 'Familia: ' ))
nume = str( input( 'Nume: ' ))
numar = str( input( 'Nr. Tel: ' ))
data = str( input( 'Data: ' ))
luna = str( input( 'Luna: ' ))
an =  str( input( 'Anul: ' ))
 


gen = (familia, nume, numar, data, luna, an)
s = 0
a = 0
z = 0
fisier = open(login + '.txt', 'a+')
print('+373' + numar)
print('373' + numar)
print(gen[0])
print(gen[1])
print(gen[2])
print(gen[3])
print(gen[4])
print(gen[5])

fisier.write('+373' + numar  + '\n')
fisier.write('373' + numar + '\n')
fisier.write(gen[0] + '\n')
fisier.write(gen[1] + '\n')
fisier.write(gen[2] + '\n')
fisier.write(gen[3] + '\n')
fisier.write(gen[4] + '\n')
fisier.write(gen[5] + '\n')
while s < 36:
	print(gen[z] + '.' + gen[a])
	print(gen[z] + gen[a])

	fisier.write(gen[z] + '.' + gen[a] + '\n')
	fisier.write(gen[z] + gen[a] + '\n')
	a += 1
	if a == 6:
		z = z + 1
		a = 0
	s += 1
fisier.close()

