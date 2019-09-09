# Tira todos os espaços, tabulações e quebra de linhas

import re

arq = open("novoArquivo.c", "r")
stri = arq.read()


def regexCharEsp(str):
	a = re.sub(r'\s|\n|\t', " ", stri)
	a = re.sub(r'\s\s*', " ", a)
	return a

strFinal = regexCharEsp(stri)

arqFinal = open("arquivoFinal.c", "w")
arqFinal.write(strFinal)
arqFinal.close()