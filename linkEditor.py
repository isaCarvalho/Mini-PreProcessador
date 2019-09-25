# Faz a link edição dos includes e defines

import re

def lerArquivo(nomeArq):
	arq = open(nomeArq, "r")

	return arq.read()

def include(stri):
	nomeInc = re.match(r'\#include\s*\<(.*)\>', stri)
	arq2 = lerArquivo(nomeInc.group(1))

	return stri.replace(nomeInc.group(0), arq2)

def define(stri):
	print(stri)
	constDefine = re.search(r'\#define\s\s*(\w+)\s\s*(\d+)', stri)
	stri = stri.replace(constDefine.group(1), constDefine.group(2))

	return re.sub(r'\#define\s*(\d+)\s*(\d+)', "", stri)
	

aux = lerArquivo("arquivo.c")

novoArq = include(aux)
novoArq = define(novoArq)

print(novoArq)

novo = open("novoArquivo.c", "w");
novo.write(novoArq)