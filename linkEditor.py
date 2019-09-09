# Faz a link edição dos includes

import re

def lerArquivo(nomeArq):
	arq = open(nomeArq, "r")

	return arq.read()

def fecharArq(arq):
	arq.close()

def include(stri):
	nomeInc = re.match(r'\#include\s*\<(.*)\>', stri)

	arq2 = lerArquivo(nomeInc.group(1))

	return stri.replace(nomeInc.group(0), arq2)

aux = lerArquivo("arquivo.c")
novoArq = include(aux)

print(novoArq)

novo = open("novoArquivo.c", "w");
novo.write(novoArq)