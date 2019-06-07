import os

dir = 'Y:/'
principalDir = os.listdir(dir)
arquivosLidos = 0

def buscaRecursiva(sub):
	
	global arquivosLidos
	
	print('recursiva ' + sub)
	
	subdir = os.listdir(sub)
	
	for s in subdir:
		if os.path.isfile(sub + s):
			criatxt = open('resultado.txt', 'a', encoding='utf-8')
			criatxt.write(str(sub) + str(s) + ' \n')
			criatxt.close()
			arquivosLidos = arquivosLidos + 1			
			print(arquivosLidos)
		else:
			buscaRecursiva(sub + s + '/')
		
for a in principalDir:

	if os.path.isfile(dir + a):
		criatxt = open('resultado.txt', 'a', encoding='utf-8')
		criatxt.write(str(dir) + str(a) + ' \n')
		criatxt.close()
		arquivosLidos = arquivosLidos + 1
		print(arquivosLidos)
	else:
		buscaRecursiva(dir + a + '/')
	
print('Finish!')